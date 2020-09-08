# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 764)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_vkeditor = QtWidgets.QWidget()
        self.tab_vkeditor.setObjectName("tab_vkeditor")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_vkeditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vked_postBox = QtWidgets.QGroupBox(self.tab_vkeditor)
        self.vked_postBox.setEnabled(True)
        self.vked_postBox.setAlignment(QtCore.Qt.AlignCenter)
        self.vked_postBox.setObjectName("vked_postBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.vked_postBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vked_postLink = QtWidgets.QLineEdit(self.vked_postBox)
        self.vked_postLink.setObjectName("vked_postLink")
        self.horizontalLayout.addWidget(self.vked_postLink)
        self.vked_getPostButton = QtWidgets.QPushButton(self.vked_postBox)
        self.vked_getPostButton.setObjectName("vked_getPostButton")
        self.horizontalLayout.addWidget(self.vked_getPostButton)
        self.verticalLayout.addWidget(self.vked_postBox)
        self.vked_postParametersBox = QtWidgets.QGroupBox(self.tab_vkeditor)
        self.vked_postParametersBox.setAlignment(QtCore.Qt.AlignCenter)
        self.vked_postParametersBox.setObjectName("vked_postParametersBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.vked_postParametersBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.vked_owner_idLabel = QtWidgets.QLabel(self.vked_postParametersBox)
        self.vked_owner_idLabel.setObjectName("vked_owner_idLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vked_owner_idLabel)
        self.vked_owner_id = QtWidgets.QLabel(self.vked_postParametersBox)
        self.vked_owner_id.setObjectName("vked_owner_id")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.vked_owner_id)
        self.vked_messageLabel = QtWidgets.QLabel(self.vked_postParametersBox)
        self.vked_messageLabel.setObjectName("vked_messageLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.vked_messageLabel)
        self.vked_message = QtWidgets.QTextEdit(self.vked_postParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vked_message.sizePolicy().hasHeightForWidth())
        self.vked_message.setSizePolicy(sizePolicy)
        self.vked_message.setMinimumSize(QtCore.QSize(0, 0))
        self.vked_message.setAcceptDrops(True)
        self.vked_message.setAcceptRichText(False)
        self.vked_message.setObjectName("vked_message")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.vked_message)
        self.vked_attachmenntsLabel = QtWidgets.QLabel(self.vked_postParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vked_attachmenntsLabel.sizePolicy().hasHeightForWidth())
        self.vked_attachmenntsLabel.setSizePolicy(sizePolicy)
        self.vked_attachmenntsLabel.setObjectName("vked_attachmenntsLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.vked_attachmenntsLabel)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vked_attachments = QtWidgets.QTableWidget(self.vked_postParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vked_attachments.sizePolicy().hasHeightForWidth())
        self.vked_attachments.setSizePolicy(sizePolicy)
        self.vked_attachments.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.vked_attachments.setDragEnabled(True)
        self.vked_attachments.setDragDropOverwriteMode(False)
        self.vked_attachments.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.vked_attachments.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.vked_attachments.setAlternatingRowColors(False)
        self.vked_attachments.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.vked_attachments.setRowCount(0)
        self.vked_attachments.setColumnCount(2)
        self.vked_attachments.setObjectName("vked_attachments")
        item = QtWidgets.QTableWidgetItem()
        self.vked_attachments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vked_attachments.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.vked_attachments)
        self.vked_addAttachButton = QtWidgets.QPushButton(self.vked_postParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vked_addAttachButton.sizePolicy().hasHeightForWidth())
        self.vked_addAttachButton.setSizePolicy(sizePolicy)
        self.vked_addAttachButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.vked_addAttachButton.setObjectName("vked_addAttachButton")
        self.verticalLayout_3.addWidget(self.vked_addAttachButton)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_3)
        self.vked_signed_2 = QtWidgets.QCheckBox(self.vked_postParametersBox)
        self.vked_signed_2.setObjectName("vked_signed_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.vked_signed_2)
        self.vked_publish_dateLabel = QtWidgets.QLabel(self.vked_postParametersBox)
        self.vked_publish_dateLabel.setObjectName("vked_publish_dateLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.vked_publish_dateLabel)
        self.vked_publish_date = QtWidgets.QDateTimeEdit(self.vked_postParametersBox)
        self.vked_publish_date.setObjectName("vked_publish_date")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.vked_publish_date)
        self.vked_post_idLabel = QtWidgets.QLabel(self.vked_postParametersBox)
        self.vked_post_idLabel.setObjectName("vked_post_idLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.vked_post_idLabel)
        self.vked_post_id = QtWidgets.QLabel(self.vked_postParametersBox)
        self.vked_post_id.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.vked_post_id.setObjectName("vked_post_id")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.vked_post_id)
        self.vked_mark_as_ads = QtWidgets.QCheckBox(self.vked_postParametersBox)
        self.vked_mark_as_ads.setObjectName("vked_mark_as_ads")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.vked_mark_as_ads)
        self.vked_close_comments = QtWidgets.QCheckBox(self.vked_postParametersBox)
        self.vked_close_comments.setObjectName("vked_close_comments")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.vked_close_comments)
        self.vked_copyrightLabel = QtWidgets.QLabel(self.vked_postParametersBox)
        self.vked_copyrightLabel.setObjectName("vked_copyrightLabel")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.vked_copyrightLabel)
        self.vked_copyright = QtWidgets.QLineEdit(self.vked_postParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vked_copyright.sizePolicy().hasHeightForWidth())
        self.vked_copyright.setSizePolicy(sizePolicy)
        self.vked_copyright.setObjectName("vked_copyright")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.vked_copyright)
        self.verticalLayout.addWidget(self.vked_postParametersBox)
        self.vked_previewButton = QtWidgets.QPushButton(self.tab_vkeditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vked_previewButton.sizePolicy().hasHeightForWidth())
        self.vked_previewButton.setSizePolicy(sizePolicy)
        self.vked_previewButton.setMinimumSize(QtCore.QSize(0, 0))
        self.vked_previewButton.setObjectName("vked_previewButton")
        self.verticalLayout.addWidget(self.vked_previewButton)
        self.vked_postButton = QtWidgets.QPushButton(self.tab_vkeditor)
        self.vked_postButton.setObjectName("vked_postButton")
        self.verticalLayout.addWidget(self.vked_postButton)
        self.tabWidget.addTab(self.tab_vkeditor, "")
        self.tab_vksearchpostponed = QtWidgets.QWidget()
        self.tab_vksearchpostponed.setObjectName("tab_vksearchpostponed")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_vksearchpostponed)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vkspp_publicLineEdit = QtWidgets.QLineEdit(self.tab_vksearchpostponed)
        self.vkspp_publicLineEdit.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.vkspp_publicLineEdit.setObjectName("vkspp_publicLineEdit")
        self.verticalLayout_5.addWidget(self.vkspp_publicLineEdit)
        self.vkspp_plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_vksearchpostponed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vkspp_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.vkspp_plainTextEdit.setSizePolicy(sizePolicy)
        self.vkspp_plainTextEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.vkspp_plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.vkspp_plainTextEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.vkspp_plainTextEdit.setBaseSize(QtCore.QSize(0, 0))
        self.vkspp_plainTextEdit.setObjectName("vkspp_plainTextEdit")
        self.verticalLayout_5.addWidget(self.vkspp_plainTextEdit)
        self.vkspp_textdescCheckBox = QtWidgets.QCheckBox(self.tab_vksearchpostponed)
        self.vkspp_textdescCheckBox.setChecked(True)
        self.vkspp_textdescCheckBox.setObjectName("vkspp_textdescCheckBox")
        self.verticalLayout_5.addWidget(self.vkspp_textdescCheckBox)
        self.vkspp_attachCheckBox = QtWidgets.QCheckBox(self.tab_vksearchpostponed)
        self.vkspp_attachCheckBox.setChecked(True)
        self.vkspp_attachCheckBox.setObjectName("vkspp_attachCheckBox")
        self.verticalLayout_5.addWidget(self.vkspp_attachCheckBox)
        self.vkspp_postponed_radioButton = QtWidgets.QRadioButton(self.tab_vksearchpostponed)
        self.vkspp_postponed_radioButton.setChecked(True)
        self.vkspp_postponed_radioButton.setObjectName("vkspp_postponed_radioButton")
        self.verticalLayout_5.addWidget(self.vkspp_postponed_radioButton)
        self.vkspp_suggests_radioButton = QtWidgets.QRadioButton(self.tab_vksearchpostponed)
        self.vkspp_suggests_radioButton.setObjectName("vkspp_suggests_radioButton")
        self.verticalLayout_5.addWidget(self.vkspp_suggests_radioButton)
        self.vkspp_pushButton = QtWidgets.QPushButton(self.tab_vksearchpostponed)
        self.vkspp_pushButton.setEnabled(False)
        self.vkspp_pushButton.setObjectName("vkspp_pushButton")
        self.verticalLayout_5.addWidget(self.vkspp_pushButton)
        self.vkspp_respGroupBox = QtWidgets.QGroupBox(self.tab_vksearchpostponed)
        self.vkspp_respGroupBox.setEnabled(False)
        self.vkspp_respGroupBox.setObjectName("vkspp_respGroupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.vkspp_respGroupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.vkspp_respTableWidget = QtWidgets.QTableWidget(self.vkspp_respGroupBox)
        self.vkspp_respTableWidget.setEnabled(False)
        self.vkspp_respTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.vkspp_respTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.vkspp_respTableWidget.setDragEnabled(True)
        self.vkspp_respTableWidget.setColumnCount(4)
        self.vkspp_respTableWidget.setObjectName("vkspp_respTableWidget")
        self.vkspp_respTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.vkspp_respTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vkspp_respTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.vkspp_respTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.vkspp_respTableWidget.setHorizontalHeaderItem(3, item)
        self.vkspp_respTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_6.addWidget(self.vkspp_respTableWidget)
        self.vkspp_progressBar = QtWidgets.QProgressBar(self.vkspp_respGroupBox)
        self.vkspp_progressBar.setMinimum(0)
        self.vkspp_progressBar.setMaximum(1)
        self.vkspp_progressBar.setProperty("value", 0)
        self.vkspp_progressBar.setTextVisible(False)
        self.vkspp_progressBar.setObjectName("vkspp_progressBar")
        self.verticalLayout_6.addWidget(self.vkspp_progressBar)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vkspp_htmlGenButton = QtWidgets.QPushButton(self.vkspp_respGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vkspp_htmlGenButton.sizePolicy().hasHeightForWidth())
        self.vkspp_htmlGenButton.setSizePolicy(sizePolicy)
        self.vkspp_htmlGenButton.setObjectName("vkspp_htmlGenButton")
        self.horizontalLayout_3.addWidget(self.vkspp_htmlGenButton)
        self.label = QtWidgets.QLabel(self.vkspp_respGroupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.vkspp_fromSpinBox = QtWidgets.QSpinBox(self.vkspp_respGroupBox)
        self.vkspp_fromSpinBox.setMinimum(1)
        self.vkspp_fromSpinBox.setMaximum(1)
        self.vkspp_fromSpinBox.setObjectName("vkspp_fromSpinBox")
        self.horizontalLayout_3.addWidget(self.vkspp_fromSpinBox)
        self.label_2 = QtWidgets.QLabel(self.vkspp_respGroupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.vkspp_toSpinBox = QtWidgets.QSpinBox(self.vkspp_respGroupBox)
        self.vkspp_toSpinBox.setMinimum(1)
        self.vkspp_toSpinBox.setMaximum(1)
        self.vkspp_toSpinBox.setDisplayIntegerBase(10)
        self.vkspp_toSpinBox.setObjectName("vkspp_toSpinBox")
        self.horizontalLayout_3.addWidget(self.vkspp_toSpinBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.vkspp_respGroupBox)
        self.tabWidget.addTab(self.tab_vksearchpostponed, "")
        self.tab_vkpostsaver = QtWidgets.QWidget()
        self.tab_vkpostsaver.setObjectName("tab_vkpostsaver")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_vkpostsaver)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.vkps_postBox = QtWidgets.QGroupBox(self.tab_vkpostsaver)
        self.vkps_postBox.setEnabled(True)
        self.vkps_postBox.setAlignment(QtCore.Qt.AlignCenter)
        self.vkps_postBox.setObjectName("vkps_postBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.vkps_postBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vkps_postLink = QtWidgets.QLineEdit(self.vkps_postBox)
        self.vkps_postLink.setObjectName("vkps_postLink")
        self.horizontalLayout_2.addWidget(self.vkps_postLink)
        self.vkps_getPostButton = QtWidgets.QPushButton(self.vkps_postBox)
        self.vkps_getPostButton.setObjectName("vkps_getPostButton")
        self.horizontalLayout_2.addWidget(self.vkps_getPostButton)
        self.verticalLayout_7.addWidget(self.vkps_postBox)
        self.vkps_fileBox = QtWidgets.QGroupBox(self.tab_vkpostsaver)
        self.vkps_fileBox.setAlignment(QtCore.Qt.AlignCenter)
        self.vkps_fileBox.setObjectName("vkps_fileBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.vkps_fileBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.vkps_fileEdit = QtWidgets.QLineEdit(self.vkps_fileBox)
        self.vkps_fileEdit.setObjectName("vkps_fileEdit")
        self.horizontalLayout_4.addWidget(self.vkps_fileEdit)
        self.vkps_fileButton = QtWidgets.QToolButton(self.vkps_fileBox)
        self.vkps_fileButton.setObjectName("vkps_fileButton")
        self.horizontalLayout_4.addWidget(self.vkps_fileButton)
        self.verticalLayout_7.addWidget(self.vkps_fileBox)
        self.vkps_downloadButton = QtWidgets.QPushButton(self.tab_vkpostsaver)
        self.vkps_downloadButton.setObjectName("vkps_downloadButton")
        self.verticalLayout_7.addWidget(self.vkps_downloadButton)
        self.vkps_progressBar = QtWidgets.QProgressBar(self.tab_vkpostsaver)
        self.vkps_progressBar.setProperty("value", 0)
        self.vkps_progressBar.setObjectName("vkps_progressBar")
        self.verticalLayout_7.addWidget(self.vkps_progressBar)
        self.tabWidget.addTab(self.tab_vkpostsaver, "")
        self.tab_info = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_info.sizePolicy().hasHeightForWidth())
        self.tab_info.setSizePolicy(sizePolicy)
        self.tab_info.setObjectName("tab_info")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_info)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.info_1_hor = QtWidgets.QHBoxLayout()
        self.info_1_hor.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.info_1_hor.setContentsMargins(0, 0, -1, 0)
        self.info_1_hor.setObjectName("info_1_hor")
        self.info_ava = QtWidgets.QGraphicsView(self.tab_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_ava.sizePolicy().hasHeightForWidth())
        self.info_ava.setSizePolicy(sizePolicy)
        self.info_ava.setMaximumSize(QtCore.QSize(100, 100))
        self.info_ava.setSizeIncrement(QtCore.QSize(0, 0))
        self.info_ava.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info_ava.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info_ava.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.info_ava.setLineWidth(1)
        self.info_ava.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.info_ava.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.info_ava.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.info_ava.setAlignment(QtCore.Qt.AlignCenter)
        self.info_ava.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.info_ava.setObjectName("info_ava")
        self.info_1_hor.addWidget(self.info_ava)
        self.info_1_form = QtWidgets.QFormLayout()
        self.info_1_form.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.info_1_form.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.info_1_form.setObjectName("info_1_form")
        self.info_1_id_label = QtWidgets.QLabel(self.tab_info)
        self.info_1_id_label.setObjectName("info_1_id_label")
        self.info_1_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.info_1_id_label)
        self.info_1_id = QtWidgets.QLabel(self.tab_info)
        self.info_1_id.setObjectName("info_1_id")
        self.info_1_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.info_1_id)
        self.info_1_name_label = QtWidgets.QLabel(self.tab_info)
        self.info_1_name_label.setObjectName("info_1_name_label")
        self.info_1_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.info_1_name_label)
        self.info_1_name = QtWidgets.QLabel(self.tab_info)
        self.info_1_name.setObjectName("info_1_name")
        self.info_1_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.info_1_name)
        self.info_1_auth_lineEdit = QtWidgets.QLineEdit(self.tab_info)
        self.info_1_auth_lineEdit.setObjectName("info_1_auth_lineEdit")
        self.info_1_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.info_1_auth_lineEdit)
        self.info_1_auth_pushButton = QtWidgets.QPushButton(self.tab_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_1_auth_pushButton.sizePolicy().hasHeightForWidth())
        self.info_1_auth_pushButton.setSizePolicy(sizePolicy)
        self.info_1_auth_pushButton.setObjectName("info_1_auth_pushButton")
        self.info_1_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.info_1_auth_pushButton)
        self.info_1_accountsBox = QtWidgets.QComboBox(self.tab_info)
        self.info_1_accountsBox.setObjectName("info_1_accountsBox")
        self.info_1_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.info_1_accountsBox)
        self.info_1_hor.addLayout(self.info_1_form)
        self.verticalLayout_8.addLayout(self.info_1_hor)
        self.tabWidget.addTab(self.tab_info, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Утилиты для ВК"))
        self.vked_postBox.setTitle(_translate("MainWindow", "Ссылка на пост"))
        self.vked_getPostButton.setText(_translate("MainWindow", "Применить"))
        self.vked_postParametersBox.setTitle(_translate("MainWindow", "Параметры поста"))
        self.vked_owner_idLabel.setToolTip(_translate("MainWindow", "owner_id"))
        self.vked_owner_idLabel.setText(_translate("MainWindow", "ИД владельца"))
        self.vked_owner_id.setText(_translate("MainWindow", "owner_id"))
        self.vked_messageLabel.setToolTip(_translate("MainWindow", "message"))
        self.vked_messageLabel.setText(_translate("MainWindow", "Сообщение"))
        self.vked_attachmenntsLabel.setToolTip(_translate("MainWindow", "attachments"))
        self.vked_attachmenntsLabel.setText(_translate("MainWindow", "Вложения"))
        item = self.vked_attachments.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "type"))
        item = self.vked_attachments.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "attachment"))
        self.vked_addAttachButton.setText(_translate("MainWindow", "Добавить вложение"))
        self.vked_signed_2.setToolTip(_translate("MainWindow", "signed"))
        self.vked_signed_2.setText(_translate("MainWindow", "Подпись от автора"))
        self.vked_publish_dateLabel.setToolTip(_translate("MainWindow", "publish_date"))
        self.vked_publish_dateLabel.setText(_translate("MainWindow", "Дата публикации"))
        self.vked_post_idLabel.setToolTip(_translate("MainWindow", "post_id"))
        self.vked_post_idLabel.setText(_translate("MainWindow", "ИД поста"))
        self.vked_post_id.setText(_translate("MainWindow", "post_id"))
        self.vked_mark_as_ads.setToolTip(_translate("MainWindow", "mark_as_ads"))
        self.vked_mark_as_ads.setText(_translate("MainWindow", "Это реклама"))
        self.vked_close_comments.setToolTip(_translate("MainWindow", "close_comments"))
        self.vked_close_comments.setText(_translate("MainWindow", "Закрыть комментарии"))
        self.vked_copyrightLabel.setToolTip(_translate("MainWindow", "copyright"))
        self.vked_copyrightLabel.setText(_translate("MainWindow", "Источник"))
        self.vked_previewButton.setText(_translate("MainWindow", "Предпросмотр"))
        self.vked_postButton.setText(_translate("MainWindow", "Опубликовать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vkeditor), _translate("MainWindow", "Редактор постов"))
        self.vkspp_publicLineEdit.setPlaceholderText(_translate("MainWindow", "Ссылка на паблик"))
        self.vkspp_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Введите искомый текст"))
        self.vkspp_textdescCheckBox.setText(_translate("MainWindow", "Искать в тексте поста"))
        self.vkspp_attachCheckBox.setText(_translate("MainWindow", "Искать в описаниях вложений"))
        self.vkspp_postponed_radioButton.setText(_translate("MainWindow", "Отложка"))
        self.vkspp_suggests_radioButton.setText(_translate("MainWindow", "Предложка"))
        self.vkspp_pushButton.setText(_translate("MainWindow", "Искать"))
        self.vkspp_respGroupBox.setTitle(_translate("MainWindow", "Найденные посты"))
        item = self.vkspp_respTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ссылка"))
        item = self.vkspp_respTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Время"))
        item = self.vkspp_respTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вложений"))
        item = self.vkspp_respTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Автор"))
        self.vkspp_progressBar.setFormat(_translate("MainWindow", "%v/%m"))
        self.vkspp_htmlGenButton.setText(_translate("MainWindow", "Генерировать HTML"))
        self.label.setText(_translate("MainWindow", "C "))
        self.label_2.setText(_translate("MainWindow", " до "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vksearchpostponed), _translate("MainWindow", "Поиск по стене"))
        self.vkps_postBox.setTitle(_translate("MainWindow", "Ссылка на пост"))
        self.vkps_getPostButton.setText(_translate("MainWindow", "Применить"))
        self.vkps_fileBox.setTitle(_translate("MainWindow", "Папка"))
        self.vkps_fileButton.setText(_translate("MainWindow", "Выберите папку"))
        self.vkps_downloadButton.setText(_translate("MainWindow", "Скачать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vkpostsaver), _translate("MainWindow", "Сохранятель постов"))
        self.info_1_id_label.setText(_translate("MainWindow", "ИД текущего аккаунта"))
        self.info_1_id.setText(_translate("MainWindow", "id"))
        self.info_1_name_label.setText(_translate("MainWindow", "Имя"))
        self.info_1_name.setText(_translate("MainWindow", "name"))
        self.info_1_auth_lineEdit.setPlaceholderText(_translate("MainWindow", "Введите логин"))
        self.info_1_auth_pushButton.setText(_translate("MainWindow", "Сменить аккаунт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), _translate("MainWindow", "Инфо"))
