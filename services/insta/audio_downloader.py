import yt_dlp


COOKIES_FILE = './cookies.txt'
def download_insta_audio(url: str):
    """Extract only best audio stream (native method)"""
    try:
        ydl_opts = {
            "quiet": True,
            "cookies": COOKIES_FILE,
            "format": "bestaudio/best",
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        # Find first audio-only format
        audio_format = next(
            (f["url"] for f in info.get("formats", []) if f.get("acodec") != "none" and f.get("vcodec") == "none"),
            None
        )

        return {
            "status": "success",
            "title": info.get("title"),
            "thumbnail": info.get("thumbnail"),
            "audio_url": audio_format,
            "duration": info.get("duration"),
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
