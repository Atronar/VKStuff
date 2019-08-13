import vk_api;
import vkAuth;
from urllib.request import urlretrieve;
import sys
import design
from PyQt5 import QtWidgets, QtCore, QtNetwork
import os.path
import io;
import os;

class VKPostSaverApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.fileButton.clicked.connect(self.browse_folder)
        self.getPostButton.clicked.connect(self.get_post)
        self.downloadButton.clicked.connect(self.download)
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
        self.networkAccessManager = QtNetwork.QNetworkAccessManager()
        self._updateCookieJar(self.vk.http.cookies)

    def _updateCookieJar(self, cookiejar):     
       qnetworkcookie_list = []
   
       for cookie in cookiejar:
           tmp_cookiejar = QtNetwork.QNetworkCookie(QtCore.QByteArray(cookie.name.encode()), QtCore.QByteArray(cookie.value.encode()))
           qnetworkcookie_list.append(tmp_cookiejar)
       qcookiejar = QtNetwork.QNetworkCookieJar()
       qcookiejar.setCookiesFromUrl(qnetworkcookie_list, QtCore.QUrl('https://vk.com'))
       self.networkAccessManager.setCookieJar(qcookiejar)

    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            self.fileEdit.setText(directory)

    def get_post(self):
        text = self.postLink.text()
        self.postView.page().setNetworkAccessManager(self.networkAccessManager)
        self.postView.load(QtCore.QUrl(text))
        self.postView.show()

    def download(self):
        try:
           if not os.path.isdir(os.path.normpath(self.fileEdit.text())):
              os.makedirs(os.path.normpath(self.fileEdit.text()))
           url = self.postLink.text()
           self.downloadButton.setEnabled(False)
           post_id = url.split('?')[0].split('wall')[-1]
           resp = self.vk.method('wall.getById',{'posts': post_id})
           for item in resp:
              if 'attachments' in item:
                 nums = len(item['attachments'])
                 self.progressBar.setRange(0,nums)
                 for num, attachment in enumerate(item['attachments']):
                    urlretrieve(attachment['photo']['sizes'][-1]['url'],os.path.join(os.path.normpath(self.fileEdit.text()),str(num+1)+'.jpg'));
                    self.progressBar.setValue(num+1)
           self.downloadButton.setEnabled(True)
           self.statusBar.showMessage('Готово!')
        except:
           self.statusBar.showMessage('Не указана папка')
           print('\a',end='\r')

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = VKPostSaverApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()