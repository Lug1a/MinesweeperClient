# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import json
import sys

import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
import urllib.request

from MineSweeperUI import MineSweeperUI
import QDialog
from QDialog import MainDialog, MineDialog, myDialog, WaitDialog
from DifficultyChooseUI import DifficultyChoose_Dialog
from TcpClient import tcp_client_socket
from RankListUI import Ui_Dialog as Ranklist_Dialog
from PersonalInterfaceUI import Ui_Dialog as Personalinterface_Dialog
from GameMessage import Wait_Dialog
from ShopUI import Ui_Dialog as Shop_Dialog
from BagUI import Ui_Dialog as Bag_Dialog
from FriendListUI import Ui_dialog as FriendList_Dialog
from SettingUI import Ui_Dialog as setting_Dialog


class Ui_Dialog(object):
    def setupUi(self, Dialog, userID):
        self.path = "icon"
        self.form = Dialog
        self.userID = userID

        Dialog.setObjectName("Dialog")
        Dialog.resize(1112, 700)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())

        self.ID_button = QtWidgets.QPushButton(Dialog)
        self.ID_button.setGeometry(QtCore.QRect(0, 0, 225, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ID_button.setFont(font)
        self.ID_button.setStyleSheet(
            "QPushButton { color: rgba(255, 255, 255, 250);background-color: rgba(0,85,127,100);;border:none }")
        self.ID_button.setFlat(False)
        self.ID_button.setObjectName("ID_button")
        self.signle_game_button = QtWidgets.QPushButton(Dialog)
        self.signle_game_button.setGeometry(QtCore.QRect(460, 140, 171, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.signle_game_button.setFont(font)
        self.signle_game_button.setMouseTracking(False)
        self.signle_game_button.setTabletTracking(False)
        self.signle_game_button.setStyleSheet(
            "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
        self.signle_game_button.setIconSize(QtCore.QSize(171, 91))
        self.signle_game_button.setFlat(False)
        self.signle_game_button.setObjectName("signle_game_button")
        self.battle_button = QtWidgets.QPushButton(Dialog)
        self.battle_button.setGeometry(QtCore.QRect(460, 340, 171, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.battle_button.setFont(font)
        self.battle_button.setStyleSheet(
            "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
        self.battle_button.setObjectName("battle_button")
        self.list_button = QtWidgets.QPushButton(Dialog)
        self.list_button.setGeometry(QtCore.QRect(460, 540, 171, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.list_button.setFont(font)
        self.list_button.setStyleSheet(
            "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
        self.list_button.setObjectName("list_button")
        self.shop_button = QtWidgets.QPushButton(Dialog)
        self.shop_button.setGeometry(QtCore.QRect(1000, 130, 71, 71))
        # self.shop_button.setStyleSheet("\n"
        #                                "background-color: rgb(227, 220, 255);\n"
        #                                "border:none")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.path + "/商城.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shop_button.setIcon(icon)
        self.shop_button.setIconSize(QtCore.QSize(64, 64))
        self.shop_button.setFlat(True)
        self.shop_button.setObjectName("shop_button")
        self.bag_button = QtWidgets.QPushButton(Dialog)
        self.bag_button.setGeometry(QtCore.QRect(1000, 260, 71, 71))
        # self.bag_button.setStyleSheet("\n"
        #                               "background-color: rgb(227, 220, 255);\n"
        #                               "border:none")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.path + "/背包.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bag_button.setIcon(icon1)
        self.bag_button.setIconSize(QtCore.QSize(64, 64))
        self.bag_button.setFlat(True)
        self.bag_button.setObjectName("bag_button")
        self.friend_button = QtWidgets.QPushButton(Dialog)
        self.friend_button.setGeometry(QtCore.QRect(1000, 390, 71, 71))
        # self.friend_button.setStyleSheet("\n"
        #                                  "background-color: rgb(227, 220, 255);\n"
        #                                  "border:none")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.path + "/好友.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.friend_button.setIcon(icon2)
        self.friend_button.setIconSize(QtCore.QSize(76, 76))
        self.friend_button.setFlat(True)
        self.friend_button.setObjectName("friend_button")
        self.setting_button = QtWidgets.QPushButton(Dialog)
        self.setting_button.setGeometry(QtCore.QRect(1000, 520, 71, 71))
        # self.setting_button.setStyleSheet("\n"
        #                                   "background-color: rgb(227, 220, 255);\n"
        #                                   "border:none")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.path + "/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_button.setIcon(icon2)
        self.setting_button.setIconSize(QtCore.QSize(76, 76))
        self.setting_button.setFlat(True)
        self.setting_button.setObjectName("setting_button")
        self.shop_label = QtWidgets.QLabel(Dialog)
        self.shop_label.setGeometry(QtCore.QRect(1010, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.shop_label.setFont(font)
        self.shop_label.setObjectName("shop_label")
        self.bag_label = QtWidgets.QLabel(Dialog)
        self.bag_label.setGeometry(QtCore.QRect(1010, 340, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.bag_label.setFont(font)
        self.bag_label.setObjectName("bag_label")
        self.friend_label = QtWidgets.QLabel(Dialog)
        self.friend_label.setGeometry(QtCore.QRect(1010, 470, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.friend_label.setFont(font)
        self.friend_label.setObjectName("friend_label")
        self.setting_label = QtWidgets.QLabel(Dialog)
        self.setting_label.setGeometry(QtCore.QRect(1010, 600, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.setting_label.setFont(font)
        self.setting_label.setObjectName("setting_label")
        self.point_label = QtWidgets.QLabel(Dialog)
        self.point_label.setEnabled(True)
        self.point_label.setGeometry(QtCore.QRect(980, 10, 39, 36))
        self.point_label.setText("")
        self.point_label.setPixmap(QtGui.QPixmap(self.path + "/积分.png"))
        self.point_label.setObjectName("point_label")
        self.gold_label = QtWidgets.QLabel(Dialog)
        self.gold_label.setEnabled(True)
        self.gold_label.setGeometry(QtCore.QRect(980, 40, 61, 81))
        self.gold_label.setText("")
        self.gold_label.setPixmap(QtGui.QPixmap(self.path + "/金币.png"))
        self.gold_label.setObjectName("gold_label")
        self.point_num_label = QtWidgets.QLabel(Dialog)
        self.point_num_label.setEnabled(True)
        self.point_num_label.setGeometry(QtCore.QRect(1020, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.point_num_label.setFont(font)
        self.point_num_label.setObjectName("point_num_label")
        self.gold_num_label = QtWidgets.QLabel(Dialog)
        self.gold_num_label.setEnabled(True)
        self.gold_num_label.setGeometry(QtCore.QRect(1020, 40, 121, 81))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.gold_num_label.setFont(font)
        self.gold_num_label.setObjectName("gold_num_label")

        self.update_message()  # 获取信息
        self.update_pic()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "扫雷游戏大厅"))
        self.ID_button.setText(_translate("Dialog", '用户名：' + self.username))
        self.signle_game_button.setText(_translate("Dialog", "单人游戏"))
        self.battle_button.setText(_translate("Dialog", "匹配对战"))
        self.list_button.setText(_translate("Dialog", "排行榜"))
        self.shop_label.setText(_translate("Dialog", "商城"))
        self.bag_label.setText(_translate("Dialog", "背包"))
        self.friend_label.setText(_translate("Dialog", "好友"))
        self.setting_label.setText(_translate("Dialog", "设置"))

        self.signle_game_button.clicked.connect(self.signle_game_jump_to_difficulty_choose)  # 连接槽函数
        self.battle_button.clicked.connect(self.conflict_game_jump_to_difficulty_choose)  # 连接槽函数
        self.list_button.clicked.connect(self.jump_to_ranklist)  # 连接槽函数
        self.shop_button.clicked.connect(self.jump_to_shop)  # 连接槽函数
        self.bag_button.clicked.connect(self.jump_to_bag)  # 连接槽函数
        self.ID_button.clicked.connect(self.jump_to_personal_interface)  # 连接槽函数
        self.friend_button.clicked.connect(self.jump_to_friendList)  # 连接槽函数
        self.setting_button.clicked.connect(self.jump_to_setting)  # 连接槽函数

    # 更新主界面信息
    def update_message(self):
        # 向服务器发送玩家数据请求请求
        tcp_client_socket.send("200 " + self.userID)
        userData_list = tcp_client_socket.rec().split()
        self.username = userData_list[1]
        self.userID = userData_list[2]
        self.point = userData_list[3]
        self.gold = userData_list[4]
        self.background_volume = float(int(userData_list[5]) / 100)
        self.sound_volume = float(int(userData_list[6]) / 100)
        self.skin_url = userData_list[7]

        self.form.sound = self.sound_volume  # 设置音量

        # 设置金币积分
        self.point_num_label.setText(self.point)
        self.gold_num_label.setText(self.gold)

    def update_pic(self):
        urllib.request.urlretrieve(self.skin_url, filename=self.path + '/background.jpg')  # 下载图片
        self.form.setStyleSheet("#Dialog{background-color: gainsboro;\n"
                                "border-image: url(" + self.path + "/background.jpg);}")  # 设置背景图片

    # 单人游戏，跳转到难度选择界面,获得选择的难度后跳转到游戏界面
    def signle_game_jump_to_difficulty_choose(self):
        self.form.setEnabled(False)

        # 向服务器请求关卡数据和玩家数据
        tcp_client_socket.send("202 " + self.userID)
        data_list_203 = tcp_client_socket.rec().split("@")
        self.level_data = json.loads(data_list_203[1])
        self.stagenum = int(data_list_203[2])

        # 转到难度选择窗口
        difficulty_choose_form = myDialog()
        difficulty_choose_form.setWindowModality(2)  # 使本窗口无法选中
        difficulty_ui = DifficultyChoose_Dialog()
        difficulty_ui.setupUi(difficulty_choose_form, self.level_data)
        difficulty_choose_form.sound = self.sound_volume  # 设置音效音量
        difficulty_choose_form.show()
        difficulty_choose_form.exec_()

        diffculty = difficulty_ui.getDifficulty()  # 获取选择的难度
        if diffculty != -1:  # 如果选择了难度则跳转到游戏界面
            game_form = MineDialog()
            game_form.setWindowModality(2)  # 使本窗口无法选中
            game_ui = MineSweeperUI(game_form, diffculty + 1, self.level_data[diffculty], self.stagenum, self.userID, 0,
                                    self.background_volume)
            game_form.show()
            game_form.exec_()

            game_ui.getData()  # 如果是强制关闭则发送计算分数的请求给服务器
            self.update_message()  # 更新主界面信息

        self.form.setEnabled(True)

    # 匹配游戏，跳转到难度选择界面,获得选择的难度后跳转到等待界面，再到游戏界面
    def conflict_game_jump_to_difficulty_choose(self):
        self.form.setEnabled(False)

        # 向服务器请求关卡数据和玩家数据
        tcp_client_socket.send("202 " + self.userID)
        data_203 = tcp_client_socket.rec()
        data_list_203 = data_203.split("@")
        self.level_data = json.loads(data_list_203[1])
        self.stagenum = int(data_list_203[2])

        # 转到难度选择窗口
        difficulty_choose_form = myDialog()
        difficulty_choose_form.setWindowModality(2)  # 使本窗口无法选中
        difficulty_ui = DifficultyChoose_Dialog()
        difficulty_ui.setupUi(difficulty_choose_form, self.level_data)
        difficulty_choose_form.sound = self.sound_volume  # 设置音效音量
        difficulty_choose_form.show()
        difficulty_choose_form.exec_()

        diffculty = difficulty_ui.getDifficulty()  # 获取选择的难度
        if diffculty != -1:  # 如果选择了难度则跳转到游戏界面
            wait_form = WaitDialog()
            wait_form.setWindowModality(2)  # 使本窗口无法选中
            wait_ui = Wait_Dialog()
            wait_ui.setupUi(wait_form, self.userID, self.point, diffculty + 1, self.username)
            wait_form.sound = self.sound_volume  # 设置音效音量
            wait_form.show()
            wait_form.exec_()

            match = wait_ui.get_match()
            if match == 1:  # 如果匹配成功则跳转到游戏界面
                game_form = MineDialog()
                game_form.setWindowModality(2)  # 使本窗口无法选中
                game_ui = MineSweeperUI(game_form, diffculty + 1, self.level_data[diffculty], self.stagenum,
                                        self.userID, 1, self.background_volume)

                game_form.show()
                game_form.exec_()
                game_ui.getData()  # 如果是强制关闭则发送计算分数的请求给服务器
                game_ui.updateStage() #更新道具数量
                self.update_message()  # 更新主界面信息

        self.form.setEnabled(True)

    # 跳转到排行榜界面
    def jump_to_ranklist(self):
        self.form.setEnabled(False)  # 设置本窗口无法选择

        # 向服务器请求排行数据
        tcp_client_socket.send("204 " + self.userID)
        data_list_205 = tcp_client_socket.rec().split("@")
        self.rank_list = json.loads(data_list_205[1])

        form1 = myDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = Ranklist_Dialog()
        ui.setupUi(form1, self.userID, self.rank_list)
        form1.sound = self.sound_volume  # 设置音效音量
        form1.show()
        form1.exec_()
        self.update_message()  # 更新主界面信息
        self.form.setEnabled(True)

    # 跳转到个人界面
    def jump_to_personal_interface(self):
        self.form.setEnabled(False)

        # 向服务器请求个人战绩数据
        tcp_client_socket.send("206 " + self.userID + " " + self.userID)
        data_list_207 = tcp_client_socket.rec().split("@")
        self.exploits_list = json.loads(data_list_207[5])

        form1 = myDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = Personalinterface_Dialog()
        ui.setupUi(form1, self.userID, 0, data_list_207[1], data_list_207[2], data_list_207[3], data_list_207[4],
                   self.exploits_list, data_list_207[6])
        form1.sound = self.sound_volume  # 设置音效音量
        form1.show()
        form1.exec_()
        self.update_message()  # 更新主界面信息
        self.form.setEnabled(True)

    def jump_to_shop(self):
        self.form.setEnabled(False)

        # 向服务器请求排行数据
        form1 = myDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = Shop_Dialog()
        ui.setupUi(form1, self.userID)
        form1.sound = self.sound_volume  # 设置音效音量
        form1.show()
        form1.exec_()
        self.update_message()  # 更新主界面信息
        self.form.setEnabled(True)

    def jump_to_bag(self):
        self.form.setEnabled(False)

        # 向服务器请求排行数据
        form1 = myDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = Bag_Dialog()
        ui.setupUi(form1, self.userID)
        form1.sound = self.sound_volume  # 设置音效音量
        form1.show()
        form1.exec_()
        self.form.setEnabled(True)
        self.update_message()
        self.update_pic()
        # self.form.setStyleSheet("#Dialog{background-color: gainsboro;\n"
        #                         "border-image: url(" + self.path + "/background.jpg);}")  # 设置背景图片

    def jump_to_friendList(self):
        self.form.setEnabled(False)

        # 向服务器请求好友列表数据
        tcp_client_socket.send("600 " + self.userID)
        data_list_601 = tcp_client_socket.rec().split("@")
        self.friend_list = json.loads(data_list_601[1])

        form1 = myDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = FriendList_Dialog()
        ui.setupUi(form1, self.userID, len(self.friend_list), self.friend_list)
        form1.sound = self.sound_volume  # 设置音效音量
        form1.show()
        form1.exec_()
        self.update_message()  # 更新主界面信息
        self.form.setEnabled(True)

    def jump_to_setting(self):
        # self.form.setEnabled(False)

        # 向服务器请求设置信息
        tcp_client_socket.send("700 " + self.userID)
        data_list_701 = tcp_client_socket.rec().split("@")

        self.username = data_list_701[1]
        self.userID = data_list_701[2]
        self.background_volume = int(data_list_701[3])
        self.sound_volume = int(data_list_701[4])

        form1 = myDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = setting_Dialog()
        ui.setupUi(form1, self.userID, self.username, self.background_volume, self.sound_volume)
        form1.sound = self.sound_volume  # 设置音效音量
        form1.show()
        form1.exec_()
        self.update_message()
        self.form.setEnabled(True)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     form = MainDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(form, "123")
#     form.show()
#     sys.exit(app.exec_())
