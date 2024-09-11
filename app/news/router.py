from fastapi import APIRouter

from app.news.dao import NewsDAO
from app.news.schemas import SNewsAll

router = APIRouter(
    prefix="/news",
    tags=["Новости"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_all_news() -> list[SNewsAll]:
    """
    Get all news

    Returns:
        list[SNewsAll]: list of news
    """
    news = await NewsDAO.get_all()
    return news
