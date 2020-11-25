# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PersonalInterfaceUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QListWidget

from TcpClient import tcp_client_socket



class Ui_Dialog(object):
    def setupUi(self, Dialog, my_userID, other_people, userID, username, point, gold, exploits_list, is_friend):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 650)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setStyleSheet("#Dialog{background-color: gainsboro;\n"
                             "border-image: url(" + "icon/personal.jpg);}")

        self.form = Dialog
        self.my_userID = my_userID
        self.other_people = other_people
        self.userID = userID
        self.username = username
        self.point = point
        self.gold = gold
        self.exploits_list = exploits_list
        self.is_friend = is_friend
        self.flag = 0

        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(30, 30, 500, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("华文细黑")
        self.username_label.setFont(font)

        self.userID_label = QtWidgets.QLabel(Dialog)
        self.userID_label.setGeometry(QtCore.QRect(30, 70, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("华文细黑")
        self.userID_label.setFont(font)

        self.point_label = QtWidgets.QLabel(Dialog)
        self.point_label.setGeometry(QtCore.QRect(550, 30, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("华文细黑")
        self.point_label.setFont(font)

        self.gold_label = QtWidgets.QLabel(Dialog)
        self.gold_label.setGeometry(QtCore.QRect(550, 70, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("华文细黑")
        self.gold_label.setFont(font)

        if self.other_people == 1:
            self.addfirend_button = QtWidgets.QPushButton(Dialog)
            if self.is_friend == "0":
                self.addfirend_button.setText("添加好友")
            elif self.is_friend == "1":
                self.addfirend_button.setText("删除好友")
            else:
                self.addfirend_button.setText("等待回应")
                self.addfirend_button.setEnabled(False)

            self.addfirend_button.setGeometry(QtCore.QRect(550, 105, 100, 30))
            self.addfirend_button.setStyleSheet(
                "QPushButton { background-color: rgb(125, 127, 255);"
                " border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setFamily("华文细黑")
            self.addfirend_button.setFont(font)

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 130, 640, 461))
        self.listWidget.setFrameShape(QListWidget.NoFrame)  # 设置无边框
        self.listWidget.setStyleSheet("background-color:  transparent; ")  # 设置背景透明

        # 不显示滚动条
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        signle_list = []
        double_list = []
        # 找出单人和多人的战绩表
        for i in range(len(self.exploits_list)):
            if 0 == self.exploits_list[i][0]:
                signle_list.append(self.exploits_list[i])
            elif 1 == self.exploits_list[i][0]:
                double_list.append(self.exploits_list[i])


        # 对单人游戏（0）和匹配对战（1）战绩进行显示
        self.signle_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(25)
        self.signle_label.setFont(font)
        self.signle_label.setAlignment(QtCore.Qt.AlignCenter)

        item = QtWidgets.QListWidgetItem(self.listWidget)
        item.setSizeHint(QSize(600, 125))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, self.signle_label)
        for i in range(len(signle_list)):
            self.widget = QtWidgets.QWidget(Dialog)
            self.gridLayout = QtWidgets.QGridLayout(self.widget)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setObjectName("gridLayout")

            self.level_name = QtWidgets.QLabel(self.widget)
            font = QtGui.QFont()
            font.setFamily("幼圆")
            font.setPointSize(15)
            self.level_name.setFont(font)
            self.level_name.setObjectName("label_2")
            self.gridLayout.addWidget(self.level_name, 0, 0, 1, 1)

            self.game_frequency = QtWidgets.QLabel(self.widget)
            self.game_frequency.setObjectName("label")
            self.gridLayout.addWidget(self.game_frequency, 0, 1, 1, 1)

            self.success_rate = QtWidgets.QLabel(self.widget)
            self.success_rate.setObjectName("label_3")
            self.gridLayout.addWidget(self.success_rate, 0, 2, 1, 1)

            self.time = QtWidgets.QLabel(self.widget)
            self.time.setObjectName("label_5")
            self.gridLayout.addWidget(self.time, 1, 1, 1, 1)
            self.completion_rate = QtWidgets.QLabel(self.widget)
            self.completion_rate.setObjectName("label_4")
            self.gridLayout.addWidget(self.completion_rate, 1, 2, 1, 1)
            self.level_name.setText(signle_list[i][1])
            self.game_frequency.setText("游戏次数：" + str(signle_list[i][2]) + '次')
            self.success_rate.setText("成功率：{:.2f}".format(signle_list[i][3] * 100) + '%')
            self.time.setText("每局时长：{:.2f}".format(signle_list[i][4]) + '秒')
            self.completion_rate.setText("平均完成度：{:.2f}".format(signle_list[i][5] * 100) + '%')
            item = QtWidgets.QListWidgetItem(self.listWidget)
            item.setSizeHint(QSize(600, 125))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, self.widget)


        self.double_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(25)
        self.double_label.setFont(font)
        self.double_label.setAlignment(QtCore.Qt.AlignCenter)

        item = QtWidgets.QListWidgetItem(self.listWidget)
        item.setSizeHint(QSize(600, 125))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, self.double_label)

        for i in range(len(double_list)):
            self.widget = QtWidgets.QWidget(Dialog)
            self.gridLayout = QtWidgets.QGridLayout(self.widget)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setObjectName("gridLayout")

            self.level_name = QtWidgets.QLabel(self.widget)
            font = QtGui.QFont()
            font.setFamily("幼圆")
            font.setPointSize(15)
            self.level_name.setFont(font)
            self.level_name.setObjectName("label_2")
            self.gridLayout.addWidget(self.level_name, 0, 0, 1, 1)

            self.game_frequency = QtWidgets.QLabel(self.widget)
            self.game_frequency.setObjectName("label")
            self.gridLayout.addWidget(self.game_frequency, 0, 1, 1, 1)

            self.success_rate = QtWidgets.QLabel(self.widget)
            self.success_rate.setObjectName("label_3")
            self.gridLayout.addWidget(self.success_rate, 0, 2, 1, 1)

            self.time = QtWidgets.QLabel(self.widget)
            self.time.setObjectName("label_5")
            self.gridLayout.addWidget(self.time, 1, 1, 1, 1)
            self.completion_rate = QtWidgets.QLabel(self.widget)
            self.completion_rate.setObjectName("label_4")
            self.gridLayout.addWidget(self.completion_rate, 1, 2, 1, 1)
            self.level_name.setText(double_list[i][1])
            self.game_frequency.setText("游戏次数：" + str(double_list[i][2]) + '次')
            self.success_rate.setText("成功率：{:.2f}".format(double_list[i][3] * 100) + '%')
            self.time.setText("每局时长：{:.2f}".format(double_list[i][4]) + '秒')
            self.completion_rate.setText("平均完成度：{:.2f}".format(double_list[i][5] * 100) + '%')
            item = QtWidgets.QListWidgetItem(self.listWidget)
            item.setSizeHint(QSize(600, 125))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, self.widget)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "个人界面"))
        self.username_label.setText(_translate("Dialog", "用户名:" + self.username))
        self.userID_label.setText(_translate("Dialog", "账号:" + self.userID))
        self.point_label.setText(_translate("Dialog", "积分:" + self.point))
        self.gold_label.setText(_translate("Dialog", "金币:" + self.gold))
        self.signle_label.setText(_translate("Form", "单人游戏战绩"))
        self.double_label.setText(_translate("Form", "匹配对战战绩"))
        if self.other_people == 1:
            self.addfirend_button.clicked.connect(partial(self.operate_friend, self.addfirend_button.text()))  # 连接槽函数

    def operate_friend(self, text):
        if text == "添加好友":
            tcp_client_socket.send("602 "
                                   + self.my_userID + ' '
                                   + self.userID + ' '
                                   + str(0))
            success = tcp_client_socket.rec().split()

            if success[1] == "1":
                self.addfirend_button.setText("等待回应")
                self.addfirend_button.setEnabled(False)

        elif text == "删除好友":
            tcp_client_socket.send("602 "
                                   + self.my_userID + ' '
                                   + self.userID + ' '
                                   + str(1))
            success = tcp_client_socket.rec().split()
            if success[1] == "1":
                self.addfirend_button.setText("添加好友")
                self.addfirend_button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(form, 1, "10234879", "username", "10020", "2036",
               [[0, "初级", 120, 0.9812, 20.23, 0.8923], [0, "中级", 23, 0.9812, 20.00, 0.8923],
                [0, "高级", 13, 0.9812, 20.23, 0.8923], [0, "大师", 6, 0.9812, 20, 0.8923],
                [1, "初级", 15, 0.9812, 20.23, 0.8923], [1, "中级", 26, 0.9812, 20.23, 0.8923],
                [1, "高级", 72, 0.9812, 20.23, 0.8923], [1, "大师", 48, 0.9812, 20.23, 0.8923]])
    form.show()
    sys.exit(app.exec_())
