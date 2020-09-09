import vk_api;
import vkAuth;
import sys
import design, preview
from PyQt5 import QtWidgets, QtCore, QtGui;
import io;
import os;
import time;
from urllib.request import urlretrieve;
import json;
from FileOptimizer import FileOptimizer;
import re;

import win32clipboard  # http://sourceforge.net/projects/pywin32/
def copyClipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
def pasteClipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data

__all__ = ["VKStuffApp","previewWindow"]

MAX_VKSPP_SEARCH_COUNT = 100;

def in_any_attach(searchedText,listAttachs):
   for attach in listAttachs:
      type_attach = attach['type'];
      if 'text' in attach[type_attach] and searchedText in attach[type_attach]['text'].lower():
         return True;
   return False;

class SPPThread(QtCore.QThread):
   vkspp_progressBar_setRange = QtCore.pyqtSignal(int);
   vkspp_progressBar_setTextVisible = QtCore.pyqtSignal(bool);
   vkspp_progressBar_setValue = QtCore.pyqtSignal(int);
   vkspp_respTableWidget_insertRow = QtCore.pyqtSignal(list);
   statusBar_showMessage = QtCore.pyqtSignal(str,int);
   vkspp_respTableWidget_setEnabled = QtCore.pyqtSignal(bool);
   vkspp_respGroupBox_setEnabled = QtCore.pyqtSignal(bool);

   def __init__(self,app,params,searched,search_desc,search_attach):
      super().__init__();
      self.app = app;
      self.params = params;
      self.searched = searched;
      self.search_desc = search_desc;
      self.search_attach = search_attach;

   @QtCore.pyqtSlot()
   def run(self):
       posts_count = 0;
       try: 
          resp = self.app.vk.method('wall.get', self.params);
          count_items = resp['count'];
          self.vkspp_progressBar_setRange.emit(count_items);
          self.vkspp_progressBar_setTextVisible.emit(True);
          while self.params['offset'] < count_items:
             if self.params['offset']:
                resp = self.app.vk.method('wall.get', self.params);
             items = resp['items'];
             self.vkspp_progressBar_setValue.emit(self.params['offset']);

             if items:
                if self.search_desc and self.search_attach:
                   items = [item for item in items
                            if self.searched in item['text'].lower()
                               or ('attachments' in item
                                   and in_any_attach(self.searched,item['attachments'])
                                  )
                           ];
                elif self.search_desc:
                   items = [item for item in items
                            if self.searched in item['text'].lower()];
                elif self.search_attach:
                   items = [item for item in items
                            if 'attachments' in item
                               and in_any_attach(self.searched,item['attachments'])];
                posts_list = [{'link':f"https://vk.com/wall{post['owner_id']}_{post['id']}",
                               'date':time.strftime("%d.%m.%Y %X",time.localtime(post['date'])),
                               'num_attach': f"{len(post['attachments']) if 'attachments' in post else 0}",
                               'author': f"{post['signer_id'] if 'signer_id' in post else 0}"
                              } for post in items];
                posts_count += len(posts_list);
                self.vkspp_respTableWidget_insertRow.emit(posts_list);

                self.params['offset'] += 100;
          self.vkspp_progressBar_setValue.emit(count_items);
          if posts_count == 0:
             self.vkspp_respGroupBox_setEnabled.emit(False);
             self.vkspp_respTableWidget_setEnabled.emit(False);
             self.statusBar_showMessage.emit('Постов не найдено',2000);
          else:
             self.statusBar_showMessage.emit("Поиск завершён",2000);

       except vk_api.exceptions.ApiError as e:
          if 'Access denied' in f"{e}":
             self.statusBar_showMessage.emit('Нет доступа к сообществу',10000);
             self.vkspp_progressBar_setTextVisible.emit(False);
             print('\a',end='\r');
          elif 'owner_id should be negative' in f"{e}":
             self.statusBar_showMessage.emit('Предложка есть только в сообществах',2000);
             self.vkspp_progressBar_setTextVisible.emit(False);
             print('\a',end='\r');
          else:
             raise

