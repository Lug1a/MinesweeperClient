from socket import *
import threading
from cmd import Cmd


# 客户端socket
class TcpClientSocket(Cmd):
    def __init__(self, host, port, BUFFSIZE):
        Cmd.__init__(self)
        self.host = host
        self.port = port
        self.buffsize = BUFFSIZE
        self.addr = (self.host, self.port)

    def conn(self):
        self.tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_client_socket.connect(self.addr)

    def disconn(self):
        self.send("disconnection")

    def send(self, data):
        self.ss = data
        self.tcp_client_socket.send(self.ss.encode('utf8'))

    def rec(self):
        rdata = self.tcp_client_socket.recv(self.buffsize)
        return rdata.decode('utf8')


tcp_client_socket = TcpClientSocket('127.0.0.1', 8090, 1024 * 1024)

# def main():
#     y = TcpClientSocket('127.0.0.1', 21567, 1024)
#     y.conn()
#     while True:
#         data = input("请输入信息：")
#         y.send(data)
#         receive = y.rec()
#         print(receive)
#
#
#
# if __name__ == '__main__':
#     main()
