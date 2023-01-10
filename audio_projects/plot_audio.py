from os import times
import wave
import matplotlib.pyplot as plt
import numpy as np

obj=wave.open("new_sample","rb")

obj_frquency=obj.getframerate()
obj_frames=obj.getnframes()
signal_wave=obj.readframes(-1)

obj.close()

duration=obj_frames/obj_frquency
print(duration)
print(obj_frames)
print(len(signal_wave))

signal_wave=np.frombuffer(signal_wave,dtype=np.int16)

times=np.linspace(0,duration,num=len(signal_wave))

plt.plot(times,signal_wave)
plt.xlabel("Time")
plt.ylabel("signal wave")
plt.title("Audio signal plot")
plt.xlim(0,duration)
plt.show()