# headsortails
Implement heads or tails server to brush up the network/socket programming in python.


Network Programming Refresher
1. socket level
2. already implemented high level protocols HTTP, FTP.

I will dive into socket level for now...

What is a socket?
Consider a bidirectional communication channel, the sockets are the endpoints of this communication channel.

Basically a socket is like a file descriptor. like normal file. But it is created in kernel level. data is written into it permanently and once connection is killed, this data is gone also.

Socket API:
import socket
socket.socket(socket_family, socket_type, protocol=0)

Server methods:
	bind
	listen
	accept
Client methods:
	connect

General methods:
	send
	sendto
	recv
	recvfrom
	close
	ghostname



How Servers work generally:
create a socket
bind
listen
while True
	accept
	send
	close


telnet localhost 12345 to connect to this server.


Small projects todo:
1.write a simple socket-level heads/tail server.

telnet 1234 
HEAD [HIT ENTER]
** server flips a coin and responds**
you are right / you are wrong

2.write simple HTTP server
TODO

3.write simple DNS server
TODO
