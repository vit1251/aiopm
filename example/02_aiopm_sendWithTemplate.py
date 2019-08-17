#!/usr/bin/python3

from logging import getLogger, basicConfig, DEBUG
from aiopm import PostmarkClient
from asyncio import get_event_loop

API_TOKEN = '...'

class Application(object):
    def __init__(self):
        self.__log = getLogger('app')

    async def start(self):
        """ Start service
        """
        self._pm = PostmarkClient(server_token=API_TOKEN)
        await self._pm.sendWithTemplate(
            From='no-reply@bringreader.com',
            To='vit1251@gmail.com',
            TemplateAlias='registration',
            TemplateModel={
                'username': 'vit1251@gmail.com',
                'password': 'pa$$w0rd',
                'activate_url': 'http://example.com/activate/',
            },
        )

    async def stop(self):
        """ Stop service
        """
        pass


    def run(self):
        """ Main
        """
        self.loop = get_event_loop()
        self.loop.create_task(self.start())
        self.loop.run_forever()


if __name__ == "__main__":
    basicConfig(filename="debug.log", level=DEBUG)
    app = Application()
    app.run()
