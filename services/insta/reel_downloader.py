
import yt_dlp
COOKIES_FILE = "./cookies.txt"


# ---------- 1️⃣ Reel / Video ----------
def download_insta_reel(url: str):
    """Get Instagram reel with full audio (best format)"""
    try:
        ydl_opts = {
            "quiet": True,
            "cookiefile": COOKIES_FILE,
            "format": "best",  # best video+audio muxed
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        # Get the best muxed stream
        video_url = None
        for f in reversed(info.get("formats", [])):
            if f.get("vcodec") != "none" and f.get("acodec") != "none":
                video_url = f["url"]
                break

        return {
            "status": "success",
            "title": info.get("title"),
            "author": info.get("uploader"),
            "thumbnail": info.get("thumbnail"),
            "video_url": video_url,
            "duration": info.get("duration"),
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

