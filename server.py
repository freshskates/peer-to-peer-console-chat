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
            self.clients.add(address)
            self.transport.write(datagram)
