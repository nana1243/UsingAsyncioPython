class Connection:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    async def __anext__(self):
        self.conn =await self.conn(self.host,self.port)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()