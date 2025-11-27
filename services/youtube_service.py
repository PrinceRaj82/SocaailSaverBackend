from yt_dlp import YoutubeDL
import threading, asyncio, json
from random import choice

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/118.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X)",
]

ua_lock = threading.Lock()

def get_next_user_agent():
    with ua_lock:
        return choice(USER_AGENTS)

# SSE-compatible async generator (progress updates)
async def fetch_youtube_metadata_async(url, fields=None):
    headers = {"User-Agent": get_next_user_agent()}
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "socket_timeout": 5,
        "http_headers": headers,
    }
    await asyncio.sleep(0.2)
    yield json.dumps({"status": "Fetching metadata..."})

    await asyncio.sleep(0.3)
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    await asyncio.sleep(0.3)
    yield json.dumps({"status": "Metadata fetched!"})

    if fields:
        info = {key: info.get(key) for key in fields if key in info}

    yield json.dumps({"data": info})

# Synchronous versions (for internal use)
def fetch_direct_stream_url(url):
    headers = {"User-Agent": get_next_user_agent()}
    ydl_opts = {"quiet": True, "format": "best", "skip_download": True, "http_headers": headers}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("url")

def fetch_audio_only_url(url):
    headers = {"User-Agent": get_next_user_agent()}
    ydl_opts = {"quiet": True, "format": "bestaudio", "skip_download": True, "http_headers": headers}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("url")

def fetch_captions(url, formats=["json", "srt", "vtt"]):
    headers = {"User-Agent": get_next_user_agent()}
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en", "hi", "auto"],
        "http_headers": headers,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        subs = info.get("subtitles", {}) or info.get("automatic_captions", {})
        captions_result = {}
        for lang, subs_data in subs.items():
            for sub in subs_data:
                ext = sub.get("ext")
                if ext in formats:
                    captions_result.setdefault(lang, []).append(sub["url"])
    return captions_result
