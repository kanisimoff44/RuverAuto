from fastapi import APIRouter

from app.text_pages.dao import TextPagesDAO
from app.text_pages.schemas import STextPages

# from fastapi_cache.decorator import cache


router = APIRouter(
    prefix="/text_pages",
    tags=["Текстовые страницы"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_text_page() -> STextPages | None:
    """
    Get all products

    Returns:
        list[Products]: list of products
    """
    text_page = await TextPagesDAO.get_all()

    return text_page