class PSThread(QtCore.QThread):
   vkps_progressBar_setRange = QtCore.pyqtSignal(int);
   vkps_progressBar_setValue = QtCore.pyqtSignal(int);
   statusBar_showMessage = QtCore.pyqtSignal(str,int);

   def __init__(self, app, resp, dir_path):
      super().__init__();
      self.app = app;
      self.resp = resp;
      self.dir_path = dir_path;

   @QtCore.pyqtSlot()
   def run(self):
      filelist = [];
      for item in self.resp:
         if 'attachments' in item:
            nums = len(item['attachments']);
            self.vkps_progressBar_setRange.emit(nums);
            for num, attachment in enumerate(item['attachments']):
               if attachment['type']=='link':
                  pass;
               elif attachment['type']=='doc':
                  filename = os.path.join(self.dir_path,f"{num+1}.{attachment['doc']['ext']}");
                  filelist.append(filename);
                  urlretrieve(attachment['doc']['url'],filename);
                  self.vkps_progressBar_setValue.emit(num+1);
               else:
                  filename = os.path.join(self.dir_path,f'{num+1}.jpg');
                  filelist.append(filename);
                  urlretrieve(vkAuth.get_max_photo(attachment['photo'])['url'],filename);
                  self.vkps_progressBar_setValue.emit(num+1);
      if filelist:
         self.statusBar_showMessage.emit('Оптимизация',0);
         optimiser = FileOptimizer(filelist);
         optimiser.optimise(silentMode=False, processes=1);
      self.app.vkps_downloadButton.setEnabled(True);
      self.statusBar_showMessage.emit('Готово!',2000);

class VKStuffApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self,app):
        # Инициализация приложения
        super().__init__()
        self.setupUi(self) 
        self.app = app
        self.thread = QtCore.QThread(parent=self);

        # Поиск в отложке
        self.vkspp_pushButton.clicked.connect(self.vkspp_search)
        self.vkspp_publicLineEdit.textChanged.connect(self.vkspp_enableButton)
        self.vkspp_respTableWidget.itemDoubleClicked.connect(self.vkspp_openLink)
        self.vkspp_suggests_radioButton.clicked.connect(self.vkspp_recheck_filter)
        self.vkspp_postponed_radioButton.clicked.connect(self.vkspp_recheck_filter)
        self.vkspp_htmlGenButton.clicked.connect(self.vkspp_htmlGen)

        # Редактор постов
        self.vked_getPostButton.clicked.connect(self.vked_get_post)
        self.vked_addAttachButton.clicked.connect(self.vked_addAttachment)
        self.vked_postButton.clicked.connect(self.vked_publishPost)
        self.vked_previewButton.clicked.connect(self.vked_previewW)

        # Сохранятель постов
        self.vkps_fileButton.clicked.connect(self.vkps_browse_folder)
        self.vkps_getPostButton.clicked.connect(self.vkps_get_post)
        self.vkps_downloadButton.clicked.connect(self.vkps_download)

        # Инфо
        self.info_1_auth_pushButton.clicked.connect(self.info_auth);
        self.logins = {};
        self.info_1_accountsBox.currentTextChanged.connect(self.info_change_login);

        # Авторизация
        try:
           with open('vk_config.v2.json', 'r') as f:
              js = json.load(f)
           self.logins = {l:'' for l in js};
        except (IOError, ValueError):
           js = {}
        try:
           with open('login') as f:
              login = f.read();
        except (FileNotFoundError, io.UnsupportedOperation):
           if self.logins:
              login = list(self.logins)[0];
           else:
              login = input('Введите логин: ');
           with open('login','w') as f:
              f.write(login);
        try:
           self.vk, self.token, self.myid, self.myname = vkAuth.vk_auth(login);
           resp = self.vk.method("users.get", {"user_ids":self.myid, "fields":"photo_100"})[0]
           self.logins[login] = {'vk': self.vk,
                                 'id': f"{self.myid}",
                                 'name': f"{resp['first_name']} {resp['last_name']}",
                                 'photo': resp['photo_100']};
        except vk_api.exceptions.AuthError:
           os.remove('login')
           input("Ошибка авторизации, проверьте правильность логина и пароля\nНажмите [Enter] для выхода")
           raise
        self.info_1_accountsBox.addItems(list(self.logins));

        self.info_1_id.setText(self.logins[login]['id']);
        self.info_1_name.setText(self.logins[login]['name']);
        scene = QtWidgets.QGraphicsScene()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.vk.http.get(self.logins[login]['photo']).content)
        scene.addPixmap(pixmap)
        self.info_ava.setScene(scene)

