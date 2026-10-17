from pydantic import BaseModel, Field, model_validator
from typing import Annotated

class CalculateRequest(BaseModel):
    numbers: list[float] = Field(min_length=1)
    delays: list[Annotated[float, Field(ge=0)]] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_lengths(self):
        if len(self.numbers) != len(self.delays):
            raise ValueError("Length of numbers and delays do not match")

        if any(delay < 0 for delay in self.delays):
            raise ValueError("Delay cannot be negative")

        return self

class CalculationResponse(BaseModel):
    number: float
    delay: float
    square: float
    time: float

class CalculateResponse(BaseModel):
    results: list[CalculationResponse]
    total_time: float
    parallel_faster_than_sequential: bool
