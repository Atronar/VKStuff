# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.postBox = QtWidgets.QGroupBox(self.centralwidget)
        self.postBox.setEnabled(True)
        self.postBox.setAlignment(QtCore.Qt.AlignCenter)
        self.postBox.setObjectName("postBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.postBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.postLink = QtWidgets.QLineEdit(self.postBox)
        self.postLink.setObjectName("postLink")
        self.horizontalLayout.addWidget(self.postLink)
        self.getPostButton = QtWidgets.QPushButton(self.postBox)
        self.getPostButton.setObjectName("getPostButton")
        self.horizontalLayout.addWidget(self.getPostButton)
        self.verticalLayout.addWidget(self.postBox)
        self.postView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.postView.setUrl(QtCore.QUrl("about:blank"))
        self.postView.setObjectName("postView")
        self.verticalLayout.addWidget(self.postView)
        self.fileBox = QtWidgets.QGroupBox(self.centralwidget)
        self.fileBox.setAlignment(QtCore.Qt.AlignCenter)
        self.fileBox.setObjectName("fileBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fileBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileEdit = QtWidgets.QLineEdit(self.fileBox)
        self.fileEdit.setObjectName("fileEdit")
        self.horizontalLayout_2.addWidget(self.fileEdit)
        self.fileButton = QtWidgets.QToolButton(self.fileBox)
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_2.addWidget(self.fileButton)
        self.verticalLayout.addWidget(self.fileBox)
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setObjectName("downloadButton")
        self.verticalLayout.addWidget(self.downloadButton)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.postView.raise_()
        self.fileBox.raise_()
        self.postBox.raise_()
        self.downloadButton.raise_()
        self.progressBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сохранятель постов ВКонтакте"))
        self.postBox.setTitle(_translate("MainWindow", "Ссылка на пост"))
        self.getPostButton.setText(_translate("MainWindow", "Применить"))
        self.fileBox.setTitle(_translate("MainWindow", "Папка"))
        self.fileButton.setText(_translate("MainWindow", "Выберите папку"))
        self.downloadButton.setText(_translate("MainWindow", "Скачать"))

from PyQt5 import QtWebKitWidgets
