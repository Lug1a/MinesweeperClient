# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameMessage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import json
import threading
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

# 消息窗体,message为窗体的title和提示信息，如["提示信息","本局游戏已结束"],窗口将在5s内关闭
from TcpClient import tcp_client_socket


class Ui_Dialog(object):
    def setupUi(self, Dialog, message):
        self.message = message
        self.dialog = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 93)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 50, 81, 28))
        self.pushButton.setObjectName("pushButton")

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeCount)
        self.timer.start()
        self.time = 5

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.message[0]))
        self.label.setText(_translate("Dialog", self.message[1]))
        self.pushButton.setText(_translate("Dialog", "确认(" + str(self.time) + ")"))
        self.pushButton.clicked.connect(self.close_dialog)  # 连接槽函数

    def close_dialog(self):
        self.dialog.close()

    def timeCount(self):
        self.time -= 1
        self.pushButton.setText("确认(" + str(self.time) + ")")
        if self.time == 0:
            self.close_dialog()


# 等待窗体
class Wait_Dialog(object):
    def setupUi(self, Dialog, userID, point, diffculty, username):
        self.dialog = Dialog
        self.userID = userID

        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 93)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStrikeOut(False)
        self.label.setFont(font)

        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 50, 81, 28))
        self.pushButton.setObjectName("pushButton")

        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timeCount)
        self.timer.start()
        self.dot = 3

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.match = 0
        t = threading.Thread(target=self.request, args=(userID, point, diffculty, username))
        t.start()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "等待"))
        self.label.setText(_translate("Dialog", "匹配已开始，请等待..."))
        self.pushButton.setText(_translate("Dialog", "取消匹配"))
        self.pushButton.clicked.connect(self.cancel)  # 连接槽函数

    # 向服务器请求匹配对局
    def request(self, userID, point, diffculty, username):
        tcp_client_socket.send("208 "
                               + userID + ' '
                               + point + ' '
                               + str(diffculty) + ' '
                               + username)
        while True:
            data = tcp_client_socket.rec()

            if not data:
                continue
            data_list = data.split(" ")
            if data_list[0] == "209":
                self.dialog.if_close = 1
                self.data_list = data_list
                if data_list[1] == '1':
                    sleep(0.15)  # 等待0.15s，否则快速关闭程序，程序会崩溃
                    self.match = 1
                    self.enemy_username = data_list[2]
                    self.enemy_point = data_list[3]
                    self.timer.stop()
                    self.label.setText("匹配成功，对手是" + self.enemy_username + "，积分为" + self.enemy_point)
                self.dialog.close()
                break

    def cancel(self):
        tcp_client_socket.send("208a " + self.userID)  # 向服务器请求取消匹配

    def timeCount(self):
        self.dot += 1
        # 加点
        str = ''
        for i in range(self.dot % 4):
            str += '.'
        self.label.setText("匹配已开始，请等待" + str)

    def get_match(self):
        return self.match
