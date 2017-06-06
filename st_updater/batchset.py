from st_updater.dirwalker import DirWalker 
from st_updater.shortcut import LoadedShortCut


import logging
import sys

batlogger = logging.getLogger("batchset.py")

encoding = sys.getfilesystemencoding()
  
def ResetAllTargetLink(root, oldstring, newstring):
    dwalker = DirWalker()
    batlogger.info("Shortcut update is started.")
    for filepath in dwalker.GetFilePath(root):
        if filepath.endswith('.lnk'):
            scut = LoadedShortCut(filepath)
            target = scut.GetTargetPath()
            if target.find(oldstring) != -1:
                newtarget = target.replace(oldstring, newstring)
                scut.SetTargetPath(newtarget)
                batlogger.info(filepath.encode(encoding).strip())
                batlogger.info("<--- old target: %s" %target.encode(encoding).strip())
                batlogger.info("---> new target: %s" %newtarget.encode(encoding).strip())
    batlogger.info("Shortcut update is finished.")
    
  
if __name__ == "__main__":
    import sys, getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hr:o:n:", ['root=','old=','new='])
    except getopt.GetoptError as error:
        print(error.msg)
        print('usage: test.py -r <root_path> -o <oldstring> -n <newstring>')
        sys.exit(2)
    opts = dict((x , y) for x, y in opts)    
    if '-h' in opts.keys():
        print('usage: test.py -r <root_path> -o <oldstring> -n <newstring>')
        sys.exit()
    elif not all(['-r' in opts.keys(), '-o' in opts.keys(), '-n' in opts.keys()]):
        print('usage: test.py -r <root_path> -o <oldstring> -n <newstring>')
        print('All three options are required.')
        sys.exit(2)   
          
    root=opts['-r']
    oldstring=opts['-o']
    newstring=opts['-n']

    try:
        ResetAllTargetLink(root, oldstring, newstring)     
    except:
        print("Errors: Check your arugments")