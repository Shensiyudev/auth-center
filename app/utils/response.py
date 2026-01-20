from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


class ResponseContent(BaseModel):
    msg: str = Field(default='')
    data: dict = Field(default_factory=dict)
    code: int = Field(default=0)


class APIResponse:

    @classmethod
    def success200(
        cls,
        data: dict | BaseModel,
        msg: str = '',
        *,
        code: int = 0
    ) -> JSONResponse:
        """
        return 200
        :param data:
        :param msg:
        :param code:
        :return:
        """
        if isinstance(data, BaseModel):
            data = data.model_dump()

        content = ResponseContent(
            msg=msg,
            code=code,
            data=data
        )
        return JSONResponse(content.model_dump())

    @classmethod
    def bad400(
        cls,
        data: dict = None,
        msg: str = '',
        *,
        code: int = 0
    ) -> JSONResponse:
        """
        return 400
        :param data:
        :param msg:
        :param code:
        :return:
        """
        if data is None:
            data = {}
        content = ResponseContent(
            msg=msg,
            code=code,
            data=data
        )
        return JSONResponse(content.model_dump(), status_code=status.HTTP_400_BAD_REQUEST)
