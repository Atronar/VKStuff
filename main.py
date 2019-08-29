import vk_api;
import vkAuth;
import sys
import design
from PyQt5 import QtWidgets;
import io;
import os;
import time;
import webbrowser;

def in_any_attach(searchedText,listAttachs):
   for attach in listAttachs:
      type_attach = attach['type'];
      if 'text' in attach[type_attach] and searchedText in attach[type_attach]['text']:
         return True;
   return False;

class VKSearchPostponedApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

        self.pushButton.clicked.connect(self.search)
        self.publicLineEdit.textChanged.connect(self.enableButton)
        self.respTableWidget.itemDoubleClicked.connect(self.openLink)

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

    def search(self):
       public_raw = self.publicLineEdit.text()
       searched = self.plainTextEdit.toPlainText()
       search_desc = self.textdescCheckBox.isChecked()
       search_attach = self.attachCheckBox.isChecked()
 
       params = {'count':1000,
                 'filter':'postponed',
                 'extended':0}
 
       if public_raw.isdigit():
          params['owner_id'] = public_raw
       else:
          params['domain'] = public_raw.rsplit('/',1)[-1].split('?',1)[0].split('#',1)[0]

       #self.respListWidget.clear();
       self.respTableWidget.setRowCount(0)
       try: 
          items = self.vk.method('wall.get', params)['items'];
          if items:
             self.respGroupBox.setEnabled(True);
             #self.respListWidget.setEnabled(True);
             self.respTableWidget.setEnabled(True);
             if search_desc and search_attach:
                items = [item for item in items if searched in item['text'] or in_any_attach(searched,item['attachments'])];
             elif search_desc:
                items = [item for item in items if searched in item['text']];
             elif search_attach:
                items = [item for item in items if in_any_attach(searched,item['attachments'])];
             posts_list = [{'link':'https://vk.com/wall'+str(post['owner_id'])+'_'+str(post['id']), 'date':time.strftime("%d.%m.%Y %X",time.localtime(post['date']))} for post in items]
             #self.respListWidget.addItems(posts_list);
             for column,post in enumerate(posts_list):
                rowPosition = self.respTableWidget.rowCount()
                self.respTableWidget.insertRow(rowPosition)
                self.respTableWidget.setItem(column, 0, QtWidgets.QTableWidgetItem(post['link']))
                self.respTableWidget.setItem(column, 1, QtWidgets.QTableWidgetItem(post['date']))
          else:
             self.respGroupBox.setEnabled(False);
             #self.respListWidget.setEnabled(False);
             self.respTableWidget.setEnabled(False);
       except vk_api.exceptions.ApiError as e:
          if 'Access denied' in str(e):
             self.statusbar.showMessage('Нет доступа к сообществу',10000)
             print('\a',end='\r')
          else:
             raise
 
    def enableButton(self):
       if self.publicLineEdit.text():
          self.pushButton.setEnabled(True);
       else:
          self.pushButton.setEnabled(False);

    def openLink(self,item):
       link = self.respTableWidget.item(item.row(),0).text()
       webbrowser.open(link);

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = VKSearchPostponedApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()