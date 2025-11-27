from .base_downloader import run_yt_dlp

def videoDownloader(url: str):
    """Download normal Facebook video or return metadata."""
    res = run_yt_dlp(url)
    if res["status"] != "success":
        return res

    info = res["data"]
    formats = [f for f in info.get("formats", []) if f.get("height")]
    best = max(formats, key=lambda f: f["height"], default=None)


    return {
        "status": "success",
        "type": "video",
        "title": info.get("title"),
        "author": info.get("uploader"),
        "thumbnail": info.get("thumbnail"),
        "duration": info.get("duration"),
        "resolution": best.get("format_note") if best else None,
        "download_url": best.get("url") if best else None,
        "raw": info,
    }
