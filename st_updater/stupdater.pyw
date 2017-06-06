

from PyQt5.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QApplication
from PyQt5.QtCore import QDir

from st_updater.mainwindow import Ui_MainWindow
from st_updater.loghandler import EditLogHandler
from st_updater.batchset import ResetAllTargetLink

import logging, sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.SetLogger()
        
        self.ui.root.clicked.connect(self.PickRootPath)
        self.ui.updaptelink.clicked.connect(self.UpdateTargetLink)
        self.ui.clearlog.clicked.connect(self.ui.logwindow.clear)
        
    def SetLogger(self):
        rootlogger = logging.getLogger("")
        rootlogger.setLevel(logging.NOTSET)
        
        elhandler = EditLogHandler(self.ui.logwindow)
        rootlogger.addHandler(elhandler)
        
        flhandler = logging.FileHandler("slinkupdate.log")
        rootlogger.addHandler(flhandler)
        
    def PickRootPath(self):
        dirPath = QFileDialog.getExistingDirectory(None, 'Pick root directory', QDir.currentPath())        
        if dirPath:
            self.ui.rootpath.setText(dirPath)
            
    def UpdateTargetLink(self):
        rootpath = self.ui.rootpath.text()
        oldstring = self.ui.oldstring.text()
        newstring = self.ui.newstring.text()
        
        if not all([rootpath, oldstring]):
            if not rootpath:
                QMessageBox.warning(self, "Warning", "Root path is not set", QMessageBox.Ok)
            if not oldstring:
                QMessageBox.warning(self, "Warning", "Old string is not set", QMessageBox.Ok)
        elif not newstring:
            reply = QMessageBox.question(self, "No new string", "Do you want to erase old string?" , QMessageBox.Yes|QMessageBox.No, 
                QMessageBox.No)
            if reply == QMessageBox.Yes:
                ResetAllTargetLink(rootpath, oldstring, newstring)
        else:
            ResetAllTargetLink(rootpath, oldstring, newstring)
        

def StartMainWindow():
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    sys.exit(app.exec_())
                
if __name__ == "__main__":
    StartMainWindow()

    