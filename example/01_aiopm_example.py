#!/usr/bin/python3

from aiopm import PostmarkClient


class Application(object):
    def __init__(self):
        self._pm = PostmarkClient(server_token='API_TOKEN')

    async def start(self):
        """ Start
        """
        await self._pm.send(
            From='sender@example.com',
            To='receiver@example.com',
            Subject='Postmark test',
            HtmlBody='<html><body><strong>Hello</strong> dear Postmark user.</body></html>'
        )

    async def stop(self):
        pass


    def run(self):
        """ Main
        """
        self.loop = get_event_loop()
        self.loop.create_task(self.start())
        self.loop.run_forewer()


if __name__ == "__main__":
    app = Application()
    app.run()
