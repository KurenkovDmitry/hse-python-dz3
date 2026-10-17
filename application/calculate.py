import asyncio
from time import perf_counter

from application.ports import DelayPort
from domain.services import square
from domain.entities import CalculationResult


class CalculateUseCase:
    def __init__(self, delay: DelayPort):
        self.delay = delay

    async def execute(
        self,
        numbers: list[float],
        delays: list[float]
    ) -> tuple[list[CalculationResult], float, bool]:

        async def calculate_one(number: float, delay: float):
            start = perf_counter()
            await self.delay.wait(delay)

            return CalculationResult(
                number=number,
                square=square(number),
                delay=delay,
                time=round(perf_counter() - start, 2)
            )

        start = perf_counter()

        results = await asyncio.gather(
            *(calculate_one(number, delay) for number, delay in zip(numbers, delays)),
        )

        total_time = round(perf_counter() - start, 2)

        return (
            results,
            total_time,
            total_time < sum(delays)
        )
