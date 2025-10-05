from datetime import datetime

from pydantic import BaseModel, field_validator, ValidationError

from errors import HttpError


class BaseAdvirtisementModel(BaseModel):
    header: str
    comment: str
    created_at: datetime | None = None
    owner: str

    @field_validator('header')
    @classmethod
    def header_length(cls, value: str):
        if len(value) > 100:
            raise ValueError("Header must be less than 100 characters")
        return value


class CreateAdvertisementRequest(BaseAdvirtisementModel):
    pass


class UpdateAdvertisementRequest(BaseAdvirtisementModel):
    header: str | None = None
    comment: str | None = None
    owner: str | None = None


def validate(
        schema: type[CreateAdvertisementRequest | UpdateAdvertisementRequest],
        json_data: dict
) -> dict:
    try:
        schema_instance = schema(**json_data)
        return schema_instance.model_dump(exclude_unset=True)
    except ValidationError as e:
        errors = e.errors()
        for error in errors:
            error.pop("ctx", None)
        raise HttpError(400, errors)