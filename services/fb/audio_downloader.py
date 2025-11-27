from .base_downloader import run_yt_dlp

def download_audio(url: str):
    """Extract best audio stream URL."""
    opts = {"format": "bestaudio"}
    res = run_yt_dlp(url, opts)

    if res["status"] != "success":
        return res

    info = res["data"]
    audio = next((f for f in info.get("formats", []) if f.get("vcodec") == "none"), None)

    return {
        "status": "success",
        "type": "audio",
        "title": info.get("title"),
        "duration": info.get("duration"),
        "download_url": audio.get("url") if audio else None,
        "ext": audio.get("ext") if audio else "mp3",
        "raw": info,
    }
