import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

# --- Simple motor model: torque falls as RPM rises; power = torque * RPM * 9000 ---
@dataclass
class State:
    rpm: float
    torque: float

dt = 0.05
max_rpm = 6000
max_torque = 50.0
rpm_rate = 200.0  # RPM per second

def torque_from_rpm(rpm: float) -> float:
    # Linear drop: max at 0 RPM, ~0 at max_rpm
    return max(max_torque * (1.0 - rpm / max_rpm), 0.0)

def step(state: State) -> State:
    new_rpm = min(state.rpm + rpm_rate * dt, max_rpm)
    new_torque = torque_from_rpm(new_rpm)
    return State(new_rpm, new_torque)

def animate(i):
    global s
    s = step(s)
    power = s.torque * s.rpm * 9000  # simplified power relation

    ax.clear()
    ax.grid()
    ax.set_xlim(0, max_rpm)
    ax.set_ylim(0, max_torque)
    ax.set_xlabel("RPM")
    ax.set_ylabel("Torque (Nm)")
    ax.set_title("Motor Torque vs RPM")

    # point showing current operating point
    ax.scatter([s.rpm], [s.torque], s=80)

    # status readout
    ax.text(0.05*max_rpm, 0.85*max_torque,
            f"RPM: {s.rpm:6.0f}\nTorque: {s.torque:6.2f} Nm\nPower: {power:,.0f} (units)",
            fontsize=9)

    return ax

# --- Template-style setup ---
fig = plt.figure(figsize=(5,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(0, max_rpm)
ax.set_ylim(0, max_torque)

s = State(rpm=0.0, torque=max_torque)

ani = animation.FuncAnimation(fig, animate, interval=int(dt*1000))
plt.show()
