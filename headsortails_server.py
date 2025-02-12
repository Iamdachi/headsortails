import socket, random

def flip_coin():
    bit = random.randrange(2)
    coin = b''
    
    if bit == 1:
        coin = b'head\r\n'
    else:
        coin = b'tail\r\n'
    return coin

s = socket.socket()

port = 1234

s.bind(('', 12348))

s.listen()

while True:
    c, addr = s.accept()
    c.send(b'Welcome to my server! type head or tail! nothing else!\r\n')
    
    # input guess
    guess = c.recv(1024)
    while guess != b'head\r\n' and guess != b'tail\r\n':
        c.send(b'type head or tail! nothing else!\r\n')
        guess = c.recv(1024)
    
    coin = flip_coin()
    
    if coin == guess:
        c.send(b'You are Right!!!!\r\n')
    else:
        c.send(b'Oh no!!! Bad luck :(\r\n')
    
    c.close()

