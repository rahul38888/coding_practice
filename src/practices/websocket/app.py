#!/usr/bin/env python

import asyncio
import itertools
import json
import secrets

import websockets
from websockets import ConnectionClosedOK

from src.practices.websocket.connect4 import Connect4, PLAYER1, PLAYER2


async def loop_handler(websocket):
    while True:
        try:
            message = await websocket.recv()
            print(message)
        except ConnectionClosedOK as ex:
            print("Connection closed with code", ex.code)
            break


JOIN = {}


async def handler(websocket):
    # await loop_handler(websocket)

    join_key = ...

    game, connected = JOIN[join_key]

    connected.add(websocket)

    game = Connect4()

    connected = {websocket}

    join_key = secrets.token_urlsafe(12)
    JOIN[join_key] = game, connected

    turns = itertools.cycle([PLAYER1, PLAYER2])
    player = next(turns)

    async for message in websocket:
        print(message)
        event = json.loads(message)
        assert event['type'] == 'play'
        column = event['column']

        try:
            row = game.play(player=player, column=column)
        except RuntimeError as ex:
            event = {"type": "error", "message": str(ex)}

            await websocket.send(json.dumps(event))
            continue
        finally:
            del JOIN[join_key]

        event = {"type": "play", "player": player, "column": column, "row": row}
        await websocket.send(json.dumps(event))

        if game.winner is not None:
            event = {"type": "win", "player": game.winner}
            await websocket.send(json.dumps(event))

        player = next(turns)

    print("Connection closed. Game over!")


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
