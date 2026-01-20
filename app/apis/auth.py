from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/validate")
async def validate(request: Request):
    return {"message": "OK"}
