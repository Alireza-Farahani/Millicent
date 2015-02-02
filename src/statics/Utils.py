'''
Created on Jan 30, 2015

@author: AlirezaFj
'''

from hashlib import md5
import hmac
from entities.Node import Node
import rsa
from Crypto.Cipher import DES


def encrypt_message_deco(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def decrypt_message_deco(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def encrypt_message(msg, crypto, key, iv=''):
    if crypto == Node.RSA_CRYPTO:
        return rsa.encrypt(msg, key)

    if crypto == Node.DES_CRYPTO:
        cbc_des_cipher = DES.new(key, DES.MODE_CBC, iv)
        return cbc_des_cipher.encrypt(msg)

    if crypto == Node.AES_CRYPTO:
        return "Is it really needed ?"


def decrypt_message(msg, crypto, key, iv=''):
    if crypto == Node.RSA_CRYPTO:
        return rsa.decrypt(msg, key)

    if crypto == Node.DES_CRYPTO:
        cbc_des_decipher = DES.new(key, DES.MODE_CBC, iv)
        return cbc_des_decipher.decrypt(msg)

    if crypto == Node.AES_CRYPTO:
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

