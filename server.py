# Protocol TCP
# DatagramProtocol UDP
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint


class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()

    def datagramReceived(self, datagram, address):
        datagram = datagram.decode('utf-8')
        if(datagram == "ready"):
            addresses = "\n".join([str(x) for x in self.clients])
            self.transport.write(addresses.encode("utf-8"), address)
            self.clients.add(address)


if __name__ == "__main__":
    port = 9999
    reactor.listenUDP(port, Server())
    reactor.run()
