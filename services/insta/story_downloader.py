import yt_dlp


def download_insta_story(url: str):
    """Get all story URLs (supports multiple stories)"""
    try:
        ydl_opts = {
            "quiet": True,
             'cookiefile': './cookies.txt',
            "format": "best",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        stories = []
        if "entries" in info:
            stories = [e.get("url") for e in info["entries"] if e.get("url")]
        elif info.get("url"):
            stories = [info.get("url")]

        return {"status": "success", "stories": stories, "count": len(stories)}
    except Exception as e:
        return {"status": "error", "message": str(e)}

