# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RankList.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import json
import sys
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QApplication, QListWidget, QMessageBox
from FlowLayout import FlowLayout
from QDialog import myDialog
from TcpClient import tcp_client_socket
from PersonalInterfaceUI import Ui_Dialog as Personalinterface_Dialog


class Ui_Dialog(object):
    def setupUi(self, Dialog, selfID, rank_list):
        self.form = Dialog
        self.selfID = selfID
        self.rank_list = rank_list
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 900)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(25)
        Dialog.setFont(font)
        Dialog.setStyleSheet("#Dialog{background-color: gainsboro;\n"
                             "border-image: url(" + "icon/rank.jpg);}")

        # class ListWidget(QListWidget):
        #     def clicked(self, item):
        #         print(item)
        #         print(item.text())

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QRect(105, 300, 496, 560))  # 设置大小
        self.listWidget.setFrameShape(QListWidget.NoFrame)  # 设置无边框
        self.listWidget.setStyleSheet("background-color:  transparent; ")  # 设置背景透明

        # 最顶上加上  排名，用户名，积分  3个标签
        self.rank_label = QtWidgets.QLabel(Dialog)
        self.name_label = QtWidgets.QLabel(Dialog)
        self.point_label = QtWidgets.QLabel(Dialog)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.rank_label.setFont(font)
        self.name_label.setFont(font)
        self.point_label.setFont(font)

        self.rank_label.setGeometry(QtCore.QRect(148, 265, 50, 30))
        self.name_label.setGeometry(QtCore.QRect(318, 265, 50, 30))
        self.point_label.setGeometry(QtCore.QRect(503, 265, 50, 30))

        # 把排行信息写入listwidget
        for i in range(len(self.rank_list)):
            # 设置每行要加入的控件
            rank_button = QtWidgets.QPushButton(str(i + 1))
            rank_button.setFlat(True)
            rank_button.setMinimumSize(50, 30)
            rank_button.clicked.connect(partial(self.clicked, i))  # 绑定点击事件
            name_button = QtWidgets.QPushButton(rank_list[i][1])
            name_button.setFlat(True)
            name_button.setMinimumSize(250, 30)
            name_button.clicked.connect(partial(self.clicked, i))  # 绑定点击事件
            point_button = QtWidgets.QPushButton(rank_list[i][2])
            point_button.setFlat(True)
            point_button.setMinimumSize(50, 30)
            point_button.clicked.connect(partial(self.clicked, i))  # 绑定点击事件

            # 设置每一行的布局
            layout = FlowLayout()
            layout.addWidget(rank_button)
            layout.addWidget(name_button)
            layout.addWidget(point_button)

            # 给每一行加入上面的布局
            widget = QtWidgets.QDialog(self.listWidget)
            item = QtWidgets.QListWidgetItem(self.listWidget)
            item.setSizeHint(QSize(350, 50))

            item.setText(str(i))
            font = QtGui.QFont()
            font.setPointSize(1)
            item.setFont(font)

            widget.setLayout(layout)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

        # 不显示滚动条
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "积分排行榜"))
        self.rank_label.setText(_translate("Dialog", "排名"))
        self.name_label.setText(_translate("Dialog", "用户名"))
        self.point_label.setText(_translate("Dialog", "积分"))
        self.listWidget.itemClicked.connect(self.clicked)  # 绑定点击事件

    def clicked(self, i):
        if isinstance(i, int):
            userID = self.rank_list[i][0]
        else:
            userID = self.rank_list[int(i.text())][0]

        self.form.setEnabled(False)

        # 向服务器请求个人战绩数据
        tcp_client_socket.send("206 " + self.selfID + " " + userID)
        data_list_207 = tcp_client_socket.rec().split("@")
        self.exploits_list = json.loads(data_list_207[5])

        form1 = myDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = Personalinterface_Dialog()

        # 判断是否是自己
        if self.selfID == userID:
            ui.setupUi(form1, self.selfID, 0, data_list_207[1], data_list_207[2], data_list_207[3], data_list_207[4],
                       self.exploits_list, data_list_207[6])
        else:
            ui.setupUi(form1, self.selfID, 1, data_list_207[1], data_list_207[2], data_list_207[3], data_list_207[4],
                       self.exploits_list, data_list_207[6])

        form1.sound = self.form.sound  # 设置音效音量
        form1.show()
        form1.exec_()
        self.form.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
