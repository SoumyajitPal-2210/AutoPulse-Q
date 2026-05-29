import numpy as np
import qutip as qt
from typing import Callable, Dict, Any, Optional

class QubitSimulator:
    """Simulates a noisy single superconducting qubit in the rotating frame."""
    def __init__(self, t1: float, t2_star: float):
        self.t1 = t1
        self.t2_star = t2_star
        
        gamma_1 = 1.0 / t1 if t1 > 0 else 0.0
        gamma_2 = 1.0 / t2_star if t2_star > 0 else 0.0
        gamma_phi = max(0.0, gamma_2 - (gamma_1 / 2.0))
        
        self.sz, self.sx, self.sy = qt.sigmaz(), qt.sigmax(), qt.sigmay()
        self.sm = qt.destroy(2)
        
        self.c_ops = []
        if gamma_1 > 0: self.c_ops.append(np.sqrt(gamma_1) * self.sm)
        if gamma_phi > 0: self.c_ops.append(np.sqrt(gamma_phi / 2.0) * self.sz)

    def run_driven_evolution(
        self, duration: float, detuning: float, pulse_func: Callable, 
        pulse_args: Dict[str, Any], initial_state: Optional[qt.Qobj] = None, steps: int = 100
    ) -> qt.Result:
        if initial_state is None: initial_state = qt.basis(2, 0)
        tlist = np.linspace(0, duration, steps)
        H = [0.5 * detuning * self.sz, [0.5 * self.sx, pulse_func]]
        return qt.mesolve(H, initial_state, tlist, self.c_ops, e_ops=[self.sz, self.sx, self.sy], args=pulse_args)