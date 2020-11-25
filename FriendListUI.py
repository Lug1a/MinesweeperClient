# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import json
from QDialog import myDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView
from TcpClient import tcp_client_socket
from PersonalInterfaceUI import Ui_Dialog as Personalinterface_Dialog
from ApplyListUI import Ui_Dialog as ApplyList_Dialog


class Ui_dialog(object):
    def setupUi(self, dialog, userID, friend_Num, friend_List):
        self.form = dialog
        self.friend_list = friend_List
        self.userID = userID
        dialog.setObjectName("dialog")
        dialog.resize(403, 500)
        dialog.setFixedSize(dialog.width(), dialog.height())
        dialog.setStyleSheet("#dialog{background-color: gainsboro;\n"
                             "border-image: url(" + "icon/personal.jpg);}")

        self.gridLayoutWidget = QtWidgets.QWidget(dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 361, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.verticalHeader().setVisible(False)#隐藏垂直表头

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(friend_Num)

        for i in range(friend_Num):  # 好友数=行数
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        for i in range(3):  # 用户名、积分、金币三列
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
            self.tableWidget.setHorizontalHeaderItem(i, item)

        for i in range(friend_Num):
            for j in range(3):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(98)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(24)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 450, 78, 33))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(164, 10, 81, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(dialog, friend_Num, friend_List)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget.cellClicked.connect(self.clicked)
        self.pushButton.clicked.connect(self.applyList)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog, friend_Num, friend_List):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "好友列表"))

        for i in range(friend_Num):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("dialog", str(i + 1)))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dialog", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dialog", "积分"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dialog", "金币"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(friend_Num):
            for j in range(3):
                item = self.tableWidget.item(i, j)
                item.setText(_translate("dialog", str(friend_List[i][j + 1])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("dialog", "申请列表"))
        self.label.setText(_translate("dialog", "好友列表"))

    def clicked(self, i):  # 点击排行榜上的用户跳转到个人战绩
        userID = self.friend_list[i][0]
        self.form.setEnabled(False)

        # 向服务器请求个人战绩数据
        tcp_client_socket.send("206 " + self.userID + " " + userID)
        data_list_207 = tcp_client_socket.rec().split("@")
        exploits_list = json.loads(data_list_207[5])

        form1 = myDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = Personalinterface_Dialog()
        ui.setupUi(form1, self.userID, 1, data_list_207[1], data_list_207[2], data_list_207[3],
                   data_list_207[4], exploits_list, data_list_207[6])

        form1.sound = self.form.sound  # 设置音效音量'''

        form1.show()
        form1.exec_()
        self.form.setEnabled(True)

    def applyList(self):  # 点击查看申请列表
        self.form.setEnabled(False)
        # 向服务器请求申请列表数据
        tcp_client_socket.send("604 " + self.userID)
        data_list_605 = tcp_client_socket.rec().split("@")
        apply_list = json.loads(data_list_605[1])

        form1 = myDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = ApplyList_Dialog()
        ui.setupUi(form1, self.userID, len(apply_list), apply_list)

        form1.sound = self.form.sound  # 设置音效音量'''

        form1.show()
        form1.exec_()
        self.form.setEnabled(True)