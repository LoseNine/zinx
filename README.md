# Zinx
使用Twisted引擎实现Zinx框架

`server.py`
```python
from msghandler import IMsgHandler
from message import Message
from datapack import DataPack
from server import Server


def handleData(addr,transport):
    msg = Message()
    msg.setMsgData(b'Test msg python')
    msg.setMsgId(0)

    datapack = DataPack(msg)
    data = datapack.pack()
    transport.write(data)
    print('[Server] write data %r to addr %r' % (data, addr))


if __name__ == '__main__':
    #添加不同id处理方法
    routers=IMsgHandler()
    routers.AddRouter(0, handleData1)
    
    serve = Server(routers=routers)
    serve.server()

```

`client.py`
```python
from __future__ import print_function

from twisted.internet import reactor, protocol
from message import Message
from datapack import DataPack

# a client protocol

class EchoClient(protocol.Protocol):

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

```

`config.py`
```python
class Config:
    Host='127.0.0.1'
    Port=8080
    Name='Zinx Server'

    Version='ipv4'
    MaxConn=1

```
