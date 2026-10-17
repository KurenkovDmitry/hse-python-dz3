from fastapi import FastAPI

from application.calculate import CalculateUseCase
from adapters.controllers.calculete_controller import CalculateController
from adapters.presenters.calculate_presenter import CalculatePresenter
from adapters.gateway.delay_gateway import DelayGateway
from frameworks.api.routes import create_router

app = FastAPI()

gateway = DelayGateway()
use_case = CalculateUseCase(gateway)
controller = CalculateController(use_case)
presenter = CalculatePresenter()

app.include_router(create_router(controller, presenter))
