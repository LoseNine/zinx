from ziface import Iprotocol
from twisted.internet.protocol import connectionDone

from message import Message
from datapack import DataPack

# 定义协议类
class PingProtocol(Iprotocol.ServerProtocol):

    def connectionMade(self):
        self.peer = self.transport.getPeer()
        print('[connMade]conn user:', self.peer)
        print(self.users)


    def dataReceived(self, data):
        msg=Message()
        datapack=DataPack(msg)
        msglen,msgid,msgdata=datapack.unpack(data)
        print('[Server] receive data %r from num %r , len:%r , id:%r' % (msgdata, self.peer,msglen,msgid))
        
        #根据包的ID进行router分发处理
        routerID=self.routers.apis.get(msgid,None)
        if routerID:
            #发送数据
            routerID(self.peer,self.transport)
        else:
            self.sendData(b'ping....ping....', 1)
    
    def sendData(self,data,dataid):
        msg=Message()
        msg.setMsgData(data)
        msg.setMsgId(dataid)
        
        datapack=DataPack(msg)
        data=datapack.pack()
        self.transport.write(data)
        print('[Server] write data %r to num %r' % (data, self.peer))
    
    def connectionLost(self,reason=connectionDone):
        #退出连接
        print('[connLost] connection Lost %r'%(self.transport.getPeer()))
        try:
            self.users.remove(self.transport.getPeer())
        except:
            pass
        print(self.users)

