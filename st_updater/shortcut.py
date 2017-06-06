
import os
import pythoncom
from win32com.shell import shell
import win32com.client

class LoadedShortCut():
    """Load existing short cut and do opertion on it"""
    def __init__(self, filepath):
        self.filepath = filepath
        self.Load()
        
    def Load(self):
        self.link = pythoncom.CoCreateInstance (
            shell.CLSID_ShellLink,
            None,
            pythoncom.CLSCTX_INPROC_SERVER,
            shell.IID_IShellLink
        )
        self.persist_file = self.link.QueryInterface (pythoncom.IID_IPersistFile)
        self.persist_file.Load (self.filepath)  

    
    def GetTargetPath(self):
        return self.link.GetPath(shell.SLGP_UNCPRIORITY)[0]
        
    def SetTargetPath(self, targetPath):
        self.link.SetPath(targetPath)
        self.persist_file.Save(self.filepath, 0)
        

class NewShortcut():  
    """
    Create new shortcut
    """  
    def __init__(self, filepath, targetpath):
        self.filepath=filepath
        self.targetpath = targetpath
        self.CreateShortCut()  
        
    def CreateShortCut(self):
        ws = win32com.client.Dispatch("wscript.shell")
        self.scut = ws.CreateShortcut(self.filepath)
        self.scut.TargetPath = self.targetpath
        self.scut.Save()