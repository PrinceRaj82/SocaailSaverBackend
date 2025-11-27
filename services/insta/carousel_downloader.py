import yt_dlp

def download_insta_carousel(url: str):
    """Fetch all images/videos in a carousel post"""
    try:
        ydl_opts = {
            "quiet": True,
            "cookies": COOKIES_FILE,
            "extract_flat": False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        entries = info.get("entries", [info])
        media = []
        for e in entries:
            media_type = "video" if e.get("ext") == "mp4" else "image"
            media.append({
                "type": media_type,
                "url": e.get("url"),
                "thumbnail": e.get("thumbnail"),
            })

        return {"status": "success", "items": media, "count": len(media)}
    except Exception as e:
        return {"status": "error", "message": str(e)}

