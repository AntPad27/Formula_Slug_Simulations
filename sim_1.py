import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    xpos :float
    ypos :float
    xval :float
    yval :float
deltaT = 0.05
bounceCoeff= 0.9

def step (state:State) -> State:
    new_xpos = state.xpos + state.xval * deltaT
    new_ypos = state.ypos + state.yval * deltaT
    new_yval = state.yval - 9.81 * deltaT
    if new_ypos < 0:
        new_ypos = 0
        new_yval= new_yval * -1 * bounceCoeff
    state=State(
        xpos = new_xpos,
        ypos = new_ypos,
        xval = state.xval,
        yval = new_yval
    )

    return state

def animate (i):
    global ball1, ball2                           
    ball1 = step(ball1)
    ball2 = step(ball2)
    ax.clear()

    ax.scatter(ball1.xpos, ball1.ypos, s=200, color='blue')   
    ax.scatter(ball2.xpos, ball2.ypos, s=200, color='red')    


    ax.set_xlim(-1, 5)                           
    ax.set_ylim(0, 12)                           
    ax.set_title("Two Bouncing Balls")            
    ax.grid()
    return ax


ball1 = State(xpos=0, ypos=10.0, xval=0.1, yval=0)   
ball2 = State(xpos=2, ypos=10.0, xval=0.2, yval=0)   


fig = plt.figure(figsize=(5, 4), dpi=150)           
ax = fig.add_subplot(111)
ax.set_xlim(-1, 5)
ax.set_ylim(0, 12)
ax.grid()

ani = animation.FuncAnimation(fig, animate, interval=50) 
plt.show()