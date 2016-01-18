import socket

host = '127.0.0.1'
port = 4000

def run_client():
    s = socket.socket()
    s.connect((host, port))

    message = raw_input("Client Message : ")
    
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print 'Server Says : ' + str(data)
        message = raw_input("Client Message : ")
    
    s.close()

if __name__ == '__main__':
    run_client()
