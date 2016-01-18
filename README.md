# Async Proxy

An asynchronous proxy in python

## Proxy with parallel connections written in Python

On execution, it would try to connect to a server, either mentioned in two commandline parameters (host and port) or the default values
at loopback ip with 8000 port and it would accept client request from ip 127.0.0.1 with port 4000.

After the client connection is added to forward, and Forward is connected to Server, the client will then have the opportunity to transfer
query messages to the server through forward. And forward will print the transfer details in the console for debugging.