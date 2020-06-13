from msghandler import IMsgHandler
from message import Message
from datapack import DataPack
from server import Server


def handleData1(addr,transport):
    msg = Message()
    msg.setMsgData(b'Test msg python')
    msg.setMsgId(0)

    datapack = DataPack(msg)
    data = datapack.pack()
    transport.write(data)
    print('[Server] write data %r to addr %r' % (data, addr))

def handleData2(addr,transport):
    msg = Message()
    msg.setMsgData(b'Test msg go')
    msg.setMsgId(1)

    datapack = DataPack(msg)
    data = datapack.pack()
    transport.write(data)
    print('[Server] write data %r to addr %r' % (data, addr))

if __name__ == '__main__':
    #添加不同id处理方法
    routers=IMsgHandler()
    routers.AddRouter(0, handleData1)
    routers.AddRouter(1, handleData2)
    
    serve = Server(routers=routers)
    serve.server()