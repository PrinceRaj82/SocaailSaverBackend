import yt_dlp

COOKIES_FILE = "./cookies.txt"

def get_insta_metadata(url: str):
    """Fetch complete metadata (for Reels, posts, or albums) using yt-dlp."""
    try:
        ydl_opts = {
            "quiet": True,
            "cookiefile": COOKIES_FILE,
            "skip_download": True,
            "extract_flat": False,  # ensures we get detailed info, not just URLs
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        # Handle both single video and multiple entries (carousel posts)
        if "entries" in info:  
            entries_data = []
            for entry in info["entries"]:
                entries_data.append({
                    "id": entry.get("id"),
                    "title": entry.get("title"),
                    "url": entry.get("url"),
                    "duration": entry.get("duration"),
                    "width": entry.get("width"),
                    "height": entry.get("height"),
                    "ext": entry.get("ext"),
                    "format": entry.get("format"),
                    "thumbnail": entry.get("thumbnail"),
                })
            return {
                "status": "success",
                "type": "album",
                "post_url": url,
                "count": len(entries_data),
                "entries": entries_data,
                "full_metadata": info,  # includes everything yt-dlp extracted
            }

        # For single reel/post
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
            "tags": info.get("tags"),
            "thumbnail": info.get("thumbnail"),
            "formats": info.get("formats"),
            "webpage_url": info.get("webpage_url"),
            "full_metadata": info,  # return everything for debugging or future use
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
import yt_dlp

COOKIES_FILE = "./cookies.txt"

def get_insta_metadata(url: str):
    """Fetch complete metadata (for Reels, posts, or albums) using yt-dlp."""
    try:
        ydl_opts = {
            "quiet": True,
            "cookiefile": COOKIES_FILE,
            "skip_download": True,
            "extract_flat": False,  # ensures we get detailed info, not just URLs
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        # Handle both single video and multiple entries (carousel posts)
        if "entries" in info:  
            entries_data = []
            for entry in info["entries"]:
                entries_data.append({
                    "id": entry.get("id"),
                    "title": entry.get("title"),
                    "url": entry.get("url"),
                    "duration": entry.get("duration"),
                    "width": entry.get("width"),
                    "height": entry.get("height"),
                    "ext": entry.get("ext"),
                    "format": entry.get("format"),
                    "thumbnail": entry.get("thumbnail"),
                })
            return {
                "status": "success",
                "type": "album",
                "post_url": url,
                "count": len(entries_data),
                "entries": entries_data,
                "full_metadata": info,  # includes everything yt-dlp extracted
            }

        # For single reel/post
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
            "tags": info.get("tags"),
            "thumbnail": info.get("thumbnail"),
            "formats": info.get("formats"),
            "webpage_url": info.get("webpage_url"),
            "full_metadata": info,  # return everything for debugging or future use
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
