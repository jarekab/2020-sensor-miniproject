#!/usr/bin/env python3
"""
WebSockets server

This program generates simulated data for multiple rooms, with multiple sensors per room.

The default behavior is to be only visible on the computer itself by parameter "localhost"
so that no firewall edits are needed.

The port number is arbitrary, as long as the server and client are on the same port all is well.

Naturally, this server must be started before the client(s) attempt to connect.
"""

import argparse
import asyncio
import websockets
from sp_iotsim import iot_handler


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="WebSocket server")
    p.add_argument("host", help="Host address", nargs="?", default="localhost")
    p.add_argument("port", help="network port", nargs="?", type=int, default=8765)
    P = p.parse_args()

    print(f"SERVER: {P.host} port {P.port}")
    start_server = websockets.serve(
        iot_handler,
        host=P.host,
        port=P.port,
        compression=None,
        max_size=2 ** 12,
        read_limit=2 ** 10,
        max_queue=4,
    )

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
