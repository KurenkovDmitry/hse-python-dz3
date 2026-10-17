from application.calculate import CalculateUseCase

class CalculateController:
    def __init__(self, use_case: CalculateUseCase):
        self.use_case = use_case

    async def calculate(
        self,
        numbers: list[float],
        delays: list[float]
    ):
        return await self.use_case.execute(numbers, delays)
