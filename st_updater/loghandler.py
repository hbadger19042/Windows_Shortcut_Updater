'''
Created on Apr 22, 2017

@author: dongi
'''


import logging



class EditLogHandler(logging.Handler):
    def __init__(self, qedit):
        super().__init__()
        self.widget = qedit
        self.widget.setReadOnly(True)
        
    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)
        self.flush()
        
