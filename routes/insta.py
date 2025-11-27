from fastapi import APIRouter, Query
from services.insta import (
    reel_downloader,
    photo_downloader,
    carousel_downloader,
    audio_downloader,
    story_downloader,
    metadata
)

router = APIRouter(prefix="/insta", tags=["Instagram"])

@router.get("/reel")
def insta_reel(url: str = Query(..., description="Instagram Reel URL")):
    return reel_downloader.download_insta_reel(url)

@router.get("/reel/meta")
def insta_reel(url: str = Query(..., description="Instagram Reel URL")):
    return metadata.get_insta_metadata(url)

@router.get("/photo")
def insta_photo(url: str = Query(..., description="Instagram Photo URL")):
    return photo_downloader.download_insta_photo(url)

@router.get("/carousel")
def insta_carousel(url: str = Query(..., description="Instagram Carousel URL")):
    return carousel_downloader.download_insta_carousel(url)

@router.get("/reel/audio")
def insta_audio(url: str = Query(..., description="Instagram Post or Reel URL")):
    return audio_downloader.download_insta_audio(url)

@router.get("/story")
def insta_story(url: str = Query(..., description="Instagram Story URL")):
    return story_downloader.download_insta_story(url)
