'''
Created on Jan 30, 2015

@author: AlirezaF
'''

class Node():
    '''
    Base class for a node in network. A node can be one of the customer, vendor or broker
    '''

    def __init__(self, net_id):
        '''
        '''
        self.id = net_id
        
        
        

class Broker(Node):
    '''
    Knows vendors in network and has their secret keys
    Customer buy broker Scrip by sending request and receiving Scrip in plain text.
    '''
    
    def __init__(self, vendors, customers):
        '''
        Secrets are created in vendor init function, broker simply use them.
        '''
  
class Customer(Node):
    '''
    Has a unique ID in network, buy scrip from broker and uses that in 
    '''                
    
    
class Vendor(Node):
    
    
    
    def __init__(self):    