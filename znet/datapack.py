from ziface.Idatapack import IdataPack
import struct
import ctypes
import binascii

from message import Message

class DataPack(IdataPack):
    def __init__(self,msg):
        self.msg=msg

    @property
    def getHeadLen(self):
        """len 4 + id 4 = 8"""
        return 8
    
    def pack(self):
        values=(self.msg.getMsgLen(),
                self.msg.getMsgId(),
                self.msg.getMsgData())

        s=struct.Struct('<ii{}s'.format(self.msg.getMsgLen()))
        prebuff=s.pack(*values)
        return prebuff

    def unpack(self,data):
        s = struct.unpack('<ii', data[:8])
        dataLen=s[0]
        dataId=s[1]
        if dataLen>0:
            afterbuff=struct.unpack('{}s'.format(dataLen),data[8:8+dataLen])[0]
        else:
            afterbuff=b''
            
        return (dataLen,dataId,afterbuff)
        