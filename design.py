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
        MainWindow.resize(450, 572)
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
        self.postParametersBox = QtWidgets.QGroupBox(self.centralwidget)
        self.postParametersBox.setAlignment(QtCore.Qt.AlignCenter)
        self.postParametersBox.setObjectName("postParametersBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.postParametersBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.owner_idLayout = QtWidgets.QHBoxLayout()
        self.owner_idLayout.setObjectName("owner_idLayout")
        self.owner_idLabel = QtWidgets.QLabel(self.postParametersBox)
        self.owner_idLabel.setObjectName("owner_idLabel")
        self.owner_idLayout.addWidget(self.owner_idLabel)
        self.owner_id = QtWidgets.QLabel(self.postParametersBox)
        self.owner_id.setObjectName("owner_id")
        self.owner_idLayout.addWidget(self.owner_id)
        self.verticalLayout_2.addLayout(self.owner_idLayout)
        self.messageLayout = QtWidgets.QHBoxLayout()
        self.messageLayout.setObjectName("messageLayout")
        self.messageLabel = QtWidgets.QLabel(self.postParametersBox)
        self.messageLabel.setObjectName("messageLabel")
        self.messageLayout.addWidget(self.messageLabel)
        self.message = QtWidgets.QTextEdit(self.postParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setMinimumSize(QtCore.QSize(0, 0))
        self.message.setAcceptDrops(True)
        self.message.setObjectName("message")
        self.messageLayout.addWidget(self.message)
        self.verticalLayout_2.addLayout(self.messageLayout)
        self.attachmentsLayout = QtWidgets.QHBoxLayout()
        self.attachmentsLayout.setObjectName("attachmentsLayout")
        self.attachmenntsLabel = QtWidgets.QLabel(self.postParametersBox)
        self.attachmenntsLabel.setObjectName("attachmenntsLabel")
        self.attachmentsLayout.addWidget(self.attachmenntsLabel)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.attachments = QtWidgets.QTableWidget(self.postParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attachments.sizePolicy().hasHeightForWidth())
        self.attachments.setSizePolicy(sizePolicy)
        self.attachments.setDragEnabled(True)
        self.attachments.setDragDropOverwriteMode(False)
        self.attachments.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.attachments.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.attachments.setAlternatingRowColors(False)
        self.attachments.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.attachments.setRowCount(0)
        self.attachments.setColumnCount(2)
        self.attachments.setObjectName("attachments")
        item = QtWidgets.QTableWidgetItem()
        self.attachments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.attachments.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.attachments)
        self.addAttachButton = QtWidgets.QPushButton(self.postParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addAttachButton.sizePolicy().hasHeightForWidth())
        self.addAttachButton.setSizePolicy(sizePolicy)
        self.addAttachButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.addAttachButton.setObjectName("addAttachButton")
        self.verticalLayout_3.addWidget(self.addAttachButton)
        self.attachmentsLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.attachmentsLayout)
        self.signed_2 = QtWidgets.QCheckBox(self.postParametersBox)
        self.signed_2.setObjectName("signed_2")
        self.verticalLayout_2.addWidget(self.signed_2)
        self.publish_dateLayout = QtWidgets.QHBoxLayout()
        self.publish_dateLayout.setObjectName("publish_dateLayout")
        self.publish_dateLabel = QtWidgets.QLabel(self.postParametersBox)
        self.publish_dateLabel.setObjectName("publish_dateLabel")
        self.publish_dateLayout.addWidget(self.publish_dateLabel)
        self.publish_date = QtWidgets.QDateTimeEdit(self.postParametersBox)
        self.publish_date.setObjectName("publish_date")
        self.publish_dateLayout.addWidget(self.publish_date)
        self.verticalLayout_2.addLayout(self.publish_dateLayout)
        self.post_idLayout = QtWidgets.QHBoxLayout()
        self.post_idLayout.setObjectName("post_idLayout")
        self.post_idLabel = QtWidgets.QLabel(self.postParametersBox)
        self.post_idLabel.setObjectName("post_idLabel")
        self.post_idLayout.addWidget(self.post_idLabel)
        self.post_id = QtWidgets.QLabel(self.postParametersBox)
        self.post_id.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.post_id.setObjectName("post_id")
        self.post_idLayout.addWidget(self.post_id)
        self.verticalLayout_2.addLayout(self.post_idLayout)
        self.mark_as_ads = QtWidgets.QCheckBox(self.postParametersBox)
        self.mark_as_ads.setObjectName("mark_as_ads")
        self.verticalLayout_2.addWidget(self.mark_as_ads)
        self.close_comments = QtWidgets.QCheckBox(self.postParametersBox)
        self.close_comments.setObjectName("close_comments")
        self.verticalLayout_2.addWidget(self.close_comments)
        self.copyrightLayout = QtWidgets.QHBoxLayout()
        self.copyrightLayout.setObjectName("copyrightLayout")
        self.copyrightLabel = QtWidgets.QLabel(self.postParametersBox)
        self.copyrightLabel.setObjectName("copyrightLabel")
        self.copyrightLayout.addWidget(self.copyrightLabel)
        self.copyright = QtWidgets.QLineEdit(self.postParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyright.sizePolicy().hasHeightForWidth())
        self.copyright.setSizePolicy(sizePolicy)
        self.copyright.setObjectName("copyright")
        self.copyrightLayout.addWidget(self.copyright)
        self.verticalLayout_2.addLayout(self.copyrightLayout)
        self.verticalLayout.addWidget(self.postParametersBox)
        self.previewButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewButton.sizePolicy().hasHeightForWidth())
        self.previewButton.setSizePolicy(sizePolicy)
        self.previewButton.setMinimumSize(QtCore.QSize(0, 0))
        self.previewButton.setObjectName("previewButton")
        self.verticalLayout.addWidget(self.previewButton)
        self.postButton = QtWidgets.QPushButton(self.centralwidget)
        self.postButton.setObjectName("postButton")
        self.verticalLayout.addWidget(self.postButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактор постов ВКонтакте"))
        self.postBox.setTitle(_translate("MainWindow", "Ссылка на пост"))
        self.getPostButton.setText(_translate("MainWindow", "Применить"))
        self.postParametersBox.setTitle(_translate("MainWindow", "Параметры поста"))
        self.owner_idLabel.setToolTip(_translate("MainWindow", "owner_id"))
        self.owner_idLabel.setText(_translate("MainWindow", "ИД владельца"))
        self.owner_id.setText(_translate("MainWindow", "owner_id"))
        self.messageLabel.setToolTip(_translate("MainWindow", "message"))
        self.messageLabel.setText(_translate("MainWindow", "Сообщение"))
        self.attachmenntsLabel.setToolTip(_translate("MainWindow", "attachments"))
        self.attachmenntsLabel.setText(_translate("MainWindow", "Вложения"))
        item = self.attachments.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "type"))
        item = self.attachments.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "attachment"))
        self.addAttachButton.setText(_translate("MainWindow", "Добавить вложение"))
        self.signed_2.setToolTip(_translate("MainWindow", "signed"))
        self.signed_2.setText(_translate("MainWindow", "Подпись от автора"))
        self.publish_dateLabel.setToolTip(_translate("MainWindow", "publish_date"))
        self.publish_dateLabel.setText(_translate("MainWindow", "Дата публикации"))
        self.post_idLabel.setToolTip(_translate("MainWindow", "post_id"))
        self.post_idLabel.setText(_translate("MainWindow", "ИД поста"))
        self.post_id.setText(_translate("MainWindow", "post_id"))
        self.mark_as_ads.setToolTip(_translate("MainWindow", "mark_as_ads"))
        self.mark_as_ads.setText(_translate("MainWindow", "Это реклама"))
        self.close_comments.setToolTip(_translate("MainWindow", "close_comments"))
        self.close_comments.setText(_translate("MainWindow", "Закрыть комментарии"))
        self.copyrightLabel.setToolTip(_translate("MainWindow", "copyright"))
        self.copyrightLabel.setText(_translate("MainWindow", "Источник"))
        self.previewButton.setText(_translate("MainWindow", "Предпросмотр"))
        self.postButton.setText(_translate("MainWindow", "Опубликовать"))

