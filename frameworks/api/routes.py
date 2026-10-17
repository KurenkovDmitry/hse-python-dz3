from fastapi import APIRouter

from adapters.controllers.calculete_controller import CalculateController
from adapters.presenters.calculate_presenter import CalculatePresenter
from frameworks.api.schemas import CalculateRequest, CalculateResponse

def create_router(
    controller: CalculateController,
    presenter: CalculatePresenter
) -> APIRouter:
    router = APIRouter()

    @router.post("/calculate/", response_model=CalculateResponse)
    async def calculate(request: CalculateRequest):
        result, total_time, is_faster = await controller.calculate(
            request.numbers,
            request.delays
        )

        return presenter.present(result, total_time, is_faster)

    return router
