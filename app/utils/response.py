from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


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
        """
        if isinstance(data, BaseModel):
            data = data.model_dump()

        content = dict(
            msg=msg,
            code=code,
            data=data
        )
        return JSONResponse(content)

    @classmethod
    def bad400(
        cls,
        data: dict | None = None,
        msg: str = '',
        *,
        code: int = 0
    ) -> JSONResponse:
        """
        return 400
        """
        if data is None:
            data = {}
        content = dict(
            msg=msg,
            code=code,
            data=data
        )
        return JSONResponse(content, status_code=status.HTTP_400_BAD_REQUEST)
