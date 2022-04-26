import requests
from typing import Tuple
from youtube_transcript_api import (
    NoTranscriptAvailable,
    NoTranscriptFound,
    TooManyRequests,
    TranscriptsDisabled,
    YouTubeTranscriptApi,
)

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
        if len(resp.get("items")) == 0:  # video does not exist
            return False, True
        return True, True
    except Exception as e:
        print(
            f"Failed to check if video exists using youtube api v3 with exception {e}"
        )
        return False, False


def get_subtitles(video_id: str):
    """This function return subtitles for given video_id.

    PARAMETERS:
        video_id : video id of youtube video

    RETURNS :
        dict object : {
            "success": bool,
            "message": str,
            "transcript": str,
        }
    """
    try:
        subtitles = YouTubeTranscriptApi.get_transcript(video_id=video_id)
        # format reponse object into a paragraph
        transcript = ""
        for subtitle in subtitles:
            transcript += subtitle["text"]
            transcript += " "
        return {
            "success": True,
            "message": "Subtiles generated successfully.",
            "transcript": transcript,
        }
    except TooManyRequests as e:
        return {
            "success": False,
            "message": "TooManyRequests: YouTube is receiving too many requests from this IP. Wait until the ban on server has been lifted.",
            "transcript": None,
        }
    except TranscriptsDisabled as e:
        return {
            "success": False,
            "message": "Transcripts Disabled : YouTube has disabled subtitles for this video.Summary can not be generated.",
            "transcript": None,
        }
    except NoTranscriptAvailable as e:
        return {
            "success": False,
            "message": "NoTranscripts Available : No Transcripts available for requested video id. Summary can not be generated.",
            "transcript": None,
        }
    except NoTranscriptFound as e:
        return {
            "success": False,
            "message": "NoTranscriptFound : No transcripts were found for requeseted video id. Summary can not be generated.",
            "transcript": None,
        }
    except Exception as e:
        print("Interval server error : {e} ")
        return {
            "success": False,
            "message": "Internal Server Error : Server failed to generate summary.",
            "transcript": None,
        }