######### Функции поиска в отложке
#
    def vkspp_search(self):
       public_raw = self.vkspp_publicLineEdit.text()
       searched = self.vkspp_plainTextEdit.toPlainText().lower().strip()
       search_desc = self.vkspp_textdescCheckBox.isChecked()
       search_attach = self.vkspp_attachCheckBox.isChecked()

       if self.vkspp_suggests_radioButton.isChecked():
          search_filter = 'suggests';
       else: # if self.vkspp_postponed_radioButton.isChecked():
          search_filter = 'postponed';
 
       params = {'count':MAX_VKSPP_SEARCH_COUNT,
                 'offset':0,
                 'filter':search_filter,
                 'extended':0}
 
       if public_raw.isdigit():
          params['owner_id'] = public_raw
       else:
          params['domain'] = public_raw.rsplit('/',1)[-1].split('?',1)[0].split('#',1)[0]

       self.vkspp_respTableWidget.setRowCount(0)

       self.vkspp_respTableWidget.setEnabled(True);
       self.vkspp_respGroupBox.setEnabled(True);

       self.thread.quit();
       self.thread.wait();
       self.thread = QtCore.QThread(parent=self);
       self.sppThread = SPPThread(self,params,searched,search_desc,search_attach);
       self.sppThread.moveToThread(self.thread);

       self.sppThread.vkspp_progressBar_setRange.connect(self.vkspp_signal_progressBar_setRange);
       self.sppThread.vkspp_progressBar_setTextVisible.connect(self.vkspp_signal_progressBar_setTextVisible);
       self.sppThread.vkspp_progressBar_setValue.connect(self.vkspp_signal_progressBar_setValue);
       self.sppThread.vkspp_respTableWidget_insertRow.connect(self.vkspp_signal_respTableWidget_insertRow);
       self.sppThread.statusBar_showMessage.connect(self.vkspp_signal_statusBar_showMessage);
       self.sppThread.vkspp_respTableWidget_setEnabled.connect(self.vkspp_signal_vkspp_respTableWidget_setEnabled);
       self.sppThread.vkspp_respGroupBox_setEnabled.connect(self.vkspp_signal_vkspp_respGroupBox_setEnabled);

       self.thread.started.connect(self.sppThread.run);
       self.thread.finished.connect(self.thread.deleteLater);
       self.thread.finished.connect(self.sppThread.deleteLater);
       self.thread.start();
  ##### Сигналы
    @QtCore.pyqtSlot(int)
    def vkspp_signal_progressBar_setRange(self, count):
       self.vkspp_progressBar.setRange(0,count);

    @QtCore.pyqtSlot(bool)
    def vkspp_signal_progressBar_setTextVisible(self, flag):
       self.vkspp_progressBar.setTextVisible(flag);

    @QtCore.pyqtSlot(int)
    def vkspp_signal_progressBar_setValue(self, count):
       self.vkspp_progressBar.setValue(count);

    @QtCore.pyqtSlot(list)
    def vkspp_signal_respTableWidget_insertRow(self, posts_list):
       for post in posts_list:
          rowPosition = self.vkspp_respTableWidget.rowCount();
          self.vkspp_respTableWidget.insertRow(rowPosition);
          self.vkspp_respTableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(post['link']));
          self.vkspp_respTableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(post['date']));
          self.vkspp_respTableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(post['num_attach']));
          self.vkspp_respTableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(post['author']));
       self.vkspp_respTableWidget.resizeColumnsToContents();

       max_value_SpinBox = self.vkspp_respTableWidget.rowCount();
       if max_value_SpinBox > 0:
          self.vkspp_fromSpinBox.setMaximum(max_value_SpinBox);
          self.vkspp_toSpinBox.setMaximum(max_value_SpinBox);
          self.vkspp_htmlGenButton.setEnabled(True);
          self.vkspp_fromSpinBox.setEnabled(True);
          self.vkspp_toSpinBox.setEnabled(True);
       else:
          self.vkspp_htmlGenButton.setEnabled(False);
          self.vkspp_fromSpinBox.setEnabled(False);
          self.vkspp_toSpinBox.setEnabled(False);

    @QtCore.pyqtSlot(str,int)
    def vkspp_signal_statusBar_showMessage(self, message, timeout):
       self.statusBar.showMessage(message,timeout);

    @QtCore.pyqtSlot(bool)
    def vkspp_signal_vkspp_respTableWidget_setEnabled(self, flag):
       self.vkspp_respTableWidget.setEnabled(flag);
       self.vkspp_htmlGenButton.setEnabled(flag);
       self.vkspp_fromSpinBox.setEnabled(flag);
       self.vkspp_toSpinBox.setEnabled(flag);

    @QtCore.pyqtSlot(bool)
    def vkspp_signal_vkspp_respGroupBox_setEnabled(self, flag):
       self.vkspp_respGroupBox.setEnabled(flag);

    def vkspp_htmlGen(self):
       first_post_num = self.vkspp_fromSpinBox.value()
       last_post_num = self.vkspp_toSpinBox.value()
       first_post_num, last_post_num = sorted((first_post_num, last_post_num))
       def posts(first, last):
          for i in range(first-1, last):
             post_id = self.vkspp_respTableWidget.item(i,0).text().split('wall',1)[-1];
             yield post_id;
       post_id = ','.join(list(posts(first_post_num, last_post_num)))
       post_list = self.vk.method("wall.getById", {"posts":post_id})
       with open('posts.html','wt',encoding='utf-8') as html:
          html.write('<html>\n');
          html.write('<head><meta charset="utf-8"></head>\n');
          html.write('<body>\n');
          for post in post_list:
             post_url = f'wall{post["owner_id"]}_{post["id"]}'
             html.write(f'<a href="https://vk.com/{post_url}">{time.strftime("%d.%m.%Y %H:%M",time.localtime(post["date"]))}</a><br>\n')
             url_pattern = r"([^.\s]+\.{1}[^./\s]{2,6}(?:/[^\s]*)*)"
             text = re.sub(url_pattern,r'<a href=\1>\1</a>',post["text"])
             text = re.sub(r'(href=(?!http).*?)',r'\1http://',text)
             text = text.replace("\n","<br>\n");
             html.write(f'{text}<br>\n')
             if "attachments" in post:
                for attachment in post["attachments"]:
                   if "photo" in attachment:
                      link = f'https://vk.com/{post_url}?z=photo{attachment["photo"]["owner_id"]}_{attachment["photo"]["id"]}%2F{post_url}';
                      img = attachment["photo"]["sizes"][2]["url"];
                      html.write(f'<a href="{link}"><img src="{img}"></a>\n');
                   elif "doc" in attachment and attachment['doc']['ext']=='gif':
                      link = attachment['doc']['url'];
                      img = link;
                      html.write(f'<a href="{link}"><img src="{img}"></a>\n');
                   elif "link" in attachment:
                      link = attachment['link']['url'];
                      html.write(f'<a href="{link}">{link}</a>\n');
                   else:
                      link = f'https://vk.com/{attachment["type"]}{attachment[attachment["type"]]["owner_id"]}_{attachment[attachment["type"]]["id"]}_{attachment[attachment["type"]]["access_key"]}';
                      html.write(f'<a href="{link}">{link}</a>\n');
             html.write('<hr>\n\n');
          html.write('</body>\n</html>');
       self.statusBar.showMessage("Страница сгенерирована ",2000);
       
  ######
    def vkspp_enableButton(self):
       if self.vkspp_publicLineEdit.text():
          self.vkspp_pushButton.setEnabled(True);
       else:
          self.vkspp_pushButton.setEnabled(False);

    def vkspp_openLink(self,item):
       link = self.vkspp_respTableWidget.item(item.row(),0).text();
       copyClipboard(link);
       self.statusBar.showMessage('Скопировано!',2000)

    def vkspp_recheck_filter(self):
       if self.vkspp_postponed_radioButton.isChecked():
          self.vkspp_suggests_radioButton.setChecked(False);
       elif self.vkspp_suggests_radioButton.isChecked():
          self.vkspp_postponed_radioButton.setChecked(False);
