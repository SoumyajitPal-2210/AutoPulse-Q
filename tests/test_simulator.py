import pytest
import numpy as np
from autoqcal.physics.simulator import QubitSimulator

def dummy_square_envelope(t: float, args: dict) -> float:
    duration = args.get('duration', 10.0)
    return args.get('amplitude', 1.0) if 0 <= t <= duration else 0.0

def test_ideal_qubit_inversion():
    sim = QubitSimulator(t1=0.0, t2_star=0.0)
    duration = 10.0
    amp = np.pi / duration
    result = sim.run_driven_evolution(duration=duration, detuning=0.0, pulse_func=dummy_square_envelope, pulse_args={'amplitude': amp, 'duration': duration})
    assert result.expect[0][-1] == pytest.approx(-1.0, abs=1e-4)