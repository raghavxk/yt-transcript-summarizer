import requests
from typing import Tuple
from config import settings

# env variables
YOUTUBE_API_KEY = settings.youtube_v3_api_key


def if_yt_video_exists(video_id: str) -> Tuple:
    """This function checks if a YT video exists with given videoid.

    PARAMETERS:
    video_id : video id of youtube video

    RETURNS:
        Tuple : first bool represents if video exists or not
                second bool represents if Google API is up or not.
    """

    try:
        resp = requests.get(
            f"https://www.googleapis.com/youtube/v3/videos?part=id&id={video_id}&key={YOUTUBE_API_KEY}"
        ).json()
        if len(resp.get("items"))==0: #video does not exist
            return False, True
        return True, True
    except Exception as e:
        print(
            f"Failed to check if video exists using youtube api v3 with exception {e}"
        )
        return False, False

