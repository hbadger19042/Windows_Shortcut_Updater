

"""Test Shortcut's target path reset method"""


import sys, os

import win32com.client
from fileinput import filename
from st_updater.shortcut import LoadedShortCut, NewShortcut

import pytest
from pip._vendor.requests.api import request

@pytest.fixture(scope='module')
def testScut():
    filepath = os.path.join(os.getcwd(), 'test_scut.lnk')
    targetpath = 'C:\\'
    nscut = NewShortcut(filepath, targetpath)
    yield nscut
    os.system('del ' + filepath)


def test_getTargetPath(testScut):
    """
    Create shortcut and check if its target path is correct
    """
    loadedscut = LoadedShortCut(testScut.filepath)
    assert testScut.targetpath == loadedscut.GetTargetPath()
    
    
def test_setTargetPath(testScut):
    """
    Create shortcut and check if method SetTargetPath works
    """
    loadedscut = LoadedShortCut(testScut.filepath)
    newTargetPath = 'F:\\'
    if os.path.exists(newTargetPath):
        loadedscut.SetTargetPath(newTargetPath)
        newTargetPath = loadedscut.GetTargetPath()
        assert newTargetPath == loadedscut.GetTargetPath()     
        
