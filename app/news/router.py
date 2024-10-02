from fastapi import APIRouter

from app.news.dao import NewsDAO
from app.news.schemas import SNewsAll, SNewsDetail
from app.utils import check_news_img

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
    all_news = await NewsDAO.get_all()
    for news in all_news:
        check_news_img(news)

    return all_news


@router.get("/{news_id}")
# @cache(expire=3600)
async def get_news_by_id(news_id: int) -> SNewsDetail:
    """
    Get news by id

    Args:
        prodnews_iduct_id (int): _description_

    Returns:
        SNewsDetail: _description_
    """
    news = await NewsDAO.get_by_id(news_id)
    check_news_img(news)

    return news
