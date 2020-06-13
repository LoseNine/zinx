import abc

class IMsgHandler(metaclass=abc.ABCMeta):
    #添加
    @abc.abstractmethod
    def AddRouter(self,id,router):
        pass
