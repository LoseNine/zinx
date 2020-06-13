from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol,connectionDone

from utils.config import Config
#定义协议类
class ServerProtocol(Protocol):
    def __init__(self,users,routers):
        self.users=users
        self.routers=routers
    
    def connectionMade(self):
        #建立连接
        pass

    def dataReceived(self, data):
        #接收数据
        self.transport.write(data)

    def connectionLost(self, reason=connectionDone):
        #退出连接
        pass

#定义工厂类
class ServerFactory(Factory):
    def __init__(self,protocol,routers):
        self.users=[]
        self.protocol=protocol
        self.routers=routers


    #进行协议分发
    def buildProtocol(self, addr):
        self.users.append(addr)
        #判断是否超过最大连接
        if len(self.users)>Config.MaxConn:
            print('[Conn] Too Many conns!')
            return 
        p = self.protocol(self.users,self.routers)
        p.factory = self
        return p
