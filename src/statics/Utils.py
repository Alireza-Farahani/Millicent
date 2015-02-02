'''
Created on Jan 30, 2015

@author: AlirezaFj
'''

from hashlib import md5
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


def get_md5(*args):
    m = md5()
    for arg in args:
        # bytes takes iterable objects
        if (type(arg) == str):
            # m.update(bytes(list(arg)))
            m.update(arg.encode())
        else:
            m.update(arg)
    return md5().hexdigest()


print(get_md5("alireza"))