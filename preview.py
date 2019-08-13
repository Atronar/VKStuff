# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.owner = QtWidgets.QLabel(Dialog)
        self.owner.setObjectName("owner")
        self.verticalLayout.addWidget(self.owner)
        self.date = QtWidgets.QLabel(Dialog)
        self.date.setObjectName("date")
        self.verticalLayout.addWidget(self.date)
        self.message = QtWebKitWidgets.QWebView(Dialog)
        self.message.setUrl(QtCore.QUrl("file:///C:/Users/Цифровой портал/SkyDrive/ProgsPy/VKPostEditor/preview.html"))
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.author = QtWidgets.QLabel(Dialog)
        self.author.setText("")
        self.author.setObjectName("author")
        self.verticalLayout.addWidget(self.author)
        self.ads = QtWidgets.QLabel(Dialog)
        self.ads.setText("")
        self.ads.setObjectName("ads")
        self.verticalLayout.addWidget(self.ads)
        self.comments = QtWidgets.QLabel(Dialog)
        self.comments.setText("")
        self.comments.setObjectName("comments")
        self.verticalLayout.addWidget(self.comments)
        self.copyright = QtWidgets.QLabel(Dialog)
        self.copyright.setText("")
        self.copyright.setObjectName("copyright")
        self.verticalLayout.addWidget(self.copyright)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Предпросмотр"))
        self.owner.setText(_translate("Dialog", "Owner"))
        self.date.setText(_translate("Dialog", "Date"))

from PyQt5 import QtWebKitWidgets
