import sys
import json
from QDialog import myDialog
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QHeaderView, QListWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from TcpClient import tcp_client_socket

class Ui_dialog(object):
    def setupUi(self, dialog, administratorsID, playerData):
        self.administratorsID = administratorsID
        self.playerNum = len(playerData)
        self.data = playerData
        self.dialog = dialog
        dialog.setObjectName("dialog")
        dialog.resize(630, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(dialog)
        self.tableWidget.setMidLineWidth(-12)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")


        self.tableWidget.verticalHeader().setVisible(False) #隐藏垂直表头

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(self.playerNum)
        item = QtWidgets.QTableWidgetItem()

        for i in range(self.playerNum):
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()

        for i in range(self.playerNum):
            for j in range(4):
                self.tableWidget.setItem(i, j, item)
                item = QtWidgets.QTableWidgetItem()

        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(dialog)
        self.tableWidget.cellClicked['int','int'].connect(self.deleteGamer)

        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "玩家账号管理"))
        self.label.setText(_translate("dialog", "玩家账号管理"))

        for i in range(self.playerNum):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("dialog", str(i+1)))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dialog", "玩家ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dialog", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dialog", "密码"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("dialog", "删除玩家"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for i in range(self.playerNum):
            for j in range(3):
                item = self.tableWidget.item(i, j)
                item.setText(_translate("dialog", str(self.data[i][j])))
            item = self.tableWidget.item(i, 3)
            item.setText(_translate("dialog", "删除"))

        self.tableWidget.setSortingEnabled(__sortingEnabled)


    def deleteGamer(self, x, y):
        if y==3:
            isDel = QMessageBox.information(self.dialog, "提示", "是否确定删除玩家" + str(self.data[x][1]) +"？", QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if isDel == QMessageBox.Yes:
                tcp_client_socket.send("814 " + self.administratorsID + " " + str(self.data[x][0]))
                data_list_815 = tcp_client_socket.rec().split(" ")
                if(json.loads(data_list_815[1]) == 1):
                    del self.data[x]
                    self.tableWidget.removeRow(x)
                elif json.loads(data_list_815[1]) == 2:
                    reply = QMessageBox.about(self.dialog, "提示", "您输入的账号在线！请稍后再删除该账号")


if __name__ == "__main__":

    data=[[111111,"小红",123123],[2222222,"小白",234234],[333333,"小黑",345345]]

    app = QApplication(sys.argv)
    form = myDialog()
    ui = Ui_dialog()
    ui.setupUi(form, 12342, data)
    form.show()
    app.exec_()
    sys.exit()