#
#########

######### Функции редактора постов
#
    def vked_get_post(self):
      if ('vk.com' in self.vked_postLink.text() and 'wall' in self.vked_postLink.text()) or 'vk.com' not in self.vked_postLink.text():
         posts = self.vked_postLink.text().split('?')[0].split('wall')[-1]
         retry=True
         while retry:
            retry=False
            try:
               post = self.vk.method('wall.getById', {'posts': posts})
            except vk_api.exceptions.ApiHttpError as e:
               if "Response code 502" in f"{e}":
                  retry=True
                  time.sleep(3)
               else:
                  raise
         if post:
            post = post[0];
            post_id = post['id']
            owner_id = post['owner_id']
            publish_date = post['date']
            mark_as_ads = post['marked_as_ads']
            message = post['text']
            if 'attachments' in post:
               attachments = post['attachments']
            else:
               attachments = []
            if 'copyright' in post:
               copyright = post['copyright']
            else:
               copyright = False
            if 'signer_id' in post:
               signed = True;
            else:
               signed = False;
            if 'can_open' in post['comments'] and post['comments']['can_open']==1:
               close_comments = True;
            else:
               close_comments = False;
 
            name = ''
            if owner_id>0:
               name = f"{name}{self.vk.method('users.get', {'user_ids': owner_id})[0]['first_name']}" \
                       " " \
                      f"{self.vk.method('users.get', {'user_ids': owner_id})[0]['last_name']}"
            else:
               name+=self.vk.method('groups.getById', {'group_id': -owner_id})[0]['name']
 
            self.vked_owner_id.setText(f'{owner_id} {name}')
            self.vked_message.setText(message)
 
            self.vked_attachments.setRowCount(0)
            for attachment in attachments:
               rowPosition = self.vked_attachments.rowCount()
               self.vked_attachments.insertRow(rowPosition)
               self.vked_attachments.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(attachment['type']))
               if attachment['type']=='link':
                  self.vked_attachments.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(attachment['link']['url']))
               else:
                  self.vked_attachments.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(f"{attachment[attachment['type']]['owner_id']}_{attachment[attachment['type']]['id']}"))
            self.vked_attachments.resizeColumnsToContents()
 
            if signed:
               self.vked_signed_2.setChecked(True)
            else:
               self.vked_signed_2.setChecked(False)
 
            qdate = QtCore.QDateTime()
            qdate.setMSecsSinceEpoch(1000*publish_date)
            self.vked_publish_date.setDateTime(qdate)
 
            self.vked_post_id.setText(f"{post_id}")
 
            if mark_as_ads:
               self.vked_mark_as_ads.setChecked(True)
            else:
               self.vked_mark_as_ads.setChecked(False)
 
            if close_comments:
               self.vked_close_comments.setChecked(True)
            else:
               self.vked_close_comments.setChecked(False)
 
            if copyright:
               self.vked_copyright.setText(copyright['link'])
            else:
               self.vked_copyright.setText('')

         else:
            self.statusBar.showMessage('Пост не найден',2000)
            print('\a',end='\r')

      else:
         self.statusBar.showMessage('Неправильная ссылка на пост!',2000)
         print('\a',end='\r')

    def vked_addAttachment(self):
       rowPosition = self.vked_attachments.rowCount()
       self.vked_attachments.insertRow(rowPosition)

    def vked_publishPost(self):
       self.tab_vkeditor.setEnabled(False)
       owner_id = self.vked_owner_id.text().split(' ')[0]
       message = self.vked_message.toPlainText()

       attachments=''
       rowCount = self.vked_attachments.rowCount()
       for row in range(0,rowCount):
          if self.vked_attachments.item(row,0) and self.vked_attachments.item(row,0).text() and self.vked_attachments.item(row,1) and self.vked_attachments.item(row,1).text():
             if self.vked_attachments.item(row,0).text()=='link':
                attachments = f"{attachments}{self.vked_attachments.item(row,1).text().replace(',','')},"
             else:
                attachments = f"{attachments}{self.vked_attachments.item(row,0).text()}{self.vked_attachments.item(row,1).text()},"

       signed = int(self.vked_signed_2.isChecked())
       publish_date = int(time.mktime(time.strptime(self.vked_publish_date.text(),'%d.%m.%Y %H:%M')))
       post_id = self.vked_post_id.text()
       mark_as_ads = int(self.vked_mark_as_ads.isChecked())
       close_comments = int(self.vked_close_comments.isChecked())
       copyright = self.vked_copyright.text()
       try:
          self.vk.method('wall.edit', {'owner_id': owner_id,
                                       'from_group':1,
                                       'message': message,
                                       'attachments':attachments,
                                       'signed':signed,
                                       'publish_date':publish_date,
                                       'post_id':post_id,
                                       'mark_as_ads':mark_as_ads,
                                       'close_comments':close_comments,
                                       'copyright':copyright})
          self.tab_vkeditor.setEnabled(True)
          self.statusBar.showMessage('Опубликовано',2000)
       except vk_api.exceptions.Captcha as captcha:
          vkAuth.captcha_handler(captcha, show_captcha=True);
       except vk_api.exceptions.ApiError as e:
          print('\a')
          self.statusBar.showMessage(f'{e}',10000)
          self.tab_vkeditor.setEnabled(True)

    def vked_previewW(self):
       owner = self.vked_owner_id.text().split(' ',1)[-1]
       message = self.vked_message.toPlainText().replace('\n','<br>')+'<br>'

       attachments=[]
       rowCount = self.vked_attachments.rowCount()
       for row in range(0,rowCount):
          if self.vked_attachments.item(row,0).text() and self.vked_attachments.item(row,1).text():
             attachments.append([self.vked_attachments.item(row,0).text(),self.vked_attachments.item(row,1).text()])

       for attachment in attachments:
          if attachment[0]=='photo':
             url = self.vk.method('photos.getById', {'photos': attachment[1]})[0]['sizes'][-1]['url']
             message+='<img src="'+url+'" width="200px">'
          elif attachment[0]=='doc':
             url = self.vk.method('docs.getById', {'docs': attachment[1]})[0]['preview']['photo']['sizes'][-1]['url']
             message+='<br>doc: <img src="'+url+'" width="200px">'

       author = ''
       if self.vked_signed_2.isChecked():
          author_id = self.vk.method('wall.getById', {'posts': self.vked_postLink.text().split('?')[0].split('wall')[-1]})[0]['created_by']
          name = self.vk.method('users.get', {'user_ids': author_id})[0]
          author+=name['first_name']
          author+=' '
          author+=name['last_name']

       date = self.vked_publish_date.text()

       if self.vked_mark_as_ads.isChecked():
          ads = 'Рекламный пост'
       else:
          ads = ''

       if self.vked_close_comments.isChecked():
          comments = 'Доступ к комментированию закрыт'
       else:
          comments = 'Комментариев: 0'

       copyright = self.vked_copyright.text()

       self.vked_dialog = previewWindow(owner,date,message,author,ads,comments,copyright)
       self.vked_dialog.show()
