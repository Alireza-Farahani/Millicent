'''
Created on Jan 30, 2015

@author: AlirezaF
'''
from statics.Utils import get_md5

import json

class Scrip():
    '''
    Base class for Scrip
    if vendor is not set (empty string as ""), means its a broker scrip
    '''


    def __init__(self, vendor_id, id, cust_id, expiry, amount, info=None):
        '''
        Create a new Scrip from given parameters.
        Info is a optional parameter containing some information
        about customer like age, gender etc. (Not implemented yet)
        '''
        
        # parameters used in certificate hash
        self.vendor_id = vendor_id
        # value of this scrip
        self.amount = amount
        self.id = id
        self.cust_id = cust_id
        self.expiry = expiry
        self.certificate = self.get_certificate()
        
        
    
    def get_certificate(self):
        return get_md5(str(self.vendor_id), str(self.amount), str(self.id), str(self.cust_id), str(self.expiry))    

    def __str__(self):
#         return str(self.vendor_id) + '&' + str(self.amount) + '&' + str(self.id) + '&' +\
#              str(self.cust_id) + '&' + str(self.expiry) + '&' + str(self.certificate)
        return json.dumps({'vendor': str(self.vendor), 'id' :str(self.id),
                           'cust_id':str(self.cust_id), 'expiry':str(self.expiry),
                           'certificate': str(self.certificate)
        })
