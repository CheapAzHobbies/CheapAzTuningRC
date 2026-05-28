"""
Brushless motor acceleration sim for FastAzJato4x4.

Question: Castle 1412 3200KV (15T pinion) vs Castle 1415 2400KV (20T pinion),
geared to roughly the same top speed on 4S. Which accelerates faster?
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- vehicle constants ----
MASS_LB = 6.5             # FastAzJato4x4 with battery, lbs
MASS_KG = MASS_LB * 0.4536
WHEEL_DIAM_MM = 90        # ~3.5" tires
WHEEL_R = (WHEEL_DIAM_MM / 1000) / 2
INTERNAL_GEAR = 2.78      # Slash/Jato 4x4 internal trans ratio
SPUR = 50                 # teeth
CD_A = 0.012              # m^2, frontal area * drag coef (typical 1/10)
RHO = 1.225               # kg/m^3
CRR = 0.04                # rolling resistance coef (offroad-ish)
G = 9.81
EFF_DRIVETRAIN = 0.85     # mechanical efficiency

# ---- battery / esc ----
V_BATT = 14.8             # 4S nominal
I_LIMIT = 120             # ESC continuous amp limit (Fire Phoenix 120A)

# ---- motor configs (Kv, internal resistance ohms, pinion T) ----
# Resistance values from Hobbywing G3 data sheet for similar 36mm motors;
# Castle doesn't publish R, so we estimate similar based on stator size.
MOTORS = [
    {"name": "Castle 1412 3200KV (15T pinion)",   "kv": 3200, "R": 0.0055, "pinion": 15, "color": "tab:red"},
    {"name": "Castle 1415 2400KV (20T pinion)",   "kv": 2400, "R": 0.0080, "pinion": 20, "color": "tab:blue"},
    {"name": "Castle 1412 2100KV (22T pinion)",   "kv": 2100, "R": 0.0085, "pinion": 22, "color": "tab:green"},
]

def motor_torque_and_current(kv, R, V, omega_motor):
    """Return (torque N*m, current A) for given motor at given mechanical omega (rad/s)."""
    # Back-EMF: V_bemf = omega / (Kv * 2pi/60)
    # rearrange: omega_no_load [rad/s] = Kv * V * 2pi/60
    # I = (V - V_bemf) / R, but clip at I_LIMIT
    omega_no_load = kv * V * 2 * np.pi / 60
    V_bemf = V * (omega_motor / omega_no_load) if omega_no_load > 0 else 0
    I = max(0, (V - V_bemf) / R)
    I = min(I, I_LIMIT)
    # Torque: T = Kt * I; Kt [N*m/A] = 60 / (2pi * Kv)
    Kt = 60 / (2 * np.pi * kv)
    T = Kt * I
    return T, I

def simulate(motor, t_end=8.0, dt=0.001):
    pinion = motor["pinion"]
    fdr = (SPUR / pinion) * INTERNAL_GEAR
    v = 0.0
    t = 0.0
    times, speeds_mph, currents, torques, motor_rpms, powers_in, powers_out = [], [], [], [], [], [], []
    while t < t_end:
        omega_wheel = v / WHEEL_R
        omega_motor = omega_wheel * fdr
        T_motor, I = motor_torque_and_current(motor["kv"], motor["R"], V_BATT, omega_motor)
        T_wheel = T_motor * fdr * EFF_DRIVETRAIN
        F_drive = T_wheel / WHEEL_R
        F_drag = 0.5 * RHO * CD_A * v * v
        F_roll = CRR * MASS_KG * G
        F_net = F_drive - F_drag - F_roll
        a = F_net / MASS_KG
        v = max(0, v + a * dt)

        times.append(t)
        speeds_mph.append(v * 2.23694)
        currents.append(I)
        torques.append(T_wheel)
        motor_rpms.append(omega_motor * 60 / (2 * np.pi))
        powers_in.append(V_BATT * I)
        # heat dissipated in motor windings (copper loss) ~= I^2 * R
        powers_out.append(I * I * motor["R"])
        t += dt
    return {
        "t": np.array(times),
        "mph": np.array(speeds_mph),
        "I": np.array(currents),
        "T_wheel": np.array(torques),
        "motor_rpm": np.array(motor_rpms),
        "P_in": np.array(powers_in),
        "P_heat": np.array(powers_out),
        "fdr": fdr,
    }

# ---- run ----
results = [(m, simulate(m)) for m in MOTORS]

def time_to_speed(t, mph, target):
    idx = np.argmax(mph >= target)
    return t[idx] if mph[idx] >= target else None

print("\n=== Top speed and 0-x times (4S, 6.5 lb, 90mm tires, offroad surface) ===\n")
print(f"{'Motor':<40s} {'FDR':>5s} {'Vmax':>6s} {'0-20':>6s} {'0-30':>6s} {'0-40':>6s} {'PeakA':>6s} {'PeakHeat(W)':>11s}")
for m, r in results:
    vmax = r["mph"].max()
    t20 = time_to_speed(r["t"], r["mph"], 20)
    t30 = time_to_speed(r["t"], r["mph"], 30)
    t40 = time_to_speed(r["t"], r["mph"], 40)
    peak_I = r["I"].max()
    peak_heat = r["P_heat"].max()
    fmt = lambda x: f"{x:.2f}s" if x else "  n/a"
    print(f"{m['name']:<40s} {r['fdr']:>5.2f} {vmax:>5.1f}  {fmt(t20):>6s} {fmt(t30):>6s} {fmt(t40):>6s} {peak_I:>5.0f}A {peak_heat:>10.0f}W")

# ---- plots ----
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

ax = axes[0, 0]
for m, r in results:
    ax.plot(r["t"], r["mph"], color=m["color"], label=m["name"], linewidth=2)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Speed (mph)")
ax.set_title("Speed vs Time")
ax.legend(loc="lower right", fontsize=9)
ax.grid(True, alpha=0.3)

ax = axes[0, 1]
for m, r in results:
    ax.plot(r["t"], r["I"], color=m["color"], label=m["name"], linewidth=2)
ax.axhline(I_LIMIT, color="k", linestyle=":", alpha=0.5, label=f"ESC limit {I_LIMIT}A")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Motor current (A)")
ax.set_title("Motor Current Draw")
ax.legend(loc="upper right", fontsize=9)
ax.grid(True, alpha=0.3)

ax = axes[1, 0]
for m, r in results:
    ax.plot(r["t"], r["P_heat"], color=m["color"], label=m["name"], linewidth=2)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Motor heat (W copper loss = I²R)")
ax.set_title("Heat Generated in Windings")
ax.legend(loc="upper right", fontsize=9)
ax.grid(True, alpha=0.3)

ax = axes[1, 1]
for m, r in results:
    ax.plot(r["t"], r["motor_rpm"], color=m["color"], label=m["name"], linewidth=2)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Motor RPM")
ax.set_title("Motor RPM")
ax.legend(loc="lower right", fontsize=9)
ax.grid(True, alpha=0.3)

fig.suptitle(f"FastAzJato4x4 motor sim — 4S {V_BATT}V, {MASS_LB} lb, ESC limit {I_LIMIT}A", fontsize=13)
fig.tight_layout()
out = "/home/user/CheapAzTuningRC/cars/FastAzJato4x4/src/motor_sim_4s_acceleration.png"
fig.savefig(out, dpi=110)
print(f"\nplot saved -> {out}")
