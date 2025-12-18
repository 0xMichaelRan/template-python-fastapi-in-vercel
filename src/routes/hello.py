from fastapi import APIRouter

from src.dtos.ISayHelloDto import ISayHelloDto

router = APIRouter(prefix="/hello", tags=["hello"])


@router.get("/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.post("")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}
