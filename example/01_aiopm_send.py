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
        await self._pm.send(
            From='no-reply@example.com',
            To='vit1251@gmail.com',
            Subject='Postmark test',
            HtmlBody='<html><body><strong>Hello</strong> dear Postmark user.</body></html>'
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
