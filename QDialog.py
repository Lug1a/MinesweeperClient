# 重写closeEvent方法，实现dialog窗体关闭时执行一些代码
import PyQt5
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets


# 自定义窗口
class myDialog(QtWidgets.QDialog):
    pygame.mixer.init()
    sound = 0.0
    def mousePressEvent(self, QMouseEvent):
        if self.sound > 0.0:
            pygame.mixer.music.load("media/click_sound.mp3")
            pygame.mixer.music.set_volume(self.sound)
            pygame.mixer.music.play(1, 0)


# 主窗口
class MainDialog(myDialog):
    # pygame.mixer.init()
    # sound = 0.0
    # def mousePressEvent(self, QMouseEvent):
    #     pygame.mixer.music.load("media/click_sound.mp3")
    #     pygame.mixer.music.set_volume(self.sound)
    #     pygame.mixer.music.play(1, 0)

    def get_thread(self, main_thread):
        self.main_thread = main_thread

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '提示',
                                               "是否要退出本界面？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# 扫雷游戏窗口
class MineDialog(QtWidgets.QDialog):
    finish = 0  # 监测游戏是否处于结束状态

    def get_thread(self, main_thread):
        self.main_thread = main_thread

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        if self.finish == 0:
            reply = QtWidgets.QMessageBox.question(self,
                                                   '警告',
                                                   "现在退出游戏将扣除金币和积分，是否继续？",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
                pygame.mixer.music.pause()
                self.close()
            else:
                event.ignore()
        else:
            self.close()
# 等待窗口
class WaitDialog(myDialog):
    if_close = 0
    def get_thread(self, main_thread):
        self.main_thread = main_thread

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        if self.if_close == 0:
            event.ignore()
        self.close()