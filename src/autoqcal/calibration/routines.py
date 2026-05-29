import numpy as np
from scipy.optimize import minimize
from autoqcal.physics.simulator import QubitSimulator
from autoqcal.control.pulses import gaussian_envelope

def run_rabi_calibration(sim: QubitSimulator, duration: float, detuning: float) -> float:
    def objective(amplitude_guess: np.ndarray) -> float:
        args = {'amplitude': amplitude_guess[0], 'duration': duration, 'sigma': duration / 4.0}
        res = sim.run_driven_evolution(duration, detuning, gaussian_envelope, args)
        return res.expect[0][-1] 
    res = minimize(objective, x0=[1.0], bounds=[(0.01, 10.0)], method='Nelder-Mead')
    return res.x[0]

def run_ramsey_calibration(sim: QubitSimulator, pi_half_amp: float, duration: float) -> float:
    def objective(detuning_guess: np.ndarray) -> float:
        args = {'amplitude': pi_half_amp, 'duration': duration, 'sigma': duration / 4.0}
        res = sim.run_driven_evolution(duration, detuning_guess[0], gaussian_envelope, args)
        return res.expect[2][-1]**2 
    res = minimize(objective, x0=[0.1], method='Nelder-Mead')
    return res.x[0]