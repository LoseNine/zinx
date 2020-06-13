"""
封包，拆包 模块
面向TCP连接中的数据 处理TCP粘包问题
"""

import abc

class IdataPack(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getHeadLen(self):
        pass

    @abc.abstractmethod
    def pack(self):
        pass
    
    @abc.abstractmethod 
    def unpack(self,data):
        pass