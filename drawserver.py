import asyncio
import websockets
from IP import ip, port

clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            for client in clients:
                if client != websocket:  # Broadcast to all other clients
                    await client.send(message)
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, ip, port):
        await asyncio.Future()  # Run forever

asyncio.run(main())