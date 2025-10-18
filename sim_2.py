import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np
#colaborated with Caydence Tatlow

@dataclass
class State:
    time: float
    xpos: float
    vel: float
    accel: float

    deltaT = 0.1
    dragFactor = 1.1 / 1000

def step(state: State) -> State:
    if state.time < 10:
        accel = 2
    elif state.vel > 0:
        accel = -4
    else: 
        accel = 0
    
    drag = -np.sign(state.vel) * (state.vel **2) * state.dragFactor
    total_accel = accel + drag

    new_vel = state.vel + total_accel * state.deltaT
    new_vel = max(new_vel, 0)
    new_xpos = state.xpos + new_vel * state.deltaT
    new_time = state.time + state.deltaT

    return State(time=new_time, xpos=new_xpos, vel=new_vel, accel=total_accel)

s0= State(time=0, xpos=0, vel=0, accel=2)

time_data = []
pos_data = []
vel_data = []

def animate (i):
    global s0
    s0 = step(s0)
    time_data.append(s0.time)
    pos_data.append(s0.xpos)
    vel_data.append(s0.vel)

    ax1.clear()
    ax2.clear()

    ax1.plot(time_data, pos_data, color='blue')
    ax1.set_ylabel("Position (m)")
    ax1.set_title("Car Motion with Drag")

    ax2.plot(time_data, vel_data, color='red')
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Velocity (m/s)")

    ax1.grid(True)
    ax2.grid(True)

    return ax1, ax2

fig, (ax1, ax2)= plt.subplots(2, 1, figsize=(5, 6))
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.tight_layout
plt.show()