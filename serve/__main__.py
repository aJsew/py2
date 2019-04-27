import json
import yaml
import socket
import select
import argparse
import threading
import logging

from handlers import handle_default_request
from settings import (
    HOST, PORT, BUFFERSIZE, ENCODING
)


host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODING

parser = argparse.ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration'
)
args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        conf = yaml.load(file, Loader=yaml.Loader)
        host = conf.get('host', HOST)
        port = conf.get('port', PORT)
        buffersize = conf.get('buffersize', BUFFERSIZE)
        encoding = conf.get('encoding', ENCODING)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('info.log', encoding=ENCODING),
        logging.StreamHandler()
    ]
)

requests = []
connections = []


def read(client, requests, buffersize):
    b_request = client.recv(buffersize)
    requests.append(b_request)


def write(client, response):
    client.send(b_response)


try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.settimeout(0)
    sock.listen(10)

    logging.info('Server started')

    while True:
        try:
            client, address = sock.accept()
            logging.info(f'Client with address { address } was detected')
            connections.append(client)
        except:
            pass

        rlist, wlist, xlist = select.select(
            connections, connections, connections, 0
        )

        for r_client in rlist:
            r_thread = threading.Thread(
                target=read,
                args=(r_client, requests, buffersize),
                daemon=True,
            )
            r_thread.start()

        if requests:
            b_request = requests.pop()
            b_response = handle_default_request(b_request)

            for w_client in wlist:
                w_thread = threading.Thread(
                    target=write,
                    args=(w_client, b_response),
                    daemon=True,
                )
                w_thread.start()

except KeyboardInterrupt:
    logging.info('Client closed')