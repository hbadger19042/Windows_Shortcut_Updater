'''
Created on Apr 23, 2017

@author: dongi
'''


from setuptools import setup, find_packages
setup(
        name = "Shocut Target Updater",
        version = "0.1",
        packages = find_packages(),
        entry_points={
            'gui_scripts':[
                'shortcut_target_updater=st_updater.stupdater:StartMainWindow']
            }  
    )