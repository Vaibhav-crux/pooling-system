from fastapi import FastAPI, WebSocket
from app.routes import polls, leaderboard
from app.services.websocket_service import websocket_endpoint

app = FastAPI()

app.include_router(polls.router)
app.include_router(leaderboard.router)

@app.websocket("/ws")
async def poll_websocket(websocket: WebSocket):
    await websocket_endpoint(websocket)
