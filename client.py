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
        print("Working on id: {}".format(self.id))

    def startConnection(self):
        self.transport.write("ready".encode("utf-8"), self.address)

    def socket_received(self, datagram, address):
        datagram = datagram.decode("utf-8")
        if address == self.address:
            print("Choose a clinet from these\n {}".format(datagram))
            self.address = input("write host: "), int(input("Enter port: "))
            reactor.callInThread(self.send_message)
            # addresses = datagram.split("\n")
            # self.address = addresses[int(input())]

        print("{} : {}".format(address, datagram))

    def send_message(self):
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.address)


if __name__ == '__main__':
    port = randint(1000, 5000)
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()
