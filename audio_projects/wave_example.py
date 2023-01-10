import wave

obj=wave.open("sample.wav","rb")

print("Get Channels:",obj.getnchannels())
print("get width:",obj.getsampwidth())
print("get framerate:",obj.getframerate())
print("get frames:",obj.getnframes())
print("get parameters:",obj.getparams())

print("duration:",obj.getnframes()/obj.getframerate())

frames=obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames)/4)

obj.close()

new_obj=wave.open("new_sample","wb")

new_obj.setframerate(8000)
new_obj.setnchannels(2)
new_obj.setsampwidth(2)


new_obj.writeframes(frames)

new_obj.close()
