# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MEP.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAddNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddNew.setGeometry(QtCore.QRect(10, 40, 141, 61))
        self.btnAddNew.setAutoFillBackground(False)
        self.btnAddNew.setObjectName("btnAddNew")
        self.lblSearch = QtWidgets.QLabel(self.centralwidget)
        self.lblSearch.setGeometry(QtCore.QRect(30, 10, 41, 21))
        self.lblSearch.setObjectName("lblSearch")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 721, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Every Password"))
        self.btnAddNew.setText(_translate("MainWindow", "Add +"))
        self.lblSearch.setText(_translate("MainWindow", "Search:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
