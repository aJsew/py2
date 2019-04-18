import json
import yaml
import socket
import argparse

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

try:
    sock = socket.socket()
    sock.connect((host, port))

    print('Client started')

    data = input('Enter data to send: ')

    request = json.dumps(
        {'data': data}
    )

    sock.send(request.encode(encoding))
    b_data = sock.recv(buffersize)
    response = json.loads(
        b_data.decode(encoding)
    )

    print(response)

    sock.close()
except KeyboardInterrupt:
    print('Client closed')