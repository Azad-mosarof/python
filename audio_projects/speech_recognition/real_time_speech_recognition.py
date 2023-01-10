from time import sleep
from tkinter import W
import pyaudio
import websockets as ws
import asyncio
import base64
import json
from api import API_KEY


FRAME_PER_BUFFER=3200
FRAME_RATE=16000
CHANNELS=2
FORMAT=pyaudio.paInt16

p=pyaudio.PyAudio()

stream=p.open(
    format=FORMAT,
    channels=CHANNELS,
    frames_per_buffer=FRAME_PER_BUFFER,
    input=True,
    rate=FRAME_RATE
)

print("Start Recording....")

url="wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"

async def send_recive():
    async with ws.connect(
        url,
        ping_timeout=20,
        ping_interval=5,
        extra_headers={"Authorization":API_KEY}
    ) as _ws:
        await asyncio.sleep(0.1)
        session_begins=await _ws.recv()
        print(session_begins)
        print("Sending message")

        async def send():
            while True:
                print("Sending")
        
        async def recive():
            while True:
                pass
        
        send_result,recive_result=asyncio.gather(send(),recive())

asyncio.run(send_recive())