import abc

#定义一个服务器抽象
class IServer(metaclass=abc.ABCMeta):
    @abc.abstractmethod##定义抽象方法，无需实现功能
    def start(self):
        '开始'
        pass
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def stop(self):
        '结束'
        pass
    def server(self):
        '运行服务'
        pass
    def router(self):
        '添加协议'
        pass