'''
Created on Apr 21, 2017

@author: dongi
'''

from st_updater.batchset import ResetAllTargetLink

import pytest, os
from st_updater.shortcut import NewShortcut, LoadedShortCut

@pytest.fixture(scope='module')
def testScut():
    dirpath =os.path.join(os.getcwd(), 'this\\is\\fun\\')
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    filepath = os.path.join( dirpath + 'test_scut.lnk')
    targetpath = 'C:\\hello\\goodmorning'
    nscut = NewShortcut(filepath, targetpath)
    yield nscut
    os.system('rmdir /s /q ' + os.getcwd()+'\\this')
    
def test_reset_targetlink(testScut):
    oldstring ='good'
    newstring = 'bad'
    ResetAllTargetLink(os.getcwd(), oldstring, newstring)
    lscut = LoadedShortCut(testScut.filepath)
    assert lscut.GetTargetPath() == testScut.targetpath.replace(oldstring, newstring)