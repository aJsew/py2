import json
import yaml
import zlib
import socket
import hashlib
import argparse
from datetime import datetime

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
parser.add_argument(
    '-m', '--mode', type=str, default='w'
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

    if args.mode == 'w':
        while True:
            hash_obj = hashlib.sha256()
            hash_obj.update(
                str(datetime.now().timestamp()).encode(ENCODING)
            )

            action = input('Enter action name: ')
            data = input('Enter data to send: ')

            request = json.dumps(
                {
                    'action': action,
                    'data': data,
                    'time': datetime.now().timestamp(),
                    'user': hash_obj.hexdigest()
                }
            )

            sock.send(
                zlib.compress(
                    request.encode(encoding)
                )
            )
    else:
        while True:
            b_data = sock.recv(buffersize)

            b_response = zlib.decompress(b_data)

            response = json.loads(
                b_response.decode(encoding)
            )

            print(response)

except KeyboardInterrupt:
    print('Client closed')
    sock.close()