#
#########

######### Функции сохранятеля постов
#
    def vkps_browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            self.vkps_fileEdit.setText(directory)

    def vkps_get_post(self):
        text = self.vkps_postLink.text()

    def vkps_download(self):
        try:
           dir_path = os.path.normpath(self.vkps_fileEdit.text());
           if not os.path.isdir(dir_path):
              os.makedirs(dir_path);
           url = self.vkps_postLink.text()
           self.vkps_downloadButton.setEnabled(False)
           post_id = url.split('?')[0].split('wall')[-1]
           resp = self.vk.method('wall.getById',{'posts': post_id})

           self.thread.quit();
           self.thread.wait();
           self.thread = QtCore.QThread(parent=self);
           self.psThread = PSThread(self, resp, dir_path);
           self.psThread.moveToThread(self.thread);

           self.psThread.vkps_progressBar_setRange.connect(self.vkps_signal_progressBar_setRange);
           self.psThread.vkps_progressBar_setValue.connect(self.vkps_signal_progressBar_setValue);
           self.psThread.statusBar_showMessage.connect(self.vkspp_signal_statusBar_showMessage);

           self.thread.started.connect(self.psThread.run);
           self.thread.finished.connect(self.thread.deleteLater);
           self.thread.finished.connect(self.psThread.deleteLater);
           self.thread.start();
        except:
           self.statusBar.showMessage('Не указана папка',2000)
           self.vkps_downloadButton.setEnabled(True)
           print('\a',end='\r')
  ###### Сигналы
    @QtCore.pyqtSlot(int)
    def vkps_signal_progressBar_setRange(self, count):
       self.vkps_progressBar.setRange(0,count);

    @QtCore.pyqtSlot(int)
    def vkps_signal_progressBar_setValue(self, count):
       self.vkps_progressBar.setValue(count);
  ######
