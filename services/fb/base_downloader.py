import yt_dlp
import json
import os
import traceback

COOKIES_FILE = "./cookies.txt"

def run_yt_dlp(url: str, opts: dict = None):
    """Core yt-dlp runner with all safety and error handling."""
    try:
        if not url.startswith(("http://", "https://")):
            return {"status": "error", "message": "Invalid URL."}

        # if not os.path.exists(COOKIES_FILE):
        #     return {"status": "error", "message": "cookies.txt file not found."}

        default_opts = {
            "quiet": True,
            "noprogress": True,
            "cookiefile": COOKIES_FILE,
            "skip_download": True,
            "nocheckcertificate": True,
            "geo_bypass": True,
            "timeout": 30,
            "retries": 3,
        }

        if opts:
            default_opts.update(opts)

        with yt_dlp.YoutubeDL(default_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        return {"status": "success", "data": json.loads(json.dumps(info, default=str))}

    except yt_dlp.utils.DownloadError as e:
        return {"status": "error", "message": "DownloadError: " + str(e)}
    except yt_dlp.utils.ExtractorError as e:
        return {"status": "error", "message": "ExtractorError: " + str(e)}
    except Exception as e:
        return {"status": "error", "message": str(e), "trace": traceback.format_exc()}
