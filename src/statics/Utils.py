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

def get_hmac(key, scrip):
    m = hmac.new(key.encode(), b'', digestmod=md5)
    for e in [scrip.vendor_id, scrip.amount, scrip.id, scrip.cust_id, scrip.expiry]:
        m.update(str(e).encode())
    return m.hexdigest()

def is_scrip_valid(scrip, type, key=None):
    # type == md5 -> simple hash
    # type == hmac -> hmac using secret
    certif = scrip.certificate
    if type == "md5":
        if get_md5(scrip) != certif:
            raise Exception("bad md5")
    elif type == "hmac":
        if get_hmac(key, scrip) != certif:
            raise Exception("bad hmac")

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