from fastapi import APIRouter, HTTPException, status
from schemas import SummaryResponseSchema
from utils import if_yt_video_exists

router = APIRouter(prefix="/api")


@router.get(
    "/summary", status_code=status.HTTP_200_OK, response_model=SummaryResponseSchema
)
async def generate_summary(video_id: str):
    """This route returns summary of video as JSON response."""

    # check to ensure if videoid is valid
    resp = if_yt_video_exists(video_id)
    if resp[1] == False: # yt api is down
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail="Could not generate result because YouTube API is not reachable. Try again later.",
        )

    if resp[0] == False: # yt video does not exist
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No YouTube video exists for requested video id : {video_id}",
        )
    
    return {"summary": "here will be summary", "videoid": video_id}
