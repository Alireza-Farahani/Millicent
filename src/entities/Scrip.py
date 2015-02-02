'''
Created on Jan 30, 2015

@author: AlirezaF
'''
from statics.Utils import *

class Scrip():
    '''
    Base class for Scrip
    if vendor is not set (empty string as ""), means its a broker scrip
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
        self.certificate = self.get_certificate()
        
        # value of this scrip
        self.amount = amount
        
    
    def get_certificate(self):
        return get_md5([self.vendor, self.id, self.cust_id, self.expiry])    

    def __str__(self):
        return str(self.vendor) + '&' + str(self.id) + '&' +\
             str(self.cust_id) + '&' + str(self.expiry) + '&' + str(self.certificate)