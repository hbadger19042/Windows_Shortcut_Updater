# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 423)
        
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        self.rootpath = QtWidgets.QLineEdit(self.centralWidget)
        self.rootpath.setGeometry(QtCore.QRect(110, 20, 271, 20))
        self.rootpath.setObjectName("rootpath")
        
        self.oldstring = QtWidgets.QLineEdit(self.centralWidget)
        self.oldstring.setGeometry(QtCore.QRect(20, 60, 361, 20))
        self.oldstring.setObjectName("oldstring")
        
        self.root = QtWidgets.QPushButton(self.centralWidget)
        self.root.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.root.setObjectName("root")
        
        self.newstring = QtWidgets.QLineEdit(self.centralWidget)
        self.newstring.setGeometry(QtCore.QRect(20, 90, 361, 20))
        self.newstring.setText("")
        self.newstring.setObjectName("newstring")
        
        self.updaptelink = QtWidgets.QPushButton(self.centralWidget)
        self.updaptelink.setGeometry(QtCore.QRect(150, 120, 120, 23))
        self.updaptelink.setObjectName("updaptelink")
        self.updaptelink.setText("Update target link")
        
        self.logwindow = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.logwindow.setGeometry(QtCore.QRect(20, 150, 361, 221))
        self.logwindow.setObjectName("logwindow")
        
        self.log = QtWidgets.QLabel(self.centralWidget)
        self.log.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.log.setAlignment(QtCore.Qt.AlignCenter)
        self.log.setObjectName("log")
        
        self.clearlog = QtWidgets.QPushButton(self.centralWidget)
        self.clearlog.setGeometry(QtCore.QRect(20, 380, 75, 23))
        self.clearlog.setObjectName("clearlog")
        
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Windows Shortcut Updater"))
        self.oldstring.setPlaceholderText(_translate("MainWindow", "input old string"))
        self.root.setText(_translate("MainWindow", "Pick Root Dir"))
        self.newstring.setPlaceholderText(_translate("MainWindow", "input new string"))
        self.log.setText(_translate("MainWindow", "logging"))
        self.clearlog.setText(_translate("MainWindow", "Clear Log"))

