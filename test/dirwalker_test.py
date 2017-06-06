
import os
import pytest

from st_updater.dirwalker import DirWalker

def randomdirName(searchstring):
    choice = random.randint(1,3);
    searchAdd = 0 #number of search directory increase
    if choice == 1:
        dirName = searchstring + str(uuid.uuid4())
        searchAdd += 1
    elif choice ==2:
        dirName = str(uuid.uuid4())
    elif choice == 3:
        dirName = str(uuid.uuid4()) + searchstring
        searchAdd += 1
    return dirName, searchAdd
        
import uuid, random
import shutil

def CreateTestDTree(root, searchstring, numDir, depth):  
    """
    Create directory tree for testing . searchstring is
    to test to find out the directory by searchstring while directory walking
    """    
    if os.path.exists(root):
        shutil.rmtree(root)
        os.makedirs(root)
    else:
        os.makedirs(root)
    levelDirCount = round(numDir/depth) #directory number in each directory level     
    searchCount = 0 #number of directory to be searched 
    for j in range(levelDirCount):
        dirPath = root
        newdirName, searchAdd = randomdirName(searchstring)        
        dirPath = os.path.join(dirPath, newdirName)
        try:
            searchCount += searchAdd
            os.makedirs(dirPath)
        except OSError: pass        
        for i in range(depth-1):
            newdirName, searchAdd = randomdirName(searchstring)            
            dirPath = os.path.join(dirPath, newdirName)
            try:
                searchCount += searchAdd
                os.makedirs(dirPath)
            except OSError: pass
            
    dirPath = root
    for k in range(numDir - levelDirCount*depth):     
        newdirName, searchAdd = randomdirName(searchstring)   
        dirPath=os.path.join(dirPath, newdirName)
        try:    
            searchCount += searchAdd    
            os.makedirs(dirPath)
        except OSError: pass        
    return searchCount


testDirData = [("F:\\dfd01", "hello_", 25, 4), ("F:\\ssf02", "hi_", 50, 5), ("F:\\dfad03", "good_", 100, 3)]

@pytest.mark.parametrize("root, searchstring, numDir, depth", testDirData )
def test_directory_number_count_by_string_match(root, searchstring, numDir, depth):
    searchCount = CreateTestDTree(root, searchstring, numDir, depth)
    dircount = 0
    dwalker = DirWalker()
    for dirname in dwalker.GetDirNames(root):
        if not dirname.find(searchstring) == -1:
            print(dirname, searchstring)
            dircount += 1
    assert(dircount == searchCount)
    shutil.rmtree(root)
    
        
        