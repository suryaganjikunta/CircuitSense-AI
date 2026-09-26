
import math

def calculate(name, **p):
    if name == "Ohm's Law":
        return p["v"] / p["r"]
    if name == "Power":
        return p["v"] * p["i"]
    if name == "Series Resistance":
        return sum(p["values"])
    if name == "Parallel Resistance":
        return 1 / sum(1 / r for r in p["values"])
    if name == "Voltage Divider":
        return p["vin"] * p["r2"] / (p["r1"] + p["r2"])
    if name == "Current Divider":
        return p["total"] * p["r2"] / (p["r1"] + p["r2"])
    if name == "KVL Loop Check":
        return sum(p["values"])
    if name == "KCL Node Check":
        return p["entering"] - p["leaving"]
    if name == "Capacitive Reactance":
        c_f = p["c"] * 1e-6
        return 1 / (2 * math.pi * p["f"] * c_f)
    if name == "Inductive Reactance":
        l_h = p["l"] * 1e-3
        return 2 * math.pi * p["f"] * l_h
    if name == "RLC Impedance":
        l_h = p["l"] * 1e-3
        c_f = p["c"] * 1e-6
        xl = 2 * math.pi * p["f"] * l_h
        xc = 1 / (2 * math.pi * p["f"] * c_f)
        return math.sqrt(p["r"]**2 + (xl - xc)**2)
    if name == "RLC Resonant Frequency":
        l_h = p["l"] * 1e-3
        c_f = p["c"] * 1e-6
        return 1 / (2 * math.pi * math.sqrt(l_h * c_f))
    if name == "AC Power Factor":
        return min(1.0, p["real"] / p["apparent"])
    if name == "RC Time Constant":
        return p["r"] * p["c"] * 1e-6
    if name == "RL Time Constant":
        return p["l"] * 1e-3 / p["r"]
    if name == "Diode Series Resistor":
        return (p["vs"] - p["vd"]) / (p["current_ma"] / 1000)
    if name == "Transformer Turns Ratio":
        return p["vp"] * p["ns"] / p["np"]
    raise ValueError("Unknown calculation")
