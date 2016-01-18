import socket
import thread
import sys

def run_proxy(host, port):
    print "connecting to " + str(host) + " port " + str(port)
    p = ZProxy(str(host), int(port))
    p.forward()


class ZProxy:
    # incoming connection parameters
    i_host = '127.0.0.1'
    i_port = 4000
    
    def __init__(self, f_host, f_port):
        # receive connection from client as a server
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind((self.i_host, self.i_port))
        self.ss.listen(200)
        self.in_c, self.in_addr = self.ss.accept()
        print "server listening " + str(self.i_host) + " port " + str(self.i_port)
        
        # connect to the server as a client
        self.cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cs.connect((f_host, f_port))
        
    def forward(self):
        from_client = self.in_c.recv(1024)
        self.cs.send(from_client)
        print "received from client and sent to server : " + str(from_client)
        from_server = self.cs.recv(1024)
        self.in_c.send(from_server)
        print "received from server and sent to client : " + str(from_server)
        
        while True:
            if not from_client or not from_server:
                break
            
            from_client = self.in_c.recv(1024)
            self.cs.send(from_client)
            print "received from client and sent to server : " + str(from_client)
            from_server = self.cs.recv(1024)
            self.in_c.send(from_server)
            print "received from server and sent to client : " + str(from_server)
       
        self.in_c.close()
        self.cs.close()


if __name__ == '__main__':
    try:
        host = '127.0.0.1'
        port = 8000
        
        if len(sys.argv) == 3:
            host = sys.argv[1]
            port = sys.argv[2]
        thread.start_new_thread(run_proxy(host, port))
    except:
        print "Proxy stopped."
