from fastapi import APIRouter, Request, HTTPException, BackgroundTasks
from services.youtube_service import (
    fetch_youtube_metadata_async,
    fetch_direct_stream_url,
    fetch_audio_only_url,
    fetch_captions
)
from utils.sse_manager import sse_response
from config.settings import settings

router = APIRouter(prefix="/api/youtube", tags=["YouTube"])

# ---- SSE Metadata Endpoint ----
@router.post("/meta/sse")
async def get_metadata_sse(request: Request):
    api_key = request.headers.get("x-api-key")
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    data = await request.json()
    url = data.get("url")
    fields = data.get("fields")

    if not url:
        raise HTTPException(status_code=400, detail="Missing 'url'")

    return await sse_response(fetch_youtube_metadata_async, url, fields)

# ---- Standard endpoints ----
@router.post("/stream")
async def get_direct_stream(request: Request):
    data = await request.json()
    url = data.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="Missing URL")
    return {"stream_url": fetch_direct_stream_url(url)}

@router.post("/audio")
async def get_audio(request: Request):
    data = await request.json()
    url = data.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="Missing URL")
    return {"audio_url": fetch_audio_only_url(url)}

@router.post("/captions")
async def get_caption(request: Request):
    data = await request.json()
    url = data.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="Missing URL")
    return {"captions": fetch_captions(url)}
