from domain.entities import CalculationResult

class CalculatePresenter:
    def __init__(self):
        pass

    @staticmethod
    def present(
            results: list[CalculationResult],
        total_time: float,
        parallel_faster_than_sequential:bool
    ):
        return {
            "results": [
                {
                    "number": result.number,
                    "square": result.square,
                    "delay": result.delay,
                    "time": result.time
                }
                for result in results
            ],
            "total_time": total_time,
            "parallel_faster_than_sequential": parallel_faster_than_sequential
        }
