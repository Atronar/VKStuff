import vk_api;
import vkAuth;
import sys
import design, preview
from PyQt5 import QtWidgets, QtCore, QtGui;
import io;
import os;
import time;
import webbrowser;
from urllib.request import urlretrieve;

def in_any_attach(searchedText,listAttachs):
   for attach in listAttachs:
      type_attach = attach['type'];
      if 'text' in attach[type_attach] and searchedText in attach[type_attach]['text'].lower():
         return True;
   return False;

class VKStuffApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Инициализация приложения
        super().__init__()
        self.setupUi(self) 

        # Поиск в отложке
        self.vkspp_pushButton.clicked.connect(self.vkspp_search)
        self.vkspp_publicLineEdit.textChanged.connect(self.vkspp_enableButton)
        self.vkspp_respTableWidget.itemDoubleClicked.connect(self.vkspp_openLink)

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
        self.info_1_auth_pushButton.clicked.connect(self.info_auth)

        # Авторизация
        try:
           with open('login') as f:
              login = f.read();
        except (FileNotFoundError, io.UnsupportedOperation):
           login = input('Введите логин: ');
           with open('login','w') as f:
              f.write(login);
        try:
           self.vk, self.token, self.myid, self.myname = vkAuth.vk_auth(login,captcha_handler=vkAuth.captcha_handler);
        except vk_api.exceptions.AuthError:
           os.remove('login')
           input("Ошибка авторизации, проверьте правильность логина и пароля\nНажмите [Enter] для выхода")
           raise
        resp = self.vk.method("users.get", {"user_ids":self.myid, "fields":"photo_100"})[0]
        self.info_1_id.setText(f"{self.myid}");
        self.info_1_name.setText(f"{resp['first_name']} {resp['last_name']}");
        resp['photo_100']
        scene = QtWidgets.QGraphicsScene()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.vk.http.get(resp['photo_100']).content)
        scene.addPixmap(pixmap)
        self.info_ava.setScene(scene)

######### Функции поиска в отложке
#
    def vkspp_search(self):
       public_raw = self.vkspp_publicLineEdit.text()
       searched = self.vkspp_plainTextEdit.toPlainText().lower().strip()
       search_desc = self.vkspp_textdescCheckBox.isChecked()
       search_attach = self.vkspp_attachCheckBox.isChecked()
 
       params = {'count':1000,
                 'filter':'postponed',
                 'extended':0}
 
       if public_raw.isdigit():
          params['owner_id'] = public_raw
       else:
          params['domain'] = public_raw.rsplit('/',1)[-1].split('?',1)[0].split('#',1)[0]

       #self.respListWidget.clear();
       self.vkspp_respTableWidget.setRowCount(0)
       try: 
          items = self.vk.method('wall.get', params)['items'];
          if items:
             self.vkspp_respGroupBox.setEnabled(True);
             #self.respListWidget.setEnabled(True);
             self.vkspp_respTableWidget.setEnabled(True);
             if search_desc and search_attach:
                items = [item for item in items if searched in item['text'].lower() or ('attachments' in item and in_any_attach(searched,item['attachments']))];
             elif search_desc:
                items = [item for item in items if searched in item['text'].lower()];
             elif search_attach:
                items = [item for item in items if 'attachments' in item and in_any_attach(searched,item['attachments'])];
             posts_list = [{'link':f"https://vk.com/wall{post['owner_id']}_{post['id']}",
                            'date':time.strftime("%d.%m.%Y %X",time.localtime(post['date'])),
                            'num_attach': f"{len(post['attachments'])}",
                            'author': f"{post['signer_id'] if 'signer_id' in post else 0}"
                           } for post in items]
             #self.respListWidget.addItems(posts_list);
             for column,post in enumerate(posts_list):
                rowPosition = self.vkspp_respTableWidget.rowCount()
                self.vkspp_respTableWidget.insertRow(rowPosition)
                self.vkspp_respTableWidget.setItem(column, 0, QtWidgets.QTableWidgetItem(post['link']))
                self.vkspp_respTableWidget.setItem(column, 1, QtWidgets.QTableWidgetItem(post['date']))
                self.vkspp_respTableWidget.setItem(column, 2, QtWidgets.QTableWidgetItem(post['num_attach']))
                self.vkspp_respTableWidget.setItem(column, 3, QtWidgets.QTableWidgetItem(post['author']))
             self.vkspp_respTableWidget.resizeColumnsToContents()
          else:
             self.vkspp_respGroupBox.setEnabled(False);
             #self.respListWidget.setEnabled(False);
             self.vkspp_respTableWidget.setEnabled(False);
       except vk_api.exceptions.ApiError as e:
          if 'Access denied' in f"{e}":
             self.statusbar.showMessage('Нет доступа к сообществу',10000)
             print('\a',end='\r')
          else:
             raise
 
    def vkspp_enableButton(self):
       if self.vkspp_publicLineEdit.text():
          self.vkspp_pushButton.setEnabled(True);
       else:
          self.vkspp_pushButton.setEnabled(False);

    def vkspp_openLink(self,item):
       link = self.vkspp_respTableWidget.item(item.row(),0).text()
       webbrowser.open(link);
