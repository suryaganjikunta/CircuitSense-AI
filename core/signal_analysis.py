
import numpy as np

def analyze_signal(time, signal):
    t = np.asarray(time, dtype=float)
    x = np.asarray(signal, dtype=float)
    mask = np.isfinite(t) & np.isfinite(x)
    t, x = t[mask], x[mask]
    if len(t) < 4:
        raise ValueError("At least 4 valid samples are required.")
    dt = float(np.mean(np.diff(t)))
    if dt <= 0:
        raise ValueError("Time values must increase.")
    centered = x - np.mean(x)
    rms = float(np.sqrt(np.mean(centered**2)))
    peak = float(np.max(np.abs(centered)))
    p2p = float(np.max(x) - np.min(x))
    noise = float(np.std(x - np.mean(x)))
    freqs = np.fft.rfftfreq(len(centered), d=dt)
    mags = np.abs(np.fft.rfft(centered)) / len(centered)
    idx = int(np.argmax(mags[1:]) + 1) if len(mags) > 1 else 0
    return {
        "time": t, "clean_signal": x, "rms": rms, "peak": peak,
        "peak_to_peak": p2p, "noise_std": noise,
        "frequencies": freqs, "magnitudes": mags,
        "frequency": float(freqs[idx]) if len(freqs) else 0.0
    }
