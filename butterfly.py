import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

SIGMA=10.0
RHOW=25.0
BETA=8.0/3.0

def chaos(state,t):
    x , y , z=state
    return SIGMA*(y-x), (x * (RHOW-z)) -y , (x*y) - (BETA*z)

state = [1.0 ,1.0 ,1.0]
t=np.arange(0.0, 40.0, 0.01)
print(len(t))
states = odeint(chaos,state, t)

fig=plt.figure()
axis=fig.gca(projection = "3d")

if __name__ == '__main__':
    axis.plot(states[:,0],states[:,1],states[:,2])
    plt.draw()
    plt.show()