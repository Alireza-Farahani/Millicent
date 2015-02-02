'''
Created on Jan 30, 2015

@author: AlirezaF
'''

class Logger:
    '''
    Create new Logger (file or console) object, use log method for logging.
    Dont forget to call finalize when your done. (closing file in File subclass)
    '''
    def log(self, message):
        # TODO: change this line for switching between file and console for outputing
        pass

    def finalize(self):
        pass



class Console(Logger):
    def log(self, message):
        Logger.log(self, message)
        print(message)
        




class File(Logger):
    
    def __init__(self):
        self.f = open("../log.txt", "w")
    
    def log(self, message):
        Logger.log(self, message)
        self.f.write(message + "\n")
        
    def finalize(self):
        Logger.finalize(self)
        self.f.close()
        