import vkAuth;
import sys
import design, preview
from PyQt5 import QtWidgets, QtCore
import time;
import io;
import os;

class VKPostEditorApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.getPostButton.clicked.connect(self.get_post)
        self.addAttachButton.clicked.connect(self.addAttachment)
        self.postButton.clicked.connect(self.publishPost)
        self.previewButton.clicked.connect(self.previewW)
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

    def get_post(self):
        if ('vk.com' in self.postLink.text() and 'wall' in self.postLink.text()) or 'vk.com' not in self.postLink.text():
           posts = self.postLink.text().split('?')[0].split('wall')[-1]
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
              name+=self.vk.method('users.get', {'user_ids': owner_id})[0]['first_name']
              name+=' '
              name+=self.vk.method('users.get', {'user_ids': owner_id})[0]['last_name']
           else:
              name+=self.vk.method('groups.getById', {'group_id': -owner_id})[0]['name']

           self.owner_id.setText(str(owner_id)+' '+name)
           self.message.setText(message)

           self.attachments.setRowCount(0)
           for column,attachment in enumerate(attachments):
              rowPosition = self.attachments.rowCount()
              self.attachments.insertRow(rowPosition)
              self.attachments.setItem(column, 0, QtWidgets.QTableWidgetItem(attachment['type']))
              self.attachments.setItem(column, 1, QtWidgets.QTableWidgetItem(str(attachment[attachment['type']]['owner_id'])+'_'+str(attachment[attachment['type']]['id'])))

           if signed:
              self.signed_2.setChecked(True)
           else:
              self.signed_2.setChecked(False)

           qdate = QtCore.QDateTime()
           qdate.setMSecsSinceEpoch(1000*publish_date)
           self.publish_date.setDateTime(qdate)

           self.post_id.setText(str(post_id))

           if mark_as_ads:
              self.mark_as_ads.setChecked(True)
           else:
              self.mark_as_ads.setChecked(False)

           if close_comments:
              self.close_comments.setChecked(True)
           else:
              self.close_comments.setChecked(False)

           if copyright:
              self.copyright.setText(copyright['link'])
           else:
              self.copyright.setText('')

        else:
           self.statusBar.showMessage('Неправильная ссылка на пост!')
           print('\a',end='\r')

    def addAttachment(self):
       rowPosition = self.attachments.rowCount()
       self.attachments.insertRow(rowPosition)

    def publishPost(self):
       self.centralwidget.setEnabled(False)
       owner_id = self.owner_id.text().split(' ')[0]
       message = self.message.toPlainText()

       attachments=''
       rowCount = self.attachments.rowCount()
       for row in range(0,rowCount):
          if self.attachments.item(row,0).text() and self.attachments.item(row,1).text():
             attachments+=self.attachments.item(row,0).text()+self.attachments.item(row,1).text()+','

       signed = int(self.signed_2.isChecked())
       publish_date = int(time.mktime(time.strptime(self.publish_date.text(),'%d.%m.%Y %H:%M')))
       post_id = self.post_id.text()
       mark_as_ads = int(self.mark_as_ads.isChecked())
       close_comments = int(self.close_comments.isChecked())
       copyright = self.copyright.text()
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
       self.centralwidget.setEnabled(True)
       self.statusBar.showMessage('Опубликовано',2000)

    def previewW(self):
       owner = self.owner_id.text().split(' ',1)[-1]
       message = self.message.toPlainText().replace('\n','<br>')+'<br>'

       attachments=[]
       rowCount = self.attachments.rowCount()
       for row in range(0,rowCount):
          if self.attachments.item(row,0).text() and self.attachments.item(row,1).text():
             attachments.append([self.attachments.item(row,0).text(),self.attachments.item(row,1).text()])

       for attachment in attachments:
          if attachment[0]=='photo':
             url = self.vk.method('photos.getById', {'photos': attachment[1]})[0]['sizes'][-1]['url']
             message+='<img src="'+url+'" width="200px">'
          elif attachment[0]=='doc':
             url = self.vk.method('docs.getById', {'docs': attachment[1]})[0]['preview']['photo']['sizes'][-1]['url']
             message+='<br>doc: <img src="'+url+'" width="200px">'

       author = ''
       if self.signed_2.isChecked():
          author_id = self.vk.method('wall.getById', {'posts': self.postLink.text().split('?')[0].split('wall')[-1]})[0]['created_by']
          name = self.vk.method('users.get', {'user_ids': author_id})[0]
          author+=name['first_name']
          author+=' '
          author+=name['last_name']

       date = self.publish_date.text()

       if self.mark_as_ads.isChecked():
          ads = 'Рекламный пост'
       else:
          ads = ''

       if self.close_comments.isChecked():
          comments = 'Доступ к комментированию закрыт'
       else:
          comments = 'Комментариев: 0'

       copyright = self.copyright.text()

       self.dialog = previewWindow(owner,date,message,author,ads,comments,copyright)
       self.dialog.show()

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
    window = VKPostEditorApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()