from typing import Optional

from fastapi import APIRouter

from app.main_content.dao import MainContentDAO
from app.main_content.schemas import SMainContent

# from fastapi_cache.decorator import cache


router = APIRouter(
    prefix="/main_content",
    tags=["Контент"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_content() -> Optional[SMainContent]:
    """
    Get all products

    Returns:
        list[Products]: list of products
    """
    content = await MainContentDAO.get_all()
    if content:
        content.images = content.images[0].split("/")[-1]

    return content
