__author__ = 'alirezasadeghi'

import errno
import functools
from tornado import ioloop
import socket
import random
import traceback
import sys




customer_port_number = random.randint(1235, 50000)
BROKER_PORT = 1234


















print("#################### Creating broker socket #########################")
broker_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    broker_sock.connect(("127.0.0.1", BROKER_PORT))
except socket.error as errmsg:
    traceback.print_exc()
    print("Something bad happened when trying to connect to broker.")
    sys.exit()


print("#################### Creating vendor socket #########################")

vendor_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
vendor_sock.setblocking(0)

while vendor_port_number != -1:
    vendor_port_number = input("Enter vendor port to connect to?")
    try:
        vendor_sock.connect(("127.0.0.1", vendor_port_number))
    except socket.error as e:
        traceback.print_exc()
        vendor_port_number = random.randint(1235, 50000)
        continue

### Acts as broker to customers requests
customer_sock.listen(128)
print("#################### Customer socket bound #########################")

io_loop = ioloop.IOLoop.instance()
callback = functools.partial(customer_connection_ready, customer_sock)
print("#################### Attaching customer callback #1 #########################")
io_loop.add_handler(customer_sock.fileno(), callback, io_loop.READ)
print("#################### Attached customer callback #1 #########################")

