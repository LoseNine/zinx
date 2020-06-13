import abc

#定义一个消息抽象
class IMessage(metaclass=abc.ABCMeta):
    def __init__(self):
        self.dataId=None
        self.dataLen=None
        self.data=None
    
    @abc.abstractmethod##定义抽象方法，无需实现功能
    def getMsgId(self):
        pass
    @abc.abstractmethod 
    def getMsgData(self):
        pass
    @abc.abstractmethod
    def getMsgLen(self):
        pass
    
    @abc.abstractmethod##定义抽象方法，无需实现功能
    def setMsgId(self,id):
        pass
    @abc.abstractmethod 
    def setMsgData(self,data):
        pass