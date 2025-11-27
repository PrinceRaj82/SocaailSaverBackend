from .base_downloader import run_yt_dlp

def downloadThumbnail(url: str):
    """Extract thumbnail image URL from any video/reel."""
    res = run_yt_dlp(url)
    if res["status"] != "success":
        return res

    info = res["data"]
    return {
        "status": "success",
        "thumbnail": info.get("thumbnail"),
        "title": info.get("title"),
        "author": info.get("uploader"),
    }
