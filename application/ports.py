from typing import Protocol

class DelayPort(Protocol):
    async def wait(self, seconds: float) -> None:
        ...
