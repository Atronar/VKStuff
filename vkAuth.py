import vk_api;
from getpass import getpass;
import json;
from os.path import exists as fileexists;
import time;
import vk_api.upload;

# Двухфакторная авторизация
def auth_handler():
   # Код двухфакторной аутентификации
   key = input("Код подтверждения входа: ")
   # Если: True - сохранить, False - не сохранять.
   remember_device = True
   return key, remember_device

# Обработка капчи
def captcha_handler(captcha, key=None):
   """ При возникновении капчи вызывается эта функция и ей передается объект
       капчи. Через метод get_url можно получить ссылку на изображение.
       Через метод try_again можно попытаться отправить запрос с кодом капчи
   """
   if 'VkApi._vk_login' in str(captcha.func):
      raise vk_api.exceptions.AuthError()
   if key is None:
      try:
         key = input("Введите капчу {0}: ".format(captcha.get_url()))
      except EOFError:
         key = input()
   key = key.strip()
   # Пробуем снова отправить запрос с капчей
   return captcha.try_again(key)

def captcha_saver(captcha):
   with open('captcha','wt',encoding='utf-8') as f:
      for s in [captcha.sid, captcha.func, captcha.args, captcha.kwargs, captcha.url, time.time()]:
         f.write(str(s)+'\n')
   print(captcha);
   print('\a');

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
         vk_config_json = open("vk_config.v2.json");
         vk_config_data = vk_config_json.read();
         vk_access_token = json.loads(vk_config_data)[str(login)]['token']["app6479356"]["scope_140492255"]['access_token'];
         vk_config_json.close();
      else:
         vk_access_token = vk.token['access_token'];
   else:
      if fileexists("vk_config.v2.json"):
         vk_config_json = open("vk_config.v2.json");
         vk_config_data = vk_config_json.read();
         if str(login) in json.loads(vk_config_data):
            vk_access_token = json.loads(vk_config_data)[str(login)]['token']["app6479356"]["scope_140492255"]['access_token'];
            vk_config_json.close();
            vk = vk_api.VkApi(login, auth_handler=auth_handler, captcha_handler=captcha_handler, app_id=6479356, scope=140492255);
         else:
            vk_config_json.close();
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

# В классе некоторые исправления
class betterVkUpload(vk_api.upload.VkUpload):
    # Добавлен caption - описание фото
    def photo_wall(self, photos, user_id=None, group_id=None, caption=None):
        """ Загрузка изображений на стену пользователя или в группу

        :param photos: путь к изображению(ям) или file-like объект(ы)
        :type photos: str or list

        :param user_id: идентификатор пользователя
        :param group_id: идентификатор сообщества (если загрузка идет в группу)
        """

        values = {}

        if user_id:
            values['user_id'] = user_id
        elif group_id:
            values['group_id'] = group_id

        if caption:
            values['caption'] = caption

        response = self.vk.method('photos.getWallUploadServer', values)
        url = response['upload_url']

        with vk_api.upload.FilesOpener(photos) as photos_files:
            response = self.vk.http.post(url, files=photos_files)

        values.update(response.json())

        return self.vk.method('photos.saveWallPhoto', values)