from fastapi import FastAPI
from routes.youtube import router as youtube_router
from routes.insta import router as insta_router
from routes.facebook import router as fb_router
from config.settings import settings
import uvicorn

app = FastAPI(title="FastAPI YT Microservice", version="2.0")

# Register routers
app.include_router(insta_router)
app.include_router(fb_router)
app.include_router(youtube_router)

@app.get("/")
def root():
    return {"message": "FastAPI microservice is running!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        workers=settings.WORKERS
    )
