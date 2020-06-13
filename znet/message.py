from ziface import Imessage

class Message(Imessage.IMessage):
    def getMsgData(self):
        return self.data

    def getMsgId(self):
        return self.dataId

    def getMsgLen(self):
        return self.dataLen

    def setMsgData(self,data):
        self.data=data
        self.dataLen=len(data)

    def setMsgId(self,dataId):
        self.dataId=dataId
