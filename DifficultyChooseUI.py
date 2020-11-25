# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DifficultyChoose.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from MineSweeperUI import MineSweeperUI
from QDialog import MineDialog


# 点击开始游戏和匹配游戏后显示的窗口，将要求玩家选择游戏难度，难度级别的数量将根据level_data自动生成
class DifficultyChoose_Dialog(object):
    def setupUi(self, Dialog, level_data):
        self.form = Dialog
        self.level_data = level_data
        self.difficulty = -1

        Dialog.setObjectName("Dialog")
        Dialog.resize(745, 509)
        Dialog.setStyleSheet("#Dialog{background-color: gainsboro;\n"
                             "border-image: url(icon/choose.jpg);}")
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(312, 0, 120, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 70, 141, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")

        self.level_button_list = []
        for i in range(len(self.level_data)):
            self.level_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
            self.level_button.setMinimumSize(QtCore.QSize(138, 51))
            font = QtGui.QFont()
            font.setFamily("幼圆")
            font.setPointSize(15)
            font.setBold(True)
            font.setItalic(True)
            font.setWeight(75)
            self.level_button.setFont(font)
            self.level_button.setStyleSheet(
                "QPushButton { background-color: rgb(125, 127, 255); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(255, 11, 84); }")
            self.level_button.setObjectName("pushButton_5")
            self.level_button_list.append(self.level_button)
            self.verticalLayout.addWidget(self.level_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择难度"))
        self.label.setText(_translate("Dialog", "难度选择"))
        for i in range(len(self.level_data)):
            self.level_button_list[i].setText(_translate("Dialog", self.level_data[i][3]))
            self.level_button_list[i].clicked.connect(partial(self.setDifficulty, i))  # 连接槽函数

    # 设置难度
    def setDifficulty(self, i):
        self.difficulty = i
        self.form.close()

    # 返回难度
    def getDifficulty(self):  # 获取结算数据
        return self.difficulty
