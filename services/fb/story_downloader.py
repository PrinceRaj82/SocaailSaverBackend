from .base_downloader import run_yt_dlp

def downloadStory(url: str):
    """Fetch Instagram or Facebook story media."""
    res = run_yt_dlp(url)
    if res["status"] != "success":
        return res

    info = res["data"]
    stories = []

    if "entries" in info:
        for entry in info["entries"]:
            stories.append(entry.get("url"))
    else:
        stories.append(info.get("url"))

    return {
        "status": "success",
        "type": "story",
        "count": len(stories),
        "stories": stories,
        "raw": info,
    }
