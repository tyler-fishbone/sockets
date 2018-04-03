import socket, sys

infos = socket.getaddrinfo('127.0.0.1', 3000)

stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

client = socket.socket(*stream_info[:3])

client.connect(stream_info[-1])

# print(sys.argv)
if len(sys.argv) > 1:
    cli_input_message = ' '.join(sys.argv[1:])
    message = cli_input_message + '$%^&()'
    print(len(sys.argv))
else:
    message = input('Enter the message you would like the server to echo: ') + '$%^&()'

client.sendall(message.encode('utf8'))
# print('message sent')

buffer_length = 8

message_complete = False

msg = b''

while not message_complete:
    part = client.recv(buffer_length)
    msg += part
    if b'$%^&()' in msg:
        break

print(msg[:-6].decode('utf8'))

client.close()