import yt_dlp
COOKIES_FILE = "./cookies.txt"

def download_insta_photo(url: str):
    """Get single/multiple images from a post"""
    try:
        ydl_opts = {
            "quiet": True,
            "cookiefile": COOKIES_FILE,
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        entries = info.get("entries", [info])
        photos = [e.get("url") for e in entries if e.get("url")]

        return {"status": "success", "photo_urls": photos, "count": len(photos)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
