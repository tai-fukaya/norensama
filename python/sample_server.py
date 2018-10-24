#-*-coding:utf-8-*-
# https://make-muda.net/2017/10/5645/
from websocket_server import WebsocketServer

IP='127.0.0.1'
PORT=6700

def new_client(client, server):
    print('New client {}:{} has joined.'.format(client['address'][0], client['address'][1]))
 
def message_received(client, server, message):
    print(message)

server = WebsocketServer(host=IP, port=PORT)
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()
