from entities.Scrip import Scrip
from entities.Message import ResponseBrokerScrip, Message, ResponseVendorScrip, RequestBrokerScrip, RequestVendorScrip

import errno
import functools
from tornado import ioloop
import socket
from datetime import datetime, timedelta
import json
from random import sample



BROKER_PORT = 1234
used_scripsIDs = []
valid_scripsIDs = sample(range(0, 0xFFFFFFFF), 1000)
BROKER_ID = 1


def handle_connection(connection, address, arg):
    # print("#################### Callback #2 Called !!! :D #########################")
    message = connection.recv(1024)
    print("msg received : ", message)

    msg = process_msg(message)

    if msg.get('type', '') == RequestBrokerScrip.__name__:
        ###
        ### Sequence Number 1 -- No encryption required
        ###

        scrip = Scrip(vendor_id="", id=generate_scripID(), cust_id=msg.get('sender'),
                      expiry=get_scrip_expiry(), amount=msg["data"][0])

        scrip_packet = ResponseBrokerScrip(id, msg["sender"], scrip)
        send_msg(scrip_packet, connection)


    elif msg.get('type', '') == RequestVendorScrip.__name__:
        vendor_id = msg["data"][0]
        vendor_scrip_amount = parse_scrip(msg["data"][1])
        broker_scrip = parse_scrip(msg["data"][2])
        cust_id = msg["sender"]

        vendor_scrip = Scrip(vendor_id, generate_scripID(), cust_id, get_scrip_expiry(), vendor_scrip_amount)

        broker_change_scrip = Scrip("", generate_scripID(), cust_id, get_scrip_expiry(),
                                    broker_scrip.amount - vendor_scrip_amount)

        used_scripsIDs.append(broker_scrip.id)

        send_msg(ResponseVendorScrip(id, cust_id, vendor_scrip, broker_change_scrip), connection)


def connection_ready(sock, fd, events):
    while True:
        try:
            # print("#################### Connection received #########################")
            connection, address = sock.accept()
            # print("#################### Connection established #########################")
        except socket.error as e:
            if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return

        connection.setblocking(0)
        tmp_callback = functools.partial(handle_connection, connection)
        # print("#################### Attaching callback #2 #########################")
        io_loop.add_handler(connection.fileno(), tmp_callback, io_loop.READ)
        # print("#################### Callback #2 Attached #########################")


def parse_scrip(string):
    pass


def get_scrip_expiry():
    return int(datetime.now() + timedelta())


def generate_scripID():
    id = valid_scripsIDs.pop()
    used_scripsIDs.append(id)
    return id

def process_msg(message):
    '''
         Splits the message into parts specified by ------ line
    '''
    msg = json.loads(message)
    return msg
    # msg = dict(zip(["type", "sender", "receiver", "data"], message.split("---")))
    # msg["data"] = msg["data"].split(Message.data_seg)
    # return msg


def send_msg(message, socket, crypto=None, key=None):
    '''
    sends the message into network. receiver
    '''

    socket.send(message.as_json().encode('utf-8'))


# print("#################### Creating socket #########################")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(0)
sock.bind(("", BROKER_PORT))
sock.listen(128)

# print("#################### Socket bound #########################")
#
# print("#################### Attaching callback #1 #########################")

io_loop = ioloop.IOLoop.instance()
callback = functools.partial(connection_ready, sock)
io_loop.add_handler(sock.fileno(), callback, io_loop.READ)

# print("#################### Callback #1 attached #########################")
io_loop.start()
