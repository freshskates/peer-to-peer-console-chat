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
        self.id = host, port
        self.address = None
        print("Working on id: {}".format(self.id))

    def socket_received(self, datagram, address):
        print("{} : {}".format(address, datagram))

    def send_message(self):
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.address)


if __name__ == '__main__':
    port = randint(1000, 5000)
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()
