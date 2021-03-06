# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import json
from QDialog import myDialog
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QHeaderView, QListWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from TcpClient import tcp_client_socket


class Ui_Dialog(object):
    def setupUi(self, Dialog, oldDialog,adminID):
        self.Dialog = Dialog
        self.oldDialog = oldDialog
        self.adminID = adminID
        Dialog.setObjectName("Dialog")
        Dialog.resize(273, 230)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(58, 180, 160, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 81, 31))
        self.label_3.setObjectName("label_3")
        self.UserName = QtWidgets.QLineEdit(Dialog)
        self.UserName.setGeometry(QtCore.QRect(120, 30, 123, 30))
        self.UserName.setObjectName("UserName")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(120, 80, 123, 30))
        self.password.setObjectName("password")
        self.checkPassword = QtWidgets.QLineEdit(Dialog)
        self.checkPassword.setGeometry(QtCore.QRect(120, 130, 123, 30))
        self.checkPassword.setObjectName("checkPassword")

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.checkPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.addAdministrator)
        self.buttonBox.rejected.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加管理员"))
        self.label.setText(_translate("Dialog", "用户名："))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.label_3.setText(_translate("Dialog", "确认密码："))

    def addAdministrator(self):
        if len(self.password.text()) < 6:
            self.password.setText("")
            QMessageBox.about(self.Dialog, "提示", "您输入的当前密码长度小于6！请重新输入")

        elif len(self.password.text()) >= 6:
            if self.password.text() != self.checkPassword.text():
                self.password.setText("")
                self.checkPassword.setText("")
                QMessageBox.about(self.Dialog, "提示", "确认密码与新密码不一致，请重新输入！")

            elif self.password.text() == self.checkPassword.text():
                 # 向服务器请求添加管理员
                tcp_client_socket.send(
                    "820 " + self.adminID + ' ' + str(self.UserName.text()) + ' ' + str(self.password.text()))
                data_list_821 = tcp_client_socket.rec().split(" ")
                QMessageBox.about(self.Dialog, "提示", "创建管理员成功！\n\n管理员ID为： "
                                  + data_list_821[1] + "\n管理员用户名为： "
                                  + self.UserName.text() +"\n密码为： " + self.password.text())
                self.Dialog.close()
                self.oldDialog.close()