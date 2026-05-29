import numpy as np
from dataclasses import dataclass

@dataclass
class PulseConfig:
    amplitude: float
    duration: float
    sigma: float = 0.0  
    phase: float = 0.0

def gaussian_envelope(t: float, args: dict) -> float:
    amp, duration = args.get('amplitude', 1.0), args.get('duration', 10.0)
    sigma = args.get('sigma', duration / 4.0)
    return amp * np.exp(-0.5 * ((t - (duration / 2.0)) / sigma) ** 2)