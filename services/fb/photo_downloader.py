from .base_downloader import run_yt_dlp

def photoDownloader(url: str):
    """Extract image URLs (for single or carousel posts)."""
    res = run_yt_dlp(url)
    if res["status"] != "success":
        return res

    info = res["data"]
    images = []

    # Instagram carousel or multi-image posts
    if "entries" in info:
        for entry in info["entries"]:
            images.append(entry.get("url") or entry.get("thumbnail"))
    else:
        images.append(info.get("url") or info.get("thumbnail"))

    return {
        "status": "success",
        "type": "photo",
        "count": len(images),
        "images": images,
        "raw": info,
    }
