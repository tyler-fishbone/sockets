from datetime import datetime
import socket

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP
)

PORT = 3000
address = ('127.0.0.1', PORT)

sock.bind(address)

sock.listen(1)

print('--- Starting server on port {} at {} ---'.format(PORT, datetime.now()))
try:
    conn, addr = sock.accept()

    buffer_length = 8

    message_complete = False

    msg = b''

    while not message_complete:
        part = conn.recv(buffer_length)
        msg += part
        if b'$%^&()' in msg:
            break


    recieved_message = msg[:-6].decode('utf8')

    message = recieved_message + '$%^&()'

    conn.sendall(message.encode('utf8'))
    print('[{}] Echoed : {}'.format(datetime.now(), recieved_message))

    conn.close()

    sock.close()

    print('--- Stopping server on port {} at {} ---'.format(PORT, datetime.now()))
except KeyboardInterrupt:
    print('You have closed down the server with an keyboard interrupt.')