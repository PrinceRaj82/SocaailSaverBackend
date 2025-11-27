# services/insta/shared.py
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
COOKIE_PATH = os.path.join(PROJECT_ROOT, "cookie.txt")

# services/insta/shared.py  (add to file)
def pick_best_audio_url(formats):
    # choose format that has audio (acodec not 'none') and highest abr or filesize
    audio_formats = [f for f in formats if f.get("acodec") and f.get("acodec") != "none"]
    if not audio_formats:
        # sometimes audio is present in 'url' of a single-format info, fall back
        return None
    # sort by abr then filesize then bitrate
    def score(f):
        abr = f.get("abr") or 0
        asr = f.get("asr") or 0
        size = f.get("filesize") or 0
        return (abr, asr, size)
    best = max(audio_formats, key=score)
    return best.get("url")
