# Protocol TCP
# DatagramProtocol UDP
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

# Make self.id UUID4


class Client(DatagramProtocol):
    def __init__(self, host, port):
        self.id = 2
