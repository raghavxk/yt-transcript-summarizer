from fastapi import APIRouter, status
from schemas import SummaryResponseSchema

router = APIRouter(prefix="/api")


@router.get(
    "/summary",
    status_code=status.HTTP_200_OK,
    response_model=SummaryResponseSchema
)
async def generate_summary(videoid: str):
    """This route returns summary of video as JSON response."""

    return {"summary": "here will be summary", "videoid": videoid}
