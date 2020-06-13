"""
An example client. Run simpleserv.py first before running this.
"""
from __future__ import print_function

from twisted.internet import reactor, protocol
from message import Message
from datapack import DataPack

# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):
        m=Message()
        s=b"Test msg"
        m.setMsgData(s)
        m.setMsgId(1)
        
        d=DataPack(m).pack()
        self.transport.write(d)

    def dataReceived(self, data):
        msg = Message()
        datapack = DataPack(msg)
        msglen, msgid, msgdata = datapack.unpack(data)
        print('[Client] receive data %r from server, len:%r , id:%r' % (msgdata,msglen, msgid))

    def connectionLost(self, reason):
        print("connection lost")


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 8080, f)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
