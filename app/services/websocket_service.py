from fastapi import WebSocket
from app.utils.kafka_utils import process_vote

connected_websockets = set()

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_websockets.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await process_vote(data, connected_websockets)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        connected_websockets.remove(websocket)

async def process_vote(vote_data: str, websockets):
    # Implement the vote processing logic here
    pass
