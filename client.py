# Protocol TCP
# DatagramProtocol UDP
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

# Make self.id UUID4


class Client(DatagramProtocol):

    def __init__(self, host, port):
        if host == 'localhost':
            host = '127.0.0.1'
        self.address = None
        self.id = host, port
        self.server = '127.0.0.1', 9999
        print("Working on id: {}".format(self.id))

    def startProtocol(self):
        self.transport.write("ready".encode("utf-8"), self.server)

    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode("utf-8")
        if addr == self.server:
            print("Choose a clinet from these\n {}".format(datagram))
            self.address = input("write host: "), int(input("Enter port: "))
            reactor.callInThread(self.send_message)
            # addresses = datagram.split("\n")
            # self.address = addresses[int(input())]
        else:
            print("{} : {}".format(addr, datagram))

    def send_message(self):
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.address)


if __name__ == '__main__':
    port = randint(1000, 5000)
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()
