'''
Created on Jan 30, 2015

@author: AlirezaF
'''

from hashlib import md5
import hmac

def get_md5(scrip, *args):
    m = md5()
#     for arg in args:
#         # bytes takes iterable objects
#         if (type(arg) == str):
#         # m.update(bytes(list(arg)))
#             m.update(arg.encode())
#         else:
#             m.update(arg)
    for e in [scrip.vendor_id, scrip.amount, scrip.id, scrip.cust_id, scrip.expiry]:
        m.update(str(e).encode())    
    return m.hexdigest()

def get_hmac(key, *args):
    m = hmac.new(key.encode(), b'', digestmod=md5)
    for arg in args:
        m.update(arg.encode())
    return m.hexdigest()


# print(get_certificate("sdf", "hi", "tada"))    
# digest_maker = hmac.new('secret-shared-key-goes-here')
# 
# f = open('lorem.txt', 'rb')
# try:
#     while True:
#         block = f.read(1024)
#         if not block:
#             break
#         digest_maker.update(block)
# finally:
#     f.close()
# 
# digest = digest_maker.hexdigest()
# print digest    