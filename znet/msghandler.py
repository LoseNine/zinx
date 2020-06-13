from ziface import Imsghandler

class IMsgHandler(Imsghandler.IMsgHandler):
    def __init__(self):
        #存放msgid对应的处理方法
        self.apis=dict()
    

    def AddRouter(self,id,router):
        """
        判断当前API对应方法是否存在
        :param id: 对应id
        :param router: id的方法
        """
        if id is self.apis.keys():
            print('[Handler] repeat api, msgId= %d'%id)
            return

        self.apis[id]=router
        print('[Handler] add api id %d successful！'%id)