import math
import sys
from threading import Thread
from multiprocessing import Process

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QLineEdit, QInputDialog, QMessageBox, QApplication

from TcpClient import tcp_client_socket
from mine import mineLabel, statusLabel
import random, pygame, GameMessage


# 父布局
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(800, 700)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minelabel = QtWidgets.QLabel(self.frame)
        self.horizontalLayout.addWidget(self.minelabel)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.stagelabel = QtWidgets.QLabel(self.frame)
        self.horizontalLayout.addWidget(self.stagelabel)
        self.label_2 = statusLabel.StatusLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.stagenumlabel = QtWidgets.QLabel(self.frame)
        self.horizontalLayout.addWidget(self.stagenumlabel)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.timelabel = QtWidgets.QLabel(self.frame)
        self.horizontalLayout.addWidget(self.timelabel)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "扫雷"))
        self.minelabel.setText(_translate("Dialog", "剩余雷数:"))
        self.label.setText(_translate("Dialog", "0"))
        self.stagelabel.setText(_translate("Dialog", "道具:"))
        self.stagenumlabel.setText(_translate("Dialog", "0"))
        self.timelabel.setText(_translate("Dialog", "时间:"))
        self.label_3.setText(_translate("Dialog", "0"))


# 扫雷的ui界面，主要实现功能，布局使用父布局
class MineSweeperUI(Ui_Dialog):
    def __init__(self, Dialog, diffculty, level_data, stagenum, userID, is_double, background_volume):
        self.path = "mine/media"
        # 播放音乐
        file = self.path + '/background.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(background_volume)
        pygame.mixer.music.play(-1, 0)

        # 设置行数，列数，雷数，难度级别
        self.row = level_data[0]
        self.column = level_data[1]
        self.mineNum = level_data[2]
        self.rank = level_data[3]

        self.difficulty = diffculty
        self.stagenum = stagenum
        self.userID = userID
        self.mine_num = 0
        self.is_double = is_double

        # 设置界面初始信息
        self.first_click = True
        self.first_click_i = -1
        self.first_click_j = -1
        self.finish = False
        self.dialog = Dialog
        self.dialog.setWindowIcon(QIcon(self.path + "/mine.jpg"))
        self.dialog.setFixedSize(self.dialog.minimumSize())
        self.setupUi(self.dialog)

        # 初始化格子和雷区
        self.mineLabel = []
        self.initMineArea()
        self.createMine()

        # 魔法道具按钮和数量
        pixmap = QPixmap(self.path + "/魔法药水.png")
        self.label_2.setPixmap(pixmap)
        self.label_2.leftRelease.connect(self.reduce_time)
        self.label_2.setScaledContents(True)
        if stagenum > 0:
            self.stagenumlabel.setText(str(stagenum))
        else:
            self.stagenumlabel.setText(str(stagenum))
            self.label_2.setEnabled(False)

        # 设置雷数和时间等标签的颜色和字体
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.red)  # 设置字体颜色
        self.label_3.setPalette(pe)
        self.label_3.setFont(QFont("幼圆", 12, QFont.Bold))
        self.label.setPalette(pe)
        self.label.setFont(QFont("幼圆", 12, QFont.Bold))
        self.label.setText(str(self.mineNum))
        self.minelabel.setPalette(pe)
        self.minelabel.setFont(QFont("幼圆", 12, QFont.Bold))
        self.stagenumlabel.setPalette(pe)
        self.stagenumlabel.setFont(QFont("幼圆", 12, QFont.Bold))
        self.stagelabel.setPalette(pe)
        self.stagelabel.setFont(QFont("幼圆", 12, QFont.Bold))
        self.timelabel.setPalette(pe)
        self.timelabel.setFont(QFont("幼圆", 12, QFont.Bold))

        # 计时
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeCount)
        self.timeStart = True
        self.timer.start()
        self.s_close = 0
        if self.is_double == 1:
            self.sentmessage = 0

            t = Thread(target=self.get_end)
            t.start()

    # 判断坐标是否在格子外面，在外面返回true，否则返回false
    def outOfBorder(self, i, j):
        if i < 0 or i >= self.row or j < 0 or j >= self.column:
            return True
        return False

    # 初始化雷区数组
    def initMineArea(self):
        self.gridLayout.setSpacing(0)
        # 初始化数组
        for i in range(0, self.row):
            self.mineLabel.append([])
            for j in range(0, self.column):
                # 创建格子
                label = mineLabel.mineLabel(i, j, 0, "")
                label.setPixmap(QPixmap(self.path + "/cube.jpg"))
                label.setScaledContents(True)  # 设置每个格子的图片都是按大小自动缩放填充
                label.setMinimumSize(40, 40)
                label.setAlignment(Qt.AlignCenter)

                # 绑定雷区点击事件
                label.leftPressed.connect(self.mineAreaLeftPressed)
                label.leftAndRightPressed.connect(self.mineAreaLeftAndRightPressed)
                label.leftAndRightRelease.connect(self.mineAreaLeftAndRightRelease)
                label.leftRelease.connect(self.mineAreaLeftRelease)
                label.rightRelease.connect(self.mineAreaRightRelease)

                self.mineLabel[i].append(label)
                self.gridLayout.addWidget(label, i, j)

    # 随机生成雷区数组
    def createMine(self):
        num = self.mineNum
        while num > 0:
            if self.first_click_i == -1 and self.first_click_j == -1:
                r = random.randint(0, self.row - 1)
                c = random.randint(0, self.column - 1)
            else:
                r = random.randint(0, self.row - 2)
                c = random.randint(0, self.column - 2)
                if r >= self.first_click_i:
                    r += 1
                if c >= self.first_click_j:
                    c += 1
            if self.mineLabel[r][c].num != -1:
                self.mineLabel[r][c].num = -1
                num -= 1
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if not self.outOfBorder(i, j) and (
                                self.mineLabel[i][j].num != -1):
                            self.mineLabel[i][j].num += 1

    # 挖开格子
    def DFS(self, i, j, start0):
        # 如果格子还没被挖才可以挖开
        if self.mineLabel[i][j].status == 0:
            self.mineLabel[i][j].status = 1
            # 显示对应的数字
            if self.mineLabel[i][j].num >= 0:
                self.mineLabel[i][j].setPixmap(QPixmap(self.path + "/" + str(self.mineLabel[i][j].num) + ".jpg"))

            if self.isGameFinished():
                self.gameWin()
            if (start0 and self.mineLabel[i][j].num == 0) or (
                    not start0 and self.mineLabel[i][j].num == 0):
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if not self.outOfBorder(r, c) and self.mineLabel[r][c].status == 0 and self.mineLabel[r][
                            c].num != -1:
                            self.DFS(r, c, start0)

            # 点击的格子变回原样
            self.mineLabel[i][j].setFrameShape(0)
            self.mineLabel[i][j].setFrameShadow(0)

    # 左击按下
    def mineAreaLeftPressed(self, i, j):
        if not self.finish:
            if self.mineLabel[i][j].status == 0:
                # 制造点击的特效
                self.mineLabel[i][j].setFrameShape(QtWidgets.QFrame.Panel)
                self.mineLabel[i][j].setFrameShadow(QtWidgets.QFrame.Sunken)

    # 左击松开
    def mineAreaLeftRelease(self, i, j):
        if not self.finish:
            # 点击的不是雷
            if self.mineLabel[i][j].num >= 0:
                # 如果首次点击不是雷，则首次点击改为false
                if self.first_click == True:
                    self.first_click = False
                self.DFS(i, j, self.mineLabel[i][j].num == 0)  # 挖开格子
            # 点击的是雷
            else:
                # 如果首次点击是雷，则重新生成雷区
                if self.first_click == True:
                    self.first_click_i = i
                    self.first_click_j = j
                    # 初始化格子和雷区
                    self.mineLabel = []
                    self.initMineArea()
                    self.createMine()
                    # 重新判断是不是雷
                    self.mineAreaLeftRelease(i, j)
                # 如果不是首次点击并遇到雷，则游戏失败结束
                else:
                    self.gameFailed()

    # 右击松开
    def mineAreaRightRelease(self, i, j):
        if not self.finish:
            # 状态为未挖开
            if self.mineLabel[i][j].status == 0:
                pixmap = QPixmap(self.path + "/flag.jpg")  # 变为插旗
                self.mineLabel[i][j].setPixmap(pixmap)
                self.mineLabel[i][j].status = 2
                self.label.setText(str(int(self.label.text()) - 1))  # 雷数减一
            # 状态为插旗
            elif self.mineLabel[i][j].status == 2:
                self.mineLabel[i][j].setPixmap(QPixmap(self.path + "/question.jpg"))  # 变为疑问
                self.mineLabel[i][j].status = 3
                self.label.setText(str(int(self.label.text()) + 1))  # 雷数加回来
            # 状态为疑问
            elif self.mineLabel[i][j].status == 3:
                self.mineLabel[i][j].setPixmap(QPixmap(self.path + "/cube.jpg"))  # 变回最初的样子
                self.mineLabel[i][j].status = 0

    # 左右键同时按下
    def mineAreaLeftAndRightPressed(self, i, j):
        if not self.finish:
            if self.mineLabel[i][j].status == 1:
                count = 0
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if not self.outOfBorder(r, c):
                            if self.mineLabel[r][c].status == 0 or self.mineLabel[r][c].status == 3:
                                self.mineLabel[r][c].setFrameShape(QtWidgets.QFrame.Panel)
                                self.mineLabel[r][c].setFrameShadow(QtWidgets.QFrame.Sunken)
                            elif self.mineLabel[r][c].status == 2:
                                count += 1
                return count == self.mineLabel[i][j].num
            else:
                return False

    # 左右键同时松开
    def mineAreaLeftAndRightRelease(self, i, j):
        if not self.finish:
            if self.mineLabel[i][j].status == 1:
                # 如果这个格子已经挖开并且他周围格子的插旗数已经和这个格子周围的雷数相等，则把其他格子全挖开
                if self.mineAreaLeftAndRightPressed(i, j):
                    Fail = False
                    for r in range(i - 1, i + 2):
                        for c in range(j - 1, j + 2):
                            if not self.outOfBorder(r, c):
                                if self.mineLabel[r][c].status == 0 or self.mineLabel[r][c].status == 3:
                                    if self.mineLabel[r][c].status == 3:
                                        self.mineLabel[r][c].status = 0
                                    if self.mineLabel[r][c].num >= 0:
                                        self.DFS(r, c, self.mineLabel[r][c].num == 0)
                                    else:
                                        Fail = True
                    if Fail:
                        self.gameFailed()
                # 否则只展示特效
                else:
                    for r in range(i - 1, i + 2):
                        for c in range(j - 1, j + 2):
                            if not self.outOfBorder(r, c):
                                if self.mineLabel[r][c].status == 0 or self.mineLabel[r][c].status == 3:
                                    self.mineLabel[r][c].setFrameShape(QtWidgets.QFrame.WinPanel)
                                    self.mineLabel[r][c].setFrameShadow(QtWidgets.QFrame.Raised)

    # 判断游戏是否结束
    def isGameFinished(self):
        for i in self.mineLabel:
            for j in i:
                # 如果未被挖开的都是雷，则结束，否则未结束
                if j.status == 0 and j.num != -1:
                    return False
        return True

    # 游戏结束
    def gameFinished(self):
        self.dialog.finish = 1  # 设置窗口为游戏结束状态
        for i in self.mineLabel:
            for j in i:
                # 对每个格子，画上相应的记号
                if j.num == -1 or j.status == 2:
                    j.setFrameShape(QtWidgets.QFrame.Panel)
                    j.setFrameShadow(QtWidgets.QFrame.Sunken)
                    if j.num == -1 and j.status == 2:
                        self.mine_num += 1
                        pixmap = QPixmap(self.path + "/correct.png")
                    elif j.num == -1:
                        pixmap = QPixmap(self.path + "/mine.jpg")
                    else:
                        pixmap = QPixmap(self.path + "/mistake.jpg")
                    j.setPixmap(pixmap)
                    j.setScaledContents(True)
                j.status = 1
        # 停止计时
        self.timer.stop()
        self.finish = True

    # 游戏获胜
    def gameWin(self):
        self.gameFinished()  # 游戏结束
        self.mine_num = self.mineNum

        self.requestData()
        # 创建提示消息框
        self.dialog.setEnabled(False)
        form1 = QtWidgets.QDialog()
        form1.setWindowModality(2)
        ui = GameMessage.Ui_Dialog()

        if int(self.data_list[1]) >= 0:
            point = "增加了" + self.data_list[1]
        else:
            point = "减少了" + str(int(math.fabs(int(self.data_list[1]))))
        if int(self.data_list[2]) >= 0:
            gold = "增加了" + self.data_list[2]
        else:
            gold = "减少了" + str(int(math.fabs(int(self.data_list[2]))))

        ui.setupUi(form1,
                   ["游戏成功",
                    "游戏成功，共花费" + self.label_3.text() + "秒，积分" + point + "，金币" + gold])
        form1.show()
        form1.exec_()
        self.dialog.setEnabled(True)
        pygame.mixer.music.pause()
        self.dialog.close()

    # 游戏失败
    def gameFailed(self):
        self.gameFinished()  # 游戏结束
        self.requestData()
        # 创建提示消息框
        self.dialog.setEnabled(False)
        form1 = QtWidgets.QDialog()
        form1.setWindowModality(2)  # 使本窗口无法选中
        ui = GameMessage.Ui_Dialog()
        if int(self.data_list[1]) >= 0:
            point = "增加了" + self.data_list[1]
        else:
            point = "减少了" + str(int(math.fabs(int(self.data_list[1]))))
        if int(self.data_list[2]) >= 0:
            gold = "增加了" + self.data_list[2]
        else:
            gold = "减少了" + str(int(math.fabs(int(self.data_list[2]))))

        ui.setupUi(form1,
                   ["游戏失败",
                    "游戏失败，共扫出" + str(self.mine_num) + "个雷，积分" + point + "，金币" + gold])
        form1.show()
        form1.exec_()
        self.dialog.setEnabled(True)
        pygame.mixer.music.pause()
        self.dialog.close()

    # 使用药水，用时减2s
    def reduce_time(self):
        if int(self.label_3.text()) >= 2:
            self.label_3.setText(str(int(self.label_3.text()) - 2))

        # 使用道具一次，数量减一，减到0不再让使用
        self.stagenum -= 1
        self.stagenumlabel.setText(str(self.stagenum))
        if self.stagenum <= 0:
            self.label_2.setEnabled(False)

    # 向服务器请求更新玩家数据
    def requestData(self):
        if self.is_double == 0:  # 如果是单人游戏，接收回复，否则让get_end结收
            # 如果是强制关闭
            if self.dialog.finish == 0:
                # tcp_client_socket.send("1")
                tcp_client_socket.send("300" + ' '
                                       + self.userID + ' '
                                       + str(self.difficulty) + ' '
                                       + "-1" + ' '
                                       + "-1" + ' '
                                       + str(self.stagenum))
            else:
                # tcp_client_socket.send("1")
                tcp_client_socket.send("300" + ' '
                                       + self.userID + ' '
                                       + str(self.difficulty) + ' '
                                       + self.label_3.text() + ' '
                                       + str(self.mine_num) + ' '
                                       + str(self.stagenum))
            data = tcp_client_socket.rec()
            self.data_list = data.split()
        else:
            self.sentmessage = 1
            # 如果是强制关闭
            if self.dialog.finish == 0:
                self.data_list = ["000", "0", "0"]
                # tcp_client_socket.send("1")
                tcp_client_socket.send("302" + ' '
                                       + self.userID + ' '
                                       + str(self.difficulty) + ' '
                                       + "-1" + ' '
                                       + "-1" + ' '
                                       + str(self.stagenum))
            else:
                self.data_list = ["000", "0", "0"]
                # tcp_client_socket.send("1")
                tcp_client_socket.send("302" + ' '
                                       + self.userID + ' '
                                       + str(self.difficulty) + ' '
                                       + self.label_3.text() + ' '
                                       + str(self.mine_num) + ' '
                                       + str(self.stagenum))
            while (True):
                if self.data_list[0] == "303":
                    break

    # 计时，1s加一次，并且在双人游戏时检测是否收到提前结束游戏的消息
    def timeCount(self):
        self.label_3.setText(str(int(self.label_3.text()) + 1))

        if self.s_close == 1:  # 如果在双人游戏时检测是否收到提前结束游戏的消息
            self.dialog.finish = 1
            # 停止计时
            self.timer.stop()
            self.finish = True
            # pygame.mixer.music.pause()
            # self.dialog.close()
            # 创建提示消息框
            self.dialog.setEnabled(False)
            form1 = QtWidgets.QDialog()
            form1.setWindowModality(2)  # 使本窗口无法选中
            ui = GameMessage.Ui_Dialog()

            if int(self.data_list[1]) >= 0:
                point = "增加了" + self.data_list[1]
            else:
                point = "减少了" + str(int(math.fabs(int(self.data_list[1]))))
            if int(self.data_list[2]) >= 0:
                gold = "增加了" + self.data_list[2]
            else:
                gold = "减少了" + str(int(math.fabs(int(self.data_list[2]))))

            ui.setupUi(form1,
                       ["游戏失败",
                        "游戏失败，共扫出" + str(self.mine_num) + "个雷，积分" + point + "，金币" + gold])
            form1.show()
            form1.exec_()
            self.dialog.setEnabled(True)
            pygame.mixer.music.pause()
            self.dialog.close()

    # 匹配对战新开线程让get_end接收回复
    def get_end(self):
        while True:
            data = tcp_client_socket.rec()
            if not data:
                continue

            data_list = data.split(" ")
            # print(data_list)
            if data_list[0] == "303":
                self.data_list = data_list

            print("扫雷游戏窗口状态:",  self.sentmessage == 0)

            if self.sentmessage == 0:  # 如果还没结束游戏，则关闭窗口
                self.s_close = 1
            break

    def getData(self):
        if self.dialog.finish == 0:  # 强制关闭则请求数据
            # print(1)
            self.requestData()

    def updateStage(self):
        tcp_client_socket.send("304" + ' '
                               + self.userID + ' '
                               + str(self.stagenum))
        data_list305 = tcp_client_socket.rec().split()
        if data_list305[0] != "305" or data_list305[1] != "1":
            print("error：更新道具数量失败")
