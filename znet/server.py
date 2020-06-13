from ziface import Iserver,Iprotocol

from twisted.internet import selectreactor
selectreactor.install()

from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

#自定义协议
from protocol import PingProtocol

#路由定制
from msghandler import IMsgHandler

#配置
from utils.config import Config

#实现服务器
class Server(Iserver.IServer):
    def __init__(self,name=Config.Name,
                   ipversion=Config.Version,
                   ip=Config.Host,
                   port=Config.Port,

                   protocol=PingProtocol,
                   routers=None):
        self.name=name
        self.ipversion=ipversion
        self.ip=ip
        self.port=port
        self.protocol=protocol
        self.routers=routers

    def start(self):
        "启动 "
        """
        1.TCP address
        2.监听服务器地址
        3.阻塞等待客户端链接
        """
        print('[Zinx] Server Listen at IP:%s Port:%d'%(self.ip,self.port))
        if self.ipversion=='ipv4':
            endpoint=TCP4ServerEndpoint(reactor,
                                        port=self.port,
                                        interface=self.ip)

            endpoint.listen(Iprotocol.ServerFactory(self.protocol,self.routers))
            print('[Zinx] %s is running!'%self.name)
            print('[Zinx] Version is %s'%Config.Version)
            print('[Zinx] Max connection is %d'%Config.MaxConn)


            reactor.run()

        else:
            print('[Start] IPVersion Error')

    def stop(self):
        "停止 释放资源状态链接"
        reactor.stop()

    def server(self):
        "运行"
        self.start()


def newServer():
    serve=Server(name=Config.Name,
                 ipversion=Config.Version,
                 ip=Config.Host,
                 port=Config.Port,

                 protocol=PingProtocol,
                 routers=None)
    return serve
