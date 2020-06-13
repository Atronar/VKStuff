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
        MainWindow.resize(423, 494)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.publicLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.publicLineEdit.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.publicLineEdit.setObjectName("publicLineEdit")
        self.verticalLayout_2.addWidget(self.publicLineEdit)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.plainTextEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.plainTextEdit.setBaseSize(QtCore.QSize(0, 0))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.textdescCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.textdescCheckBox.setChecked(True)
        self.textdescCheckBox.setObjectName("textdescCheckBox")
        self.verticalLayout_2.addWidget(self.textdescCheckBox)
        self.attachCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.attachCheckBox.setChecked(True)
        self.attachCheckBox.setObjectName("attachCheckBox")
        self.verticalLayout_2.addWidget(self.attachCheckBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.respGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.respGroupBox.setEnabled(False)
        self.respGroupBox.setObjectName("respGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.respGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.respTableWidget = QtWidgets.QTableWidget(self.respGroupBox)
        self.respTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.respTableWidget.setEnabled(False)
        self.respTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.respTableWidget.setDragEnabled(True)
        self.respTableWidget.setColumnCount(3)
        self.respTableWidget.setObjectName("respTableWidget")
        self.respTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.respTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.respTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.respTableWidget.setHorizontalHeaderItem(2, item)
        self.respTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.respTableWidget)
        self.verticalLayout_2.addWidget(self.respGroupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VKSearchPostponed"))
        self.publicLineEdit.setPlaceholderText(_translate("MainWindow", "Ссылка на паблик"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Введите искомый текст"))
        self.textdescCheckBox.setText(_translate("MainWindow", "Искать в тексте поста"))
        self.attachCheckBox.setText(_translate("MainWindow", "Искать в описаниях вложений"))
        self.pushButton.setText(_translate("MainWindow", "Искать"))
        self.respGroupBox.setTitle(_translate("MainWindow", "Найденные посты"))
        item = self.respTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ссылка"))
        item = self.respTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Время"))
        item = self.respTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вложений"))

