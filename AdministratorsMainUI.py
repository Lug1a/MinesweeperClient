# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administratorsMainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from GamerDataAdminUI import Ui_Dialog as gamer_data
from LevelDataAdmin import Ui_Dialog as level_data
from ShopDataAdmin import Ui_Dialog as shop_data
from GamerAccountAdminUI import Ui_dialog as gamer_account_data
from AdministratorAccountAdminUI import Ui_dialog as administrator_account_data
from GameRecordAdmin import Ui_Dialog as record_data
from QDialog import myDialog
import json
from TcpClient import tcp_client_socket

class Ui_Dialog(object):
    def setupUi(self, Dialog, administratorsID, username, is_super):
        self.path = "icon"
        self.form = Dialog
        self.administratorsID = administratorsID
        self.username = username
        self.is_super = is_super
        Dialog.setObjectName("Dialog")
        Dialog.resize(1112, 749)
        Dialog.setMinimumSize(QtCore.QSize(171, 0))
        Dialog.setMaximumSize(QtCore.QSize(1112, 749))
        Dialog.setStyleSheet("#Dialog{background-color: gainsboro;\n"
                             "border-image: url(" + self.path + "/background.jpg);}")  # 设置背景图片

        self.ID_button = QtWidgets.QPushButton(Dialog)
        self.ID_button.setGeometry(QtCore.QRect(0, 0, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ID_button.setFont(font)
        self.ID_button.setStyleSheet(
            "QPushButton { color: rgba(255, 255, 255, 250);background-color: rgba(0,85,127,100);;border:none }")
        self.ID_button.setFlat(False)
        self.ID_button.setObjectName("ID_button")

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 40, 901, 721))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gamer_account = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gamer_account.setMinimumSize(QtCore.QSize(171, 91))
        self.gamer_account.setMaximumSize(QtCore.QSize(171, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.gamer_account.setFont(font)
        self.gamer_account.setMouseTracking(False)
        self.gamer_account.setTabletTracking(False)
        self.gamer_account.setStyleSheet(
            "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
        self.gamer_account.setIconSize(QtCore.QSize(171, 91))
        self.gamer_account.setFlat(False)
        self.gamer_account.setObjectName("signle_game_button")
        self.gridLayout.addWidget(self.gamer_account, 1, 0, 1, 1)
        self.gamer_data = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gamer_data.setMinimumSize(QtCore.QSize(171, 91))
        self.gamer_data.setMaximumSize(QtCore.QSize(171, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.gamer_data.setFont(font)
        self.gamer_data.setStyleSheet(
            "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
        self.gamer_data.setObjectName("battle_button")
        self.gridLayout.addWidget(self.gamer_data, 1, 1, 1, 1)
        self.level = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.level.setMinimumSize(QtCore.QSize(171, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.level.setFont(font)
        self.level.setStyleSheet(
            "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
        self.level.setObjectName("list_button")
        self.gridLayout.addWidget(self.level, 2, 0, 1, 1)
        self.record = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.record.setMinimumSize(QtCore.QSize(171, 91))
        self.record.setMaximumSize(QtCore.QSize(171, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.record.setFont(font)
        self.record.setStyleSheet(
            "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
        self.record.setObjectName("list_button_4")
        self.gridLayout.addWidget(self.record, 3, 0, 1, 1)
        self.shop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.shop.setMinimumSize(QtCore.QSize(171, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.shop.setFont(font)
        self.shop.setStyleSheet(
            "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
        self.shop.setObjectName("list_button_3")
        self.gridLayout.addWidget(self.shop, 2, 1, 1, 1)

        if self.is_super == "1":
            self.administrators = QtWidgets.QPushButton(self.gridLayoutWidget)
            self.administrators.setMinimumSize(QtCore.QSize(171, 91))
            font = QtGui.QFont()
            font.setFamily("幼圆")
            font.setPointSize(15)
            font.setBold(True)
            font.setItalic(True)
            font.setWeight(75)
            font.setStrikeOut(False)
            self.administrators.setFont(font)
            self.administrators.setStyleSheet(
                "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
            self.administrators.setObjectName("list_button_5")
            self.gridLayout.addWidget(self.administrators, 3, 1, 1, 1)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "管理员界面"))
        self.ID_button.setText(_translate("Dialog", self.username))
        self.gamer_account.setText(_translate("Dialog", "玩家账号管理"))
        self.gamer_data.setText(_translate("Dialog", "玩家数据管理"))
        self.level.setText(_translate("Dialog", "关卡管理"))
        self.record.setText(_translate("Dialog", "战绩管理"))
        self.shop.setText(_translate("Dialog", "商城管理"))
        if self.is_super == "1":
            self.administrators.setText(_translate("Dialog", "管理员管理"))
            self.administrators.clicked.connect(self.administrator_account_jump)

        self.gamer_data.clicked.connect(self.gamer_data_jump)  # 连接槽函数
        self.level.clicked.connect(self.level_data_jump)  # 连接槽函数
        self.shop.clicked.connect(self.shop_data_jump)  # 连接槽函数
        self.gamer_account.clicked.connect(self.gamer_account_jump)
        self.record.clicked.connect(self.record_data_jump)


    def gamer_data_jump(self):
        self.form.setEnabled(False)  # 设置本窗口无法选择

        form = myDialog()
        form.setWindowModality(2)  # 使本窗口无法选中
        ui = gamer_data()
        ui.setupUi(form, self.administratorsID)
        form.show()
        form.exec_()
        self.form.setEnabled(True)

    def level_data_jump(self):
        self.form.setEnabled(False)  # 设置本窗口无法选择

        form = myDialog()
        form.setWindowModality(2)  # 使本窗口无法选中
        ui = level_data()
        ui.setupUi(form,self.administratorsID)
        form.show()
        form.exec_()
        self.form.setEnabled(True)

    def shop_data_jump(self):
        self.form.setEnabled(False)  # 设置本窗口无法选择

        form = myDialog()
        form.setWindowModality(2)  # 使本窗口无法选中
        ui = shop_data()
        ui.setupUi(form,self.administratorsID)
        form.show()
        form.exec_()
        self.form.setEnabled(True)
        
    def gamer_account_jump(self):
        self.form.setEnabled(False)  # 设置本窗口无法选择

        tcp_client_socket.send("812 " + self.administratorsID)
        data_list_813 = tcp_client_socket.rec().split("@")
        playerData = json.loads(data_list_813[1])

        form = myDialog()
        form.setWindowModality(2)  # 使本窗口无法选中
        ui = gamer_account_data()
        ui.setupUi(form, self.administratorsID, playerData)
        form.show()
        form.exec_()
        self.form.setEnabled(True)

    def administrator_account_jump(self):
        self.form.setEnabled(False)  # 设置本窗口无法选择

        tcp_client_socket.send("816 " + self.administratorsID)
        data_list_817 = tcp_client_socket.rec().split("@")
        administratorData = json.loads(data_list_817[1])

        form = myDialog()
        form.setWindowModality(2)  # 使本窗口无法选中
        ui = administrator_account_data()
        ui.setupUi(form, self.administratorsID, administratorData)
        form.show()
        form.exec_()
        self.form.setEnabled(True)

    def record_data_jump(self):
        self.form.setEnabled(False)  # 设置本窗口无法选择

        form = myDialog()
        form.setWindowModality(2)  # 使本窗口无法选中
        ui = record_data()
        ui.setupUi(form, self.administratorsID)
        form.show()
        form.exec_()
        self.form.setEnabled(True)
