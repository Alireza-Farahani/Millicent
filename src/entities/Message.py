'''
Created on Jan 30, 2015

@author: AlirezaF
'''

import json

class Message():
    '''
    Base class for all of the messages exchanged in network.
    General format is:
    msg type---sender---receiver---data
    data itself is separated by +++. (e.g. scrip from vendor_id in RequestVendorScrip)
    '''

    dash = "---"
    data_seg = "+++"

    def __init__(self, sender, receiver):
        '''
        Both sender and receiver are in terms of ID
        '''
        self.sender = sender
        self.receiver = receiver
        
        
    def __str__(self):
        return type(self).__name__ + self.dash + str(self.sender) + self.dash + str(self.receiver) + self.dash      


    def as_json(self):
        return "#TODO - FJ, Impelement it"


class RequestBrokerScrip(Message):
    '''
    A simple message from a customer to broker for buying scrip.
    Contains customer_ID and value of scrip he wants to buy.
    '''        
    
    def __init__(self, cust_id, broker_id, amount):
        Message.__init__(self, cust_id, broker_id)
        self.amount = amount
        
    def __str__(self):
        return Message.__str__(self) + str(self.amount)    
        
        
class ResponseBrokerScrip(Message):
    '''
    A simple message from the broker to a customer containing scrip.
    Contains customer_ID and value of scrip he wants to buy.
    '''        
    
    def __init__(self, broker_id, cust_id, scrip): # scrip in string format
        Message.__init__(self, cust_id, broker_id)
        self.scrip = scrip
        
    def __str__(self):
        return Message.__str__(self) + str(self.scrip)


        
class RequestVendorScrip(Message):
    '''
    A simple message from a customer to broker for buying a vendor scrip.
    Contains customer_ID and value of scrip he wants to buy and vendor ID.
    '''        
    
    def __init__(self, cust_id, broker_id, vendor_id, amount, broker_scrip):
        Message.__init__(self, cust_id, broker_id)
        self.vendor_id = vendor_id
        self.amount = amount
        self.broker_scrip = broker_scrip
        
    def __str__(self):
        return Message.__str__(self) + str(self.vendor_id) +\
             self.data_seg + str(self.amount) + self.data_seg + str(self.broker_scrip)   
        


class ResponseVendorScrip(Message):
    '''
    A simple message from the broker to a customer containing scrip.
    Contains customer_ID and value of scrip he wants to buy.
    '''        
    
    def __init__(self, broker_id, cust_id, vendor_scrip, broker_change_scrip = None):
        # scrip in string format
        Message.__init__(self, broker_id, cust_id)
        self.vendor_scrip = vendor_scrip
        self.broker_change_scrip = broker_change_scrip
        
    def __str__(self):
        return Message.__str__(self) + str(self.scrip)

        

class RequestProducInfo(Message):
    def __init__(self, cust_id, vendor_id):
        Message.__init__(self, cust_id, vendor_id)

        
class ResponseProductInfo(Message):
    '''
    '''
    def __init__(self, vendor_id, customer_id, product_name, product_price):
        Message.__init__(self, vendor_id, customer_id)
        self.product_name = product_name 
        self.product_price = product_price
        
    def __str__(self):
        return Message.__str__(self) + str(self.product_name) + self.data_seg + str(self.product_price)


class RequestBuyProduct(Message):
    '''
    Message in which a customer sends vendor scrip to that vendor
    and buys the actual product. 
    '''
    
    def __init__(self, cust_id, vendor_id, vendor_scrip): # number of products to buy will be
        Message.__init__(self, cust_id, vendor_id) # implemented. scrip in string format.
        self.vendor_scrip = vendor_scrip
        
    def __str__(self):
        return Message.__str__(self) + str(self.vendor_scrip)
    
    
class ResponBuyProduct(Message):
    '''
    Message containing the product itself and change in form of new scrip. 
    '''
    
    def __init__(self, vendor_id, cust_id, product, change_scrip): # number of products to buy will be
        Message.__init__(self, cust_id, vendor_id) # implemented. scrip in string format.
        self.change_scrip = change_scrip
        self.product = product # product is a instance object.         
    
    def __str__(self):
        return Message.__str__(self) + str(self.product) + self.data_seg + str(self.change_scrip)                   