'''
Created on Jan 30, 2015

@author: AlirezaFj
'''

from hashlib import md5
import hmac
import rsa
from Crypto.Cipher import DES
import json
from entities.Scrip import Scrip


RSA_CRYPTO = 'RSA'
AES_CRYPTO = 'AES'
DES_CRYPTO = 'DES'

def encrypt_message_deco(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def decrypt_message_deco(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def encrypt_message(msg, crypto, key, iv=''):
    if crypto == RSA_CRYPTO:
        return rsa.encrypt(msg, key)

    if crypto == DES_CRYPTO:
        cbc_des_cipher = DES.new(key, DES.MODE_CBC, iv)
        return cbc_des_cipher.encrypt(msg)

    if crypto == AES_CRYPTO:
        return "Is it really needed ?"


def decrypt_message(msg, crypto, key, iv=''):
    if crypto == RSA_CRYPTO:
        return rsa.decrypt(msg, key)

    if crypto == DES_CRYPTO:
        cbc_des_decipher = DES.new(key, DES.MODE_CBC, iv)
        return cbc_des_decipher.decrypt(msg)

    if crypto == AES_CRYPTO:
        return "Is it really needed ?"


def join_list(arr, header):
    return header + '|'.join(arr)

def get_md5(scrip):
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

def parse_scrip(string):
        # TODO: parse scrip from string representation
        j = json.loads(string)
        return Scrip(j['vendor_id'], j['id'], j['cust_id'], j['expiry'],j['amount'], j['certificate'])
