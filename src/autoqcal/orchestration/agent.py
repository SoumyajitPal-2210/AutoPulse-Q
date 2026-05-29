import logging
from typing import Dict
from autoqcal.physics.simulator import QubitSimulator
from autoqcal.calibration.routines import run_rabi_calibration, run_ramsey_calibration

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class AutoCalibrator:
    def __init__(self, simulator: QubitSimulator):
        self.sim = simulator
        self.state = {'detuning': 1.2, 'pi_amp': 0.1, 'pulse_duration': 20.0}
        
    def calibrate(self, max_iterations: int = 3) -> Dict[str, float]:
        logging.info("Initializing Autonomous Calibration Loop...")
        for i in range(max_iterations):
            logging.info(f"\n--- Iteration {i+1}/{max_iterations} ---")
            
            opt_amp = run_rabi_calibration(self.sim, self.state['pulse_duration'], self.state['detuning'])
            self.state['pi_amp'] = float(opt_amp)
            logging.info(f"-> Updated Pi Amplitude: {self.state['pi_amp']:.4f} GHz")
            
            est_detuning = run_ramsey_calibration(self.sim, self.state['pi_amp']/2.0, self.state['pulse_duration'])
            self.state['detuning'] -= float(est_detuning)
            logging.info(f"-> Corrected Detuning: {self.state['detuning']:.4f} MHz")
            
        return self.state