# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GamerDataAdminUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import json
import urllib.request
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView

from TcpClient import tcp_client_socket
from FlowLayout import FlowLayout


class Ui_Dialog(object):
    def setupUi(self, Dialog, administratorsID):
        Dialog.setObjectName("Dialog")
        Dialog.resize(766, 680)
        self.path = "icon"
        self.form = Dialog
        self.administratorsID = administratorsID
        self.label_userID = QtWidgets.QLabel(Dialog)
        self.label_userID.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_userID.setObjectName("label_userID")
        self.lineEdit_userID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_userID.setGeometry(QtCore.QRect(100, 10, 131, 21))
        self.lineEdit_userID.setObjectName("lineEdit_userID")
        self.label_point = QtWidgets.QLabel(Dialog)
        self.label_point.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_point.setObjectName("label_point")
        self.lineEdit_point = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_point.setEnabled(True)
        self.lineEdit_point.setGeometry(QtCore.QRect(100, 80, 131, 21))
        self.lineEdit_point.setReadOnly(True)
        self.lineEdit_point.setObjectName("lineEdit_point")
        self.pushButton_point = QtWidgets.QPushButton(Dialog)
        self.pushButton_point.setGeometry(QtCore.QRect(260, 80, 71, 21))
        self.pushButton_point.setObjectName("pushButton_point")
        self.pushButton_pointM = QtWidgets.QPushButton(Dialog)
        self.pushButton_pointM.setGeometry(QtCore.QRect(260, 120, 71, 21))
        self.pushButton_pointM.setObjectName("pushButton_pointM")
        self.label_pointM = QtWidgets.QLabel(Dialog)
        self.label_pointM.setGeometry(QtCore.QRect(20, 120, 71, 21))
        self.label_pointM.setObjectName("label_pointM")
        self.lineEdit_pointM = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pointM.setGeometry(QtCore.QRect(100, 120, 131, 21))
        self.lineEdit_pointM.setObjectName("lineEdit_pointM")
        self.pushButton_gold = QtWidgets.QPushButton(Dialog)
        self.pushButton_gold.setGeometry(QtCore.QRect(260, 160, 71, 21))
        self.pushButton_gold.setObjectName("pushButton_gold")
        self.label_gold = QtWidgets.QLabel(Dialog)
        self.label_gold.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.label_gold.setObjectName("label_gold")
        self.lineEdit_gold = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_gold.setEnabled(True)
        self.lineEdit_gold.setGeometry(QtCore.QRect(100, 160, 131, 21))
        self.lineEdit_gold.setReadOnly(True)
        self.lineEdit_gold.setObjectName("lineEdit_gold")
        self.pushButton_goldM = QtWidgets.QPushButton(Dialog)
        self.pushButton_goldM.setGeometry(QtCore.QRect(260, 200, 71, 21))
        self.pushButton_goldM.setObjectName("pushButton_goldM")
        self.label_goldM = QtWidgets.QLabel(Dialog)
        self.label_goldM.setGeometry(QtCore.QRect(20, 200, 71, 21))
        self.label_goldM.setObjectName("label_goldM")
        self.lineEdit_goldM = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_goldM.setGeometry(QtCore.QRect(100, 200, 131, 21))
        self.lineEdit_goldM.setObjectName("lineEdit_goldM")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(10, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.pushButton_sound = QtWidgets.QPushButton(Dialog)
        self.pushButton_sound.setGeometry(QtCore.QRect(620, 80, 71, 21))
        self.pushButton_sound.setObjectName("pushButton_sound")
        self.pushButton_volumeM = QtWidgets.QPushButton(Dialog)
        self.pushButton_volumeM.setGeometry(QtCore.QRect(620, 200, 71, 21))
        self.pushButton_volumeM.setObjectName("pushButton_volumeM")
        self.pushButton_volume = QtWidgets.QPushButton(Dialog)
        self.pushButton_volume.setGeometry(QtCore.QRect(620, 160, 71, 21))
        self.pushButton_volume.setObjectName("pushButton_volume")
        self.lineEdit_sound = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_sound.setGeometry(QtCore.QRect(460, 80, 131, 21))
        self.lineEdit_sound.setReadOnly(True)
        self.lineEdit_sound.setObjectName("lineEdit_sound")
        self.label_volume = QtWidgets.QLabel(Dialog)
        self.label_volume.setGeometry(QtCore.QRect(380, 160, 71, 21))
        self.label_volume.setObjectName("label_volume")
        self.label_volumeM = QtWidgets.QLabel(Dialog)
        self.label_volumeM.setGeometry(QtCore.QRect(380, 200, 71, 21))
        self.label_volumeM.setObjectName("label_volumeM")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_soundM = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_soundM.setGeometry(QtCore.QRect(460, 120, 131, 21))
        self.lineEdit_soundM.setReadOnly(False)
        self.lineEdit_soundM.setObjectName("lineEdit_soundM")
        self.lineEdit_volumeM = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_volumeM.setGeometry(QtCore.QRect(460, 200, 131, 21))
        self.lineEdit_volumeM.setObjectName("lineEdit_volumeM")
        self.lineEdit_volume = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_volume.setGeometry(QtCore.QRect(460, 160, 131, 21))
        self.lineEdit_volume.setReadOnly(True)
        self.lineEdit_volume.setObjectName("lineEdit_volume")
        self.label_soundM = QtWidgets.QLabel(Dialog)
        self.label_soundM.setGeometry(QtCore.QRect(380, 120, 71, 21))
        self.label_soundM.setObjectName("label_soundM")
        self.label_sound = QtWidgets.QLabel(Dialog)
        self.label_sound.setGeometry(QtCore.QRect(380, 80, 71, 21))
        self.label_sound.setObjectName("label_sound")
        self.pushButton_soundM = QtWidgets.QPushButton(Dialog)
        self.pushButton_soundM.setGeometry(QtCore.QRect(620, 120, 71, 21))
        self.pushButton_soundM.setObjectName("pushButton_soundM")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 161, 31))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_friend = QtWidgets.QPushButton(Dialog)
        self.pushButton_friend.setGeometry(QtCore.QRect(260, 290, 71, 21))
        self.pushButton_friend.setObjectName("pushButton_stage")
        self.label_friend = QtWidgets.QLabel(Dialog)
        self.label_friend.setGeometry(QtCore.QRect(20, 290, 71, 21))
        self.label_friend.setObjectName("label_stage")

        self.tableWidget_friend = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_friend.setGeometry(QtCore.QRect(20, 320, 311, 331))
        self.tableWidget_friend.setObjectName("tableWidget")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(370, 250, 161, 31))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_stage = QtWidgets.QPushButton(Dialog)
        self.pushButton_stage.setGeometry(QtCore.QRect(620, 290, 71, 21))
        self.pushButton_stage.setObjectName("pushButton_stage")
        self.label_stage = QtWidgets.QLabel(Dialog)
        self.label_stage.setGeometry(QtCore.QRect(380, 290, 71, 21))
        self.label_stage.setObjectName("label_stage")
        self.lineEdit_stage = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_stage.setEnabled(True)
        self.lineEdit_stage.setGeometry(QtCore.QRect(460, 290, 131, 21))
        self.lineEdit_stage.setText("")
        self.lineEdit_stage.setReadOnly(True)
        self.lineEdit_stage.setObjectName("lineEdit_stage")
        self.label_skin = QtWidgets.QLabel(Dialog)
        self.label_skin.setGeometry(QtCore.QRect(380, 320, 71, 21))
        self.label_skin.setObjectName("label_skin")
        self.listWidget_skin = QtWidgets.QListWidget(Dialog)
        self.listWidget_skin.setGeometry(QtCore.QRect(380, 350, 351, 301))
        self.listWidget_skin.setObjectName("listView_skin")
        self.pushButton_skin = QtWidgets.QPushButton(Dialog)
        self.pushButton_skin.setGeometry(QtCore.QRect(460, 320, 71, 21))
        self.pushButton_skin.setObjectName("pushButton_skin")
        self.pushButton_userID = QtWidgets.QPushButton(Dialog)
        self.pushButton_userID.setGeometry(QtCore.QRect(260, 10, 71, 21))
        self.pushButton_userID.setObjectName("pushButton_userID")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def set_button(self, state):  # 设置按钮是否可用
        self.pushButton_gold.setEnabled(state)
        self.pushButton_goldM.setEnabled(state)
        self.pushButton_point.setEnabled(state)
        self.pushButton_pointM.setEnabled(state)
        self.pushButton_sound.setEnabled(state)
        self.pushButton_soundM.setEnabled(state)
        self.pushButton_stage.setEnabled(state)
        self.pushButton_skin.setEnabled(state)
        self.pushButton_volume.setEnabled(state)
        self.pushButton_volumeM.setEnabled(state)
        self.pushButton_friend.setEnabled(state)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_userID.setText(_translate("Dialog", "输入用户ID："))
        self.label_point.setText(_translate("Dialog", "积分数量："))
        self.pushButton_point.setText(_translate("Dialog", "查询"))
        self.pushButton_pointM.setText(_translate("Dialog", "修改"))
        self.label_pointM.setText(_translate("Dialog", "修改积分："))
        self.pushButton_gold.setText(_translate("Dialog", "查询"))
        self.label_gold.setText(_translate("Dialog", "金币数量："))
        self.pushButton_goldM.setText(_translate("Dialog", "修改"))
        self.label_goldM.setText(_translate("Dialog", "修改金币："))
        self.label_1.setText(_translate("Dialog", "积分金币查询"))
        self.pushButton_sound.setText(_translate("Dialog", "查询"))
        self.pushButton_volumeM.setText(_translate("Dialog", "修改"))
        self.pushButton_volume.setText(_translate("Dialog", "查询"))
        self.label_volume.setText(_translate("Dialog", "音效大小："))
        self.label_volumeM.setText(_translate("Dialog", "修改音效："))
        self.label_2.setText(_translate("Dialog", "音量音效查询"))
        self.label_soundM.setText(_translate("Dialog", "修改音量："))
        self.label_sound.setText(_translate("Dialog", "音量大小："))
        self.pushButton_soundM.setText(_translate("Dialog", "修改"))
        self.label_3.setText(_translate("Dialog", "好友数据查询"))
        self.pushButton_friend.setText(_translate("Dialog", "查询"))
        self.label_friend.setText(_translate("Dialog", "好友查询："))
        self.label_4.setText(_translate("Dialog", "皮肤道具查询"))
        self.pushButton_stage.setText(_translate("Dialog", "查询"))
        self.label_stage.setText(_translate("Dialog", "道具数量："))
        self.label_skin.setText(_translate("Dialog", "皮肤数据："))
        self.pushButton_skin.setText(_translate("Dialog", "查询"))
        self.pushButton_userID.setText(_translate("Dialog", "确认"))
        self.set_button(False)  # 设置按钮不可用
        self.pushButton_userID.clicked.connect(self.get_gamer_data)  # 连接槽函数

        self.pushButton_gold.clicked.connect(self.get_gold)  # 连接槽函数
        self.pushButton_goldM.clicked.connect(self.modify_gold)  # 连接槽函数
        self.pushButton_point.clicked.connect(self.get_point)  # 连接槽函数
        self.pushButton_pointM.clicked.connect(self.modify_point)  # 连接槽函数
        self.pushButton_sound.clicked.connect(self.get_sound)  # 连接槽函数
        self.pushButton_soundM.clicked.connect(self.modify_sound)  # 连接槽函数
        self.pushButton_volume.clicked.connect(self.get_volume)  # 连接槽函数
        self.pushButton_volumeM.clicked.connect(self.modify_volume)  # 连接槽函数
        self.pushButton_friend.clicked.connect(self.get_friend)  # 连接槽函数
        self.pushButton_stage.clicked.connect(self.get_stage)  # 连接槽函数
        self.pushButton_skin.clicked.connect(self.get_skin)  # 连接槽函数

    def get_gamer_data(self):
        # 826向服务器发送登陆请求，返回得到账号是否存在
        tcp_client_socket.send("826 " + self.administratorsID + " " + self.lineEdit_userID.text())
        data_list_827 = tcp_client_socket.rec().split()
        if data_list_827[0] == "827":
            if data_list_827[1] == "0":  # 账号不存在
                reply = QMessageBox.about(self.form, "提示", "您输入的账号不存在！请重新输入")
            elif data_list_827[1] == "1":  # 账号存在
                reply = QMessageBox.about(self.form, "提示", "用户ID输入正确！正在获取用户信息")
                self.set_button(True)  # 设置按钮可用

                self.userID = self.lineEdit_userID.text()  # 获取账号

                # 828请求获取 金币积分 音量音效 正在使用的皮肤
                tcp_client_socket.send("828 " + self.administratorsID + " " + self.userID)
                userData_list = tcp_client_socket.rec().split()
                self.point = userData_list[3]
                self.gold = userData_list[4]
                self.sound = userData_list[5]
                self.volume = userData_list[6]
                self.skin_url = userData_list[7]

                # 830请求获取 好友数据
                tcp_client_socket.send("830 " + self.administratorsID + " " + self.userID)
                data_list_831 = tcp_client_socket.rec().split("@")
                self.friend_list = json.loads(data_list_831[1])

                # 832请求获取 皮肤道具 信息
                tcp_client_socket.send("832 " + self.administratorsID + " " + self.userID)
                userData_list = tcp_client_socket.rec().split()
                if userData_list[0] == "833":
                    self.toolsquantity = userData_list[2]
                    self.skin_url_list = []

                    for i in range(len(userData_list) - 3):
                        self.skin_url_list.append(userData_list[i + 3])
                        urllib.request.urlretrieve(self.skin_url_list[i],
                                                   filename=self.path + '/bag_skin' + str(i) + '.jpg')  # 下载图片"""

            else:  # 通信出错
                reply = QMessageBox.about(self.form, "提示", "服务器出错")
        else:
            reply = QMessageBox.about(self.form, "提示", "服务器出错")

    def get_gold(self):  # 显示金币
        self.lineEdit_gold.setText(self.gold)

    def get_point(self):  # 显示积分
        self.lineEdit_point.setText(self.point)

    def get_sound(self):  # 显示音量
        self.lineEdit_sound.setText(self.sound)

    def get_volume(self):  # 显示音效
        self.lineEdit_volume.setText(self.volume)

    def get_friend(self):  # 显示好友列表
        friend_Num = len(self.friend_list)
        self.tableWidget_friend.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_friend.setColumnCount(3)
        self.tableWidget_friend.setRowCount(friend_Num)
        for i in range(friend_Num):  # 好友数=行数
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_friend.setVerticalHeaderItem(i, item)

        for i in range(3):  # 用户名、积分、金币三列
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
            self.tableWidget_friend.setHorizontalHeaderItem(i, item)

        for i in range(friend_Num):
            for j in range(3):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_friend.setItem(i, j, item)

        self.tableWidget_friend.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_friend.horizontalHeader().setDefaultSectionSize(98)
        self.tableWidget_friend.horizontalHeader().setMinimumSectionSize(24)
        self.tableWidget_friend.setSelectionBehavior(QAbstractItemView.SelectRows)

        for i in range(friend_Num):
            item = self.tableWidget_friend.verticalHeaderItem(i)
            item.setText(str(i + 1))

        item = self.tableWidget_friend.horizontalHeaderItem(0)
        item.setText("用户名")
        item = self.tableWidget_friend.horizontalHeaderItem(1)
        item.setText("积分")
        item = self.tableWidget_friend.horizontalHeaderItem(2)
        item.setText("金币")

        __sortingEnabled = self.tableWidget_friend.isSortingEnabled()
        self.tableWidget_friend.setSortingEnabled(False)
        self.tableWidget_friend.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(friend_Num):
            for j in range(3):
                item = self.tableWidget_friend.item(i, j)
                item.setText(str(self.friend_list[i][j + 1]))

        self.tableWidget_friend.setSortingEnabled(__sortingEnabled)

    def get_stage(self):  # 显示道具数量
        self.lineEdit_stage.setText(self.toolsquantity)

    def get_skin(self):  # 显示皮肤
        # 把皮肤信息写入listwidget
        for i in range(len(self.skin_url_list)):
            # 设置每行要加入的控件
            if self.skin_url_list[i] == self.skin_url:
                rank_button = QtWidgets.QPushButton(str(i + 1) + "(正在使用)")
            else:
                rank_button = QtWidgets.QPushButton(str(i + 1))

            rank_button.setFlat(True)
            rank_button.setMinimumSize(50, 100)

            picture_button = QtWidgets.QPushButton()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.path + "/bag_skin" + str(i) + ".jpg"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            picture_button.setIcon(icon)
            picture_button.setIconSize(QtCore.QSize(150, 100))
            picture_button.setFlat(True)

            # 设置每一行的布局
            layout = FlowLayout()
            layout.addWidget(rank_button)
            layout.addWidget(picture_button)

            # 给每一行加入上面的布局
            widget = QtWidgets.QDialog(self.listWidget_skin)
            item = QtWidgets.QListWidgetItem(self.listWidget_skin)
            item.setSizeHint(QSize(301, 140))

            widget.setLayout(layout)
            self.listWidget_skin.addItem(item)
            self.listWidget_skin.setItemWidget(item, widget)

    def modify_gold(self):  # 修改金币
        # 向服务器请求修改数据
        if self.lineEdit_goldM.text().isdigit():
            if int(self.lineEdit_goldM.text()) >= 0:
                tcp_client_socket.send(
                    "802 " + self.administratorsID + " " + self.lineEdit_goldM.text() + " " + "2" + " " + self.lineEdit_userID.text())
                data_list = tcp_client_socket.rec().split()
                if data_list[1] == '1':
                    self.gold = self.lineEdit_goldM.text()
                    reply = QMessageBox.about(self.form, "提示", "修改成功")
                else:
                    reply = QMessageBox.about(self.form, "提示", "修改失败")
            else:
                reply = QMessageBox.about(self.form, "提示", "您输入的数小于0！请重新输入")
        else:
            reply = QMessageBox.about(self.form, "提示", "您输入的不是正整数！请重新输入")

    def modify_point(self):  # 修改积分
        # 向服务器请求修改数据
        if self.lineEdit_pointM.text().isdigit():
            if int(self.lineEdit_pointM.text()) >= 0:
                tcp_client_socket.send(
                    "802 " + self.administratorsID + " " + self.lineEdit_pointM.text() + " " + "1" + " " + self.lineEdit_userID.text())
                data_list = tcp_client_socket.rec().split()
                if data_list[1] == '1':
                    self.point = self.lineEdit_pointM.text()
                    reply = QMessageBox.about(self.form, "提示", "修改成功")
                else:
                    reply = QMessageBox.about(self.form, "提示", "修改失败")
            else:
                reply = QMessageBox.about(self.form, "提示", "您输入的数小于0！请重新输入")
        else:
            reply = QMessageBox.about(self.form, "提示", "您输入的不是正整数！请重新输入")

    def modify_sound(self):  # 修改音量
        # 向服务器请求修改数据
        if self.lineEdit_soundM.text().isdigit():
            if int(self.lineEdit_soundM.text()) >= 0 and int(self.lineEdit_soundM.text()) <= 100:
                tcp_client_socket.send(
                    "802 " + self.administratorsID + " " + self.lineEdit_soundM.text() + " " + "3" + " " + self.lineEdit_userID.text())
                data_list = tcp_client_socket.rec().split()
                if data_list[1] == '1':
                    self.sound = self.lineEdit_soundM.text()
                    reply = QMessageBox.about(self.form, "提示", "修改成功")
                else:
                    reply = QMessageBox.about(self.form, "提示", "修改失败")
            else:
                reply = QMessageBox.about(self.form, "提示", "您输入的数不在0-100间！请重新输入")
        else:
            reply = QMessageBox.about(self.form, "提示", "您输入的不是整数！请重新输入")

    def modify_volume(self):  # 修改音效
        # 向服务器请求修改数据
        if self.lineEdit_volumeM.text().isdigit():
            if int(self.lineEdit_volumeM.text()) >= 0 and int(self.lineEdit_volumeM.text()) <= 100:
                tcp_client_socket.send(
                    "802 " + self.administratorsID + " " + self.lineEdit_volumeM.text() + " " + "4" + " " + self.lineEdit_userID.text())
                data_list = tcp_client_socket.rec().split()
                if data_list[1] == '1':
                    self.volume = self.lineEdit_volumeM.text()
                    reply = QMessageBox.about(self.form, "提示", "修改成功")
                else:
                    reply = QMessageBox.about(self.form, "提示", "修改失败")
            else:
                reply = QMessageBox.about(self.form, "提示", "您输入的数不在0-100间！请重新输入")
        else:
            reply = QMessageBox.about(self.form, "提示", "您输入的不是整数！请重新输入")
