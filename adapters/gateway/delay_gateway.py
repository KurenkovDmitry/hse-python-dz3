import asyncio

class DelayGateway:
    def __init__(self):
        pass

    @staticmethod
    async def wait(seconds: float) -> None:
        await asyncio.sleep(seconds)
