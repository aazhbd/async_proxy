import socket

host = '127.0.0.1'
port = 8000

def process_data(input):
    if not input:
        return input
    print "Received data : " + str(input)
    reply = "Server received: " + str(input)
    print reply
    return reply

def run_server():
    s = socket.socket()
    s.bind((host,port))

    s.listen(200)
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    
    while True:
        reply = process_data(c.recv(1024))
        if not reply:
            break
        c.send(reply)
    
    c.close()

if __name__ == '__main__':
    try:
        run_server()
    except:
        print "Server stopped"