#
#########

######### Функции редактора постов
#
    def vked_get_post(self):
        if ('vk.com' in self.vked_postLink.text() and 'wall' in self.vked_postLink.text()) or 'vk.com' not in self.vked_postLink.text():
           posts = self.vked_postLink.text().split('?')[0].split('wall')[-1]
           post = self.vk.method('wall.getById', {'posts': posts})[0]
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
           for column,attachment in enumerate(attachments):
              rowPosition = self.vked_attachments.rowCount()
              self.vked_attachments.insertRow(rowPosition)
              self.vked_attachments.setItem(column, 0, QtWidgets.QTableWidgetItem(attachment['type']))
              self.vked_attachments.setItem(column, 1, QtWidgets.QTableWidgetItem(f"{attachment[attachment['type']]['owner_id']}_{attachment[attachment['type']]['id']}"))

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
           self.vked_statusBar.showMessage('Неправильная ссылка на пост!',2000)
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
             attachments = f"{attachments}{self.vked_attachments.item(row,0).text()}{self.vked_attachments.item(row,1).text()},"

       signed = int(self.vked_signed_2.isChecked())
       publish_date = int(time.mktime(time.strptime(self.vked_publish_date.text(),'%d.%m.%Y %H:%M')))
       post_id = self.vked_post_id.text()
       mark_as_ads = int(self.vked_mark_as_ads.isChecked())
       close_comments = int(self.vked_close_comments.isChecked())
       copyright = self.vked_copyright.text()
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
           if not os.path.isdir(os.path.normpath(self.vkps_fileEdit.text())):
              os.makedirs(os.path.normpath(self.vkps_fileEdit.text()))
           url = self.vkps_postLink.text()
           self.vkps_downloadButton.setEnabled(False)
           post_id = url.split('?')[0].split('wall')[-1]
           resp = self.vk.method('wall.getById',{'posts': post_id})
           for item in resp:
              if 'attachments' in item:
                 nums = len(item['attachments'])
                 self.vkps_progressBar.setRange(0,nums)
                 for num, attachment in enumerate(item['attachments']):
                    if attachment['type']=='link':
                       pass;
                    else:
                       urlretrieve(attachment['photo']['sizes'][-1]['url'],os.path.join(os.path.normpath(self.vkps_fileEdit.text()),f'{num+1}.jpg'));
                       self.vkps_progressBar.setValue(num+1)
           self.vkps_downloadButton.setEnabled(True)
           self.statusBar.showMessage('Готово!',2000)
        except:
           self.statusBar.showMessage('Не указана папка',2000)
           self.vkps_downloadButton.setEnabled(True)
           print('\a',end='\r')
#
#########

######### Функции страницы инфо
#
    def info_auth(self):
       login = self.info_1_auth_lineEdit.text();

       try:
          self.vk, self.token, self.myid, self.myname = vkAuth.vk_auth(login,captcha_handler=vkAuth.captcha_handler);
          resp = self.vk.method("users.get", {"user_ids":self.myid, "fields":"photo_100"})[0]
          self.info_1_id.setText(f"{self.myid}");
          self.info_1_name.setText(f"{resp['first_name']} {resp['last_name']}");
          resp['photo_100']
          scene = QtWidgets.QGraphicsScene()
          pixmap = QtGui.QPixmap()
          pixmap.loadFromData(self.vk.http.get(resp['photo_100']).content)
          scene.addPixmap(pixmap)
          self.info_ava.setScene(scene)
       except vk_api.exceptions.AuthError:
          self.statusBar.showMessage("Ошибка авторизации, проверьте правильность логина и пароля",2000)
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
    window = VKStuffApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()