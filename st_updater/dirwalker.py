
import os, logging



class DirWalker():
    """description of class"""
    @staticmethod
    def GetFilePath(root):
        for (thisdir, subdir, thisfiles) in os.walk(root): # generate dirs in tree
            for fname in thisfiles: # print files in this dir
                yield os.path.join(thisdir, fname)
    @staticmethod
    def GetDirNames(root):
        for (thisdir, subdir, thisfiles) in os.walk(root): # generate dirs in tree
            for dirname in subdir: # print files in this dir
                yield dirname


