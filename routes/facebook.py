from fastapi import APIRouter, Query
from services.fb import (
    reel_downloader,
    video_downloader,
    photo_downloader ,
    reel_downloader,
    base_downloader,
    audio_downloader,
    thumbnail_downloader,
    story_downloader,
    metadata
)

router = APIRouter(prefix="/fb", tags=["facebook"])

@router.get("/video")
def facebook_video(url: str = Query(..., description="facebook video downloader")):
    return video_downloader.videoDownloader(url)

@router.get("/reel")
def facebook_reel(url: str = Query(..., description="facebook Reel Downloader")):
    return reel_downloader.videoDownloader(url)

@router.get("/video/meta")
def videoMetadata(url: str = Query(..., description="facebook video metadata")):
    return metadata.video_metadata(url)

@router.get("/reel/meta")
def videoMetadata(url: str = Query(..., description="facebook reel metadata")):
    return metadata.video_metadata(url)

@router.get("/thumbnail")
def facebook_thumbnail(url: str = Query(..., description="facebook video URL and get thumbnail url")):
    return thumbnail_downloader.downloadThumbnail(url)

@router.get("/photo")
def facebook_photo(url: str = Query(..., description="facebook photo URL")):
    return photo_downloader.photoDownloader(url)

@router.get("/video/audio")
def insta_audio(url: str = Query(..., description="facebook video audio URL")):
    return audio_downloader.download_audio(url)

@router.get("/story")
def facebook_story(url: str = Query(..., description="facebook Story URL")):
    return story_downloader.downloadStory(url)

@router.get("/all")
def all(url: str = Query(..., description="Instagram Story URL")):
    return base_downloader.run_yt_dlp(url)
@router.get("/test")
def all():
    return "running done "
