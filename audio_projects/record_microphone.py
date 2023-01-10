from asyncio import streams
import wave
import pyaudio

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

frames=[]
second=5

for i in range (int((FRAME_RATE/FRAME_PER_BUFFER)*second)):
    data=stream.read(FRAME_PER_BUFFER)
    frames.append(data)


stream.stop_stream()
stream.close()
p.terminate()


obj=wave.open("Output.wav","wb")
obj.setframerate(FRAME_RATE)
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.writeframes(b"".join(frames))
obj.close()