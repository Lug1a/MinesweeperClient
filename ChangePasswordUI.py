import sys
import json
from QDialog import myDialog
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QHeaderView, QListWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from TcpClient import tcp_client_socket




class Ui_dialog(object):
    def setupUi(self, dialog, UserID):
        self.UserID = UserID
        self.Dialog = dialog

        dialog.setObjectName("dialog")
        dialog.resize(273, 206)
        dialog.setStyleSheet("#Dialog{background-color: gainsboro;\n"
                             "border-image: url(icon/login.jpg);}")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 160, 71, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 71, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(dialog)
        self.pushButton.clicked.connect(self.click)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "更改密码"))
        self.pushButton.setText(_translate("dialog", "确认"))
        self.label.setText(_translate("dialog", "当前密码："))
        self.label_2.setText(_translate("dialog", "更改密码："))
        self.label_3.setText(_translate("dialog", "确认密码："))

    def click(self):#点击确认更改密码
        if len(self.lineEdit.text()) < 6:
            self.lineEdit.setText("")
            QMessageBox.about(self.Dialog, "提示", "您输入的当前密码长度小于6！请重新输入")

        elif len(self.lineEdit.text()) >= 6:
            if self.lineEdit_2.text() != self.lineEdit_3.text():
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                QMessageBox.about(self.Dialog, "提示", "确认密码与新密码不一致，请重新输入！")

            elif self.lineEdit_2.text() == self.lineEdit_3.text():
                if len(self.lineEdit_2.text()) < 6:
                    self.lineEdit_2.setText("")
                    self.lineEdit_3.setText("")
                    QMessageBox.about(self.Dialog, "提示", "新密码长度小于6，请重新输入！")

                elif len(self.lineEdit_2.text()) >= 6:
                    # 向服务器请求更改密码
                    tcp_client_socket.send(
                        "702 " + self.UserID + ' ' + str(self.lineEdit.text()) + ' ' + str(self.lineEdit_2.text()))
                    data_list_703 = tcp_client_socket.rec()

                    if data_list_703 == "703a":
                        QMessageBox.about(self.Dialog, "提示", "密码修改成功！")
                        self.Dialog.close()
                    elif data_list_703 == "703b":
                        self.lineEdit.setText("")
                        self.lineEdit_2.setText("")
                        self.lineEdit_3.setText("")
                        QMessageBox.about(self.Dialog, "提示", "当前密码错误，请重新输入！")

