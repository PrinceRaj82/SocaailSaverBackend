import yt_dlp
import json
import os
import traceback

# COOKIES_FILE = "./cookies.txt"

def video_metadata(url: str):
    """
    Universal metadata extractor for Instagram / Facebook / Reels.
    Uses yt-dlp natively (no subprocess).
    Returns complete, structured metadata with error handling.
    """
    try:
        # ---- Validate input ----
        if not url or not url.startswith(("http://", "https://")):
            return {"status": "error", "message": "Invalid URL format."}

        # if not os.path.exists(COOKIES_FILE):
            # return {"status": "error", "message": "cookies.txt file not found."}

        # ---- yt-dlp configuration ----
        ydl_opts = {
            "quiet": True,                    # Suppress logs
            "noprogress": True,               # No progress bars
            # "cookiefile": COOKIES_FILE,       # Auth session
            "skip_download": True,            # Only metadata
            "extract_flat": False,            # Get full info (not flat)
            "nocheckcertificate": True,       # Ignore SSL cert issues
            "source_address": "0.0.0.0",      # Prevent IP binding issues
            "retries": 3,                     # Retry on transient errors
            "timeout": 30,                    # Network timeout
            "geo_bypass": True,               # Bypass geo-restrictions
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        # ---- Normalize Metadata ----
        def clean(obj):
            """Ensure JSON-serializable data (avoid datetime & bytes)."""
            try:
                return json.loads(json.dumps(obj, default=str))
            except Exception:
                return str(obj)

        # ---- Handle playlists / carousels ----
        if "entries" in info and isinstance(info["entries"], list):
            entries_data = []
            for entry in info["entries"]:
                entries_data.append({
                    "id": entry.get("id"),
                    "title": entry.get("title"),
                    "duration": entry.get("duration"),
                    "thumbnail": entry.get("thumbnail"),
                    "url": entry.get("url"),
                    "ext": entry.get("ext"),
                    "format": entry.get("format"),
                    "width": entry.get("width"),
                    "height": entry.get("height"),
                })

            return {
                "status": "success",
                "type": "album",
                "count": len(entries_data),
                "post_url": url,
                "entries": entries_data,
                "raw": clean(info),
            }

        # ---- Handle single video / reel ----
        return {
            "status": "success",
            "type": "single",
            "id": info.get("id"),
            "title": info.get("title"),
            "author": info.get("uploader") or info.get("creator"),
            "upload_date": info.get("upload_date"),
            "duration": info.get("duration"),
            "description": info.get("description"),
            "view_count": info.get("view_count"),
            "like_count": info.get("like_count"),
            "comment_count": info.get("comment_count"),
            "thumbnail": info.get("thumbnail"),
            "formats": info.get("formats"),
            "webpage_url": info.get("webpage_url"),
            "raw": clean(info),
        }

    except yt_dlp.utils.DownloadError as e:
        return {"status": "error", "message": "DownloadError: " + str(e)}
    except yt_dlp.utils.ExtractorError as e:
        return {"status": "error", "message": "ExtractorError: " + str(e)}
    except Exception as e:
        traceback_str = traceback.format_exc()
        return {
            "status": "error",
            "message": str(e),
            "trace": traceback_str,
        }