#
#########

######### Функции страницы инфо
#
    def info_auth(self):
       login = self.info_1_auth_lineEdit.text();
       if not login:
          try:
             with open('login') as f:
                login = f.read();
          except (FileNotFoundError, io.UnsupportedOperation):
             if self.logins:
                login = list(self.logins)[0];
             else:
                login = input('Введите логин: ');
             with open('login','w') as f:
                f.write(login);
       if login not in self.logins:
          self.logins[login] = {};
          self.info_1_accountsBox.addItem(login);
          self.info_1_accountsBox.setCurrentIndex(self.info_1_accountsBox.count()-1);
       try:
          if self.logins[login]:
             self.vk = self.logins[login]['vk'];
             self.info_1_id.setText(self.logins[login]['id']);
             self.info_1_name.setText(self.logins[login]['name']);
          else:
             self.vk, self.token, self.myid, self.myname = vkAuth.vk_auth(login,captcha_handler=vkAuth.captcha_handler);
             resp = self.vk.method("users.get", {"user_ids":self.myid, "fields":"photo_100"})[0]
             self.logins[login] = {'vk': self.vk,
                                   'id': f"{self.myid}",
                                   'name': f"{resp['first_name']} {resp['last_name']}",
                                   'photo': resp['photo_100']};
             self.info_1_id.setText(f"{self.myid}");
             self.info_1_name.setText(f"{resp['first_name']} {resp['last_name']}");
          scene = QtWidgets.QGraphicsScene()
          pixmap = QtGui.QPixmap()
          pixmap.loadFromData(self.vk.http.get(self.logins[login]['photo']).content)
          scene.addPixmap(pixmap)
          self.info_ava.setScene(scene)
       except vk_api.exceptions.AuthError:
          self.statusBar.showMessage("Ошибка авторизации, проверьте правильность логина и пароля",10000)
          print('\a',end='\r')

    def info_change_login(self):
      login = self.info_1_accountsBox.currentText();
      self.info_1_auth_lineEdit.setText(login);
#
#########

class previewWindow(QtWidgets.QDialog, preview.Ui_Dialog):
   def __init__(self,owner,date,message,author,ads,comments,copyright):
      super().__init__()
      self.setupUi(self)
      self.owner.setText(owner)
      self.date.setText(date)
      with open("preview.html", "w", encoding='utf-8') as f:
         f.write('<html><head><meta charset="utf-8"></head><body>')
         f.write(message)
         f.write('</body></html>')
      self.author.setText(author)
      self.ads.setText(ads)
      self.comments.setText(comments)
      self.copyright.setText(copyright)
      self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = VKStuffApp(app)  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    window.thread.quit(); # Закрываем поток при закрытии окна
    window.thread.wait();

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()