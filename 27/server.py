# -*-encoding:utf8-*-
import socketserver

#L617多线程调用self.finish_request(request, client_address)
#L342 def finish_request(self, request, client_address):
#中调用self.RequestHandlerClass(request, client_address, self)
#实例化MyServer对象
#调用P667def __init__(self, request, client_address, server):
#P673 self.handle()
class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print ("服务端启动...")
        while True:
            conn = self.request
            print (self.client_address)
            while True:
                client_data=conn.recv(1024)
                print (str(client_data, "utf8"))
                print ("waiting...")
                conn.sendall(client_data)
            conn.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8091),MyServer)
    server.serve_forever()
