from .base_downloader import run_yt_dlp

def videoDownloader(url: str):
    """Download or extract reel metadata and direct URLs."""
    res = run_yt_dlp(url)
    if res["status"] != "success":
        return res

    info = res["data"]
    best_format = next(
        (f for f in info.get("formats", []) if f.get("vcodec") != "none"), None
    )

    return {
        "status": "success",
        "type": "reel",
        "title": info.get("title"),
        "author": info.get("uploader"),
        "thumbnail": info.get("thumbnail"),
        "duration": info.get("duration"),
        "view_count": info.get("view_count"),
        "download_url": best_format.get("url") if best_format else None,
        "raw": info,
    }
