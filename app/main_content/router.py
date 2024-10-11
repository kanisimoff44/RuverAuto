from fastapi import APIRouter
# from fastapi_cache.decorator import cache

from app.main_content.dao import MainContentDAO
from app.main_content.schemas import SMainContent

router = APIRouter(
    prefix="/main_content",
    tags=["Контент"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_content() -> SMainContent | None:
    """
    Get all products

    Returns:
        list[Products]: list of products
    """
    content = await MainContentDAO.get_all()

    return content
