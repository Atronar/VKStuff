# v. 200425
import vk_api;
from getpass import getpass;
import json;
from os.path import exists as fileexists;
import time;
import vk_api.upload;
import cv2;
import requests;
import numpy as np;
import sys

def beep():
   try:
      import winsound
      winsound.MessageBeep()
   except:
      print('\a')

# Двухфакторная авторизация
def auth_handler():
   # Код двухфакторной аутентификации
   key = input("Код подтверждения входа: ")
   # Если: True - сохранить, False - не сохранять.
   remember_device = True
   return key, remember_device

# Обработка капчи
def captcha_handler(captcha, key=None, show_captcha=False, go_flag=None, stdin=None):
   """ При возникновении капчи вызывается эта функция и ей передается объект
       капчи. Через метод get_url можно получить ссылку на изображение.
       Через метод try_again можно попытаться отправить запрос с кодом капчи
   """
   if 'VkApi._vk_login' in f"{captcha.func}":
      raise vk_api.exceptions.AuthError()
   while not key:
   #   try:
         captcha_url = captcha.get_url();
         if show_captcha:
            show_img(requests.get(captcha_url).content, captcha_url.rsplit("sid=",1)[-1].split("&",1)[0]);
         if hasattr(go_flag, "value"):
            back_flag = go_flag.value
         beep()
         if stdin:
            print(stdin)
            sys.stdin = stdin;
         key = input(f"Введите капчу {captcha_url}: ");
         if hasattr(go_flag, "value"):
            go_flag.value = back_flag
         if show_captcha:
            cv2.destroyAllWindows();
   #   except EOFError:
   #      cv2.waitKey(10);
   #      key = False
   key = key.strip()
   # Пробуем снова отправить запрос с капчей
   return captcha.try_again(key)

def captcha_saver(captcha):
   with open('captcha','wt',encoding='utf-8') as f:
      for s in (captcha.sid, captcha.func, captcha.args, captcha.kwargs, captcha.url, time.time()):
         f.write(f'{s}\n')
   print(captcha);
   print('\a'); beep()

def too_many_rps_handler(self, error):
   """ Обработчик ошибки "Слишком много запросов в секунду".
       Ждет полсекунды и пробует отправить запрос заново

   :param error: исключение
   """

   print('Много запросов! Ждём 0.5 сек...', error.method)
   time.sleep(0.5)
   return error.try_method()

# Автоматизированный скрипт авторизации, может принимать логин и пароль, либо запрашивает их, если они не были сохранены
# Возвращает объект, необходимый для взаимодействия с vk_api и токен доступа
def vk_auth(login=None,password=None,captcha_handler=captcha_saver):
   vk_api.VkApi.too_many_rps_handler=too_many_rps_handler;
   if login is None:
      login = input("Введите логин: ");
   if password is not None:
      vk = vk_api.VkApi(login, password, auth_handler=auth_handler, captcha_handler=captcha_handler, app_id=6479356, scope=140492255);
      if fileexists("vk_config.v2.json"):
         with open("vk_config.v2.json") as vk_config_json:
            vk_config_data = vk_config_json.read();
            vk_access_token = json.loads(vk_config_data)[f"{login}"]['token']["app6479356"]["scope_140492255"]['access_token'];
      else:
         vk_access_token = vk.token['access_token'];
   else:
      if fileexists("vk_config.v2.json"):
         with open("vk_config.v2.json") as vk_config_json:
            vk_config_data = vk_config_json.read();
            if f"{login}" in json.loads(vk_config_data):
               vk_access_token = json.loads(vk_config_data)[f"{login}"]['token']["app6479356"]["scope_140492255"]['access_token'];
               vk = vk_api.VkApi(login, auth_handler=auth_handler, captcha_handler=captcha_handler, app_id=6479356, scope=140492255);
            else:
               password = getpass("Введите пароль: ");
               vk = vk_api.VkApi(login, password, auth_handler=auth_handler, captcha_handler=captcha_handler, app_id=6479356, scope=140492255);
               vk_access_token = vk.token['access_token'];
      else:
         password = getpass("Введите пароль: ");
         vk = vk_api.VkApi(login, password, auth_handler=auth_handler, captcha_handler=captcha_handler, app_id=6479356, scope=140492255);
         vk_access_token = vk.token['access_token'];
   vk.auth(token_only=True);
   try:
      with vk_api.VkRequestsPool(vk) as pool:
         my_id = pool.method('users.get', {'access_token': vk_access_token});
         my_screen_id = pool.method('account.getProfileInfo');
      my_id = my_id.result[0]['id']
      my_screen_id = my_screen_id.result['screen_name']
   except vk_api.exceptions.ApiError:
      vk, vk_access_token, my_id, my_screen_id = vk_auth(login,getpass("Введите пароль: "))
   return vk, vk_access_token, my_id, my_screen_id;

# Взятие лучшего по качеству изображения
# Принимает attach["photo"]
# Возвращает словарь вида {'url', 'width', 'height'}
def get_max_photo(photo):
   # attach["photo"]['sizes'] возвращает словарь
   if 'sizes' in photo:
      for size_item in photo['sizes']:
         try:
            if size_item['width']==max(i['width'] for i in photo['sizes']):
               return size_item
         except:
            print(photo['sizes'])
            raise
   # attach["photo"] возвращает ссылку
   else:
      # Берём фото лучшего качества
      if "photo_2560" in photo:
         photo_size = "photo_2560";
      elif "photo_1280" in photo:
         photo_size = "photo_1280";
      elif "photo_807" in photo:
         photo_size = "photo_807";
      elif "photo_604" in photo:
         photo_size = "photo_604";
      elif "photo_130" in photo:
         photo_size = "photo_130";
      elif "photo_75" in photo:
         photo_size = "photo_75";
      item = {'url': photo[photo_size]}
      if 'width' in photo:
         item.update({'width':photo['width'], 'height':photo['height']})
      return item;

# Функция показа изображения без перехвата управления вызванным окном
def show_img(img_file,title=''):
   cv_img = cv2.imdecode(np.asarray(bytearray(img_file)), 1);
   cv2.namedWindow(title);
   cv2.moveWindow(title, 400,300);
   cv2.imshow(title,cv_img);
   cv2.waitKey(1);

# В классе некоторые исправления
class betterVkUpload(vk_api.upload.VkUpload):
    # Добавлен caption - описание фото
    pass