from fastapi import FastAPI

app = FastAPI(title="Universal Price Watcher")


@app.get("/health")
async def health():
    return {"status": "ok"}