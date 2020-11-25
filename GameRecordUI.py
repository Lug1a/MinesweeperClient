import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QListWidget
from QDialog import myDialog
from TcpClient import tcp_client_socket



class Ui_Dialog(object):
    def setupUi(self, Dialog, adminID, userID, recordData):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 650)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setStyleSheet("#Dialog{background-color: gainsboro;\n"
                             "border-image: url(" + "icon/personal.jpg);}")

        self.form = Dialog
        self.adminID = adminID
        self.userID = userID
        self.exploits_list = recordData

        self.userID_label = QtWidgets.QLabel(Dialog)
        self.userID_label.setGeometry(QtCore.QRect(30, 30, 170, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("华文细黑")
        self.userID_label.setFont(font)

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 130, 640, 461))
        self.listWidget.setFrameShape(QListWidget.NoFrame)  # 设置无边框
        self.listWidget.setStyleSheet("background-color:  transparent; ")  # 设置背景透明

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
        Dialog.setWindowTitle(_translate("Dialog", "战绩查询"))
        self.userID_label.setText(_translate("Dialog", "账号:" + self.userID))

        self.signle_label.setText(_translate("Form", "单人游戏战绩"))
        self.double_label.setText(_translate("Form", "匹配对战战绩"))

if __name__ == "__main__":

    exploits_list = [[0, "初级", 120, 0.9812, 20.23, 0.8923], [0, "中级", 23, 0.9812, 20.00, 0.8923],
                     [0, "高级", 13, 0.9812, 20.23, 0.8923], [0, "大师", 6, 0.9812, 20, 0.8923],
                     [1, "初级", 15, 0.9812, 20.23, 0.8923], [1, "中级", 26, 0.9812, 20.23, 0.8923],
                     [1, "高级", 72, 0.9812, 20.23, 0.8923], [1, "大师", 48, 0.9812, 20.23, 0.8923]]

    app = QApplication(sys.argv)
    form = myDialog()
    ui = Ui_Dialog()
    ui.setupUi(form, 1111111, "用户123", exploits_list)
    form.show()
    app.exec_()
    sys.exit()