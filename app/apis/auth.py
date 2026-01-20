from fastapi import APIRouter

router = APIRouter()


@router.get("validate")
async def validate():
    return {"message": "OK"}
