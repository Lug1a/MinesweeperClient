# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'applyList.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView
from TcpClient import tcp_client_socket
from QDialog import myDialog



class Ui_Dialog(object):
    def setupUi(self, Dialog, userID, num, applylist):
        self.userID = userID
        self.num = num
        self.applylist = applylist

        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 395)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setStyleSheet("#Dialog{background-color: gainsboro;\n"
                             "border-image: url(" + "icon/personal.jpg);}")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 381, 321))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(self.num)

        #num行申请好友
        for i in range(self.num):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        #固定的三列
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        for i in range(self.num):
            for j in range(3):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(118)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 10, 111, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.tableWidget.cellClicked['int','int'].connect(self.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "申请列表"))

        for i in range(self.num):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Dialog", str(i+1)))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for i in range(self.num):
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Dialog", str(self.applylist[i][0])))

            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Dialog", "同意"))

            item = self.tableWidget.item(i, 2)
            item.setText(_translate("Dialog", "拒绝"))

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "好友申请列表"))

    def click(self, x, y):
        if y == 1:#加好友
            tcp_client_socket.send("602 " + str(self.userID) + " " + str(self.applylist[x][1]) + " " + str(2))
            data_list_601 = tcp_client_socket.rec().split()
            if data_list_601[1] == '1':
                del self.applylist[x]
                self.tableWidget.removeRow(x)

        elif y == 2:#删好友
            tcp_client_socket.send("602 " + str(self.userID) + " " + str(self.applylist[x][1]) + " " + str(1))
            data_list_601 = tcp_client_socket.rec().split()
            if data_list_601[1] == '1':
                del self.applylist[x]
                self.tableWidget.removeRow(x)

if __name__ == "__main__":
    #test
    userID=123123
    num=3
    applylist=[["小吕", 111111],["小红",2222222],["小黑",333333]]
    #test

    app = QApplication(sys.argv)
    form = myDialog()
    ui = Ui_Dialog()
    ui.setupUi(form, userID, num, applylist)
    form.show()
    app.exec_()
    sys.exit()