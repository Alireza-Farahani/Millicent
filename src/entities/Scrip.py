'''
Created on Jan 30, 2015

@author: AlirezaF
'''

class Scrip():
    '''
    Base class for Scrip
    '''


    def __init__(self, vendor, id, cust_id, expiry, amount, info=None):
        '''
        Create a new Scrip from given parameters.
        Info is a optional parameter containing some information
        about customer like age, gender etc. (Not implemented yet)
        '''
        
        # parameters used in certificate hash
        self.vendor = vendor
        self.id = id
        self.cust_id = cust_id
        self.expiry = expiry
        
        # value of this scrip
        self.amount = amount
    
        
