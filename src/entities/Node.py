'''
Created on Jan 30, 2015

@author: AlirezaF
'''
from entities.Message import *
from entities.Scrip import *
from random import randrange
from Crypto.Random.random import sample
from entities.Network import Network
import time.time

class Node():
    '''
    Base class for a node in network. A node can be one of the customer, vendor or broker
    '''

    def __init__(self, network, net_id):
        '''
        net_id is the unique id of this node in network
        '''
        self.network = network
        self.id = net_id
        
        
    def send_msg(self, message):
        '''
        sends the message into network. receiver
        ''' 
        # self.network.deliver_msg(message)
        pass    
        
    def receive_msg(self, message):
        self.process_msg(message)    
    
    def process_msg(self, message):
        '''
        Splits the message into parts specified by ------ line
        '''
        msg = dict(zip(["type", "sender", "receiver", "data"], message.split("---")))
        msg["data"] = msg["data"].split(Message.data_seg) 



class Broker(Node):
    '''
    Knows vendors in network and has their secret keys
    Customer buy broker Scrip by sending request and receiving Scrip in plain text.
    '''
    broker_expiry = 120 # in term of seconds
    vendor_expiry = 60 
    
    def __init__(self, network, net_id, vendors):
        Node.__init__(self, network, net_id)
        self.vendors = vendors
        
        self.valid_scripsIDs = sample(range(0, 0xFFFFFFFF), 1000)
        self.used_scripsIDs = []
    
    def process_msg(self, message):
        msg = Node.process_msg(self, message)
        
        if msg["type"] == "RequestBrokerScrip":
            scrip = Scrip("", self.generate_scripID(), msg["sender"], self.get_bro, msg["data"], "")
            
            self.send_msg(ResponseBrokerScrip(self.id, msg["sender"], scrip))
            
        elif msg["type"] == "RequestVendorScrip":
            # mojudie broker scrip va mizani ke vendor scrip mikhad 
            # ba tavajjoh be ham barresi shan
            # TODO: incomplete
            
            broker_scrip = msg["data"][2] # TODO: chejuri besazamesh az string??
            vendor_id = msg["data"][0]
            vendor_scrip_amount = msg["data"][1]
            cust_id = msg["sender"]
            
            vendor_scrip = Scrip(vendor_id, self.generate_scripID(), cust_id, self.get_expiry(), vendor_scrip_amount)
            
            broker_change_scrip = Scrip("", self.generate_scripID(), cust_id, self.get_broker_expiry(), broker_scrip.amount - vendor_scrip_amount)
            
            self.used_scripsIDs.append(broker_scrip.id)
            
            
            self.send_msg(ResponseVendorScrip(self.id, cust_id, vendor_scrip, broker_change_scrip))    
        
    def get_broker_expiry(self):
        return int(time() + self.broker_expiry) # a scrip lasts for only 10 minute
    
    def get_vendor_expiry(self):
        return int(time() + self.vendor_expiry)
    
    def generate_scripID(self):
        '''
        creates a new unique id for scrip.
        '''
        id = self.valid_scripsIDs.pop()
        self.used_scripsIDs.append(id)
        return id 
  
  
  
class Customer(Node):
    '''
    Has a unique ID in network, buy scrip from broker and uses that in 
    '''                
    def __init__(self, money):
        self.money = money
        self.borker_scrips = []
        
    def add_broker_scrip(self, scrip):
        self.broker_scrips.append(scrip)    
    
    def purchase_broker_scrip(self, amount):
        '''
        requests a scrip from broker with the amount given.
        '''
        self.send_msg(RequestBrokerScrip(self.id, self.network.broker_id, amount))
    
    def process_msg(self, message):
        msg = Node.process_msg(self, message)
        if msg["type"] == "ResponseBrokerScrip":
            pass
        elif msg["type"] == "ResponseVendorScrip":
            pass
        elif msg["type"] == "ResponseProductInfo":
            pass
        elif msg["type"] == "ResponseBuyProduct":
            pass
        
    
class Vendor(Node):
    '''
    '''
    
    def __init__(self, product):
        '''
        product is the class object of product type this vendor will sell
        '''
        self.create_mss() # Master_scrip_secret. 
        self.create_mcs() # Master_customer_secret.
        self.used_scrips = []
        self.product = product
    
    def create_product(self):
        self.products = [self.product() for i in range(100)]
    
    def product_info(self):
        return self.product.name + " " + self.product.price    
        
    def create_mss(self):
        '''
        creates ten random integer as Master Scrip secrets.
        '''
        self.mss = sample(randrange(0, 0xFFFFFFFF), 10) 
        
        
    def create_mcs(self):
        '''
        creates ten random integer as Master customer secrets.
        '''
        self.mss = sample(randrange(0, 0xFFFFFFFF), 10)
        
        
    def process_msg(self, message):
        msg = Node.process_msg(self, message)
        cust_id = msg["sender"]
        
        if msg["type"] == "RequestProducInfo":
            self.send_msg(ResponseProductInfo(self.id, cust_id, self.product.name, self.product.price))
            
        elif msg["type"] == "RequestBuyProduct":
            vendor_scrip = msg["data"] # TODO: recreate scrip from string
            
            vendor_change_scrip = Scrip(self.id, cust_id, self.get_expiry(), vendor_scrip.amount - self.product.price)
            self.used_scrips.append(vendor_scrip.id)
            
            self.send_msg(ResponBuyProduct(self.id, cust_id, vendor_change_scrip, self.products.pop()))
    
    
    def get_expiry(self):
        return int(time() + self.vendor_expiry)
    
        
class Product:
    pass
#     __name = ""
#     __price = ""
#     def set_values(name, price):
#         __name = name
#         __price = price
#     name = __name
#     price = __price    

class Book(Product):
    name = "book"
    price = "104" # in cents
    
class Track(Product):
    name = "track"
    price = "99" # in cents
    
class Service(Product):
    name = "service"
    price = "5"  # in cents               