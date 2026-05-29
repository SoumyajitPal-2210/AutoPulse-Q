import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from autoqcal.control.pulses import gaussian_envelope

def generate_dashboard(sim, initial_config, final_config):
    """Generates a high-fidelity visual dashboard of the calibration results."""
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(16, 8))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1.5])
    fig.suptitle('Autonomous Pulse Calibration Results', fontsize=20, fontweight='bold', y=0.98)

    tlist = np.linspace(0, final_config['pulse_duration'], 200)
    args_init = {'amplitude': initial_config['pi_amp'], 'duration': initial_config['pulse_duration']}
    args_final = {'amplitude': final_config['pi_amp'], 'duration': final_config['pulse_duration']}
    
    res_init = sim.run_driven_evolution(initial_config['pulse_duration'], initial_config['detuning'], gaussian_envelope, args_init, steps=200)
    res_final = sim.run_driven_evolution(final_config['pulse_duration'], final_config['detuning'], gaussian_envelope, args_final, steps=200)

    # 1. Pulses
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(tlist, [gaussian_envelope(t, args_init) for t in tlist], color='#ff4c4c', linestyle='--', linewidth=2, label='Initial')
    ax1.plot(tlist, [gaussian_envelope(t, args_final) for t in tlist], color='#00ffcc', linewidth=3, label='Final')
    ax1.set(title='Microwave Pulse Envelopes', xlabel='Time (ns)', ylabel='Amplitude (GHz)')
    ax1.legend(loc='upper right')
    ax1.grid(alpha=0.2)

    # 2. Rabi Landscape
    ax2 = fig.add_subplot(gs[0, 1])
    test_amps = np.linspace(0.1, 2.5, 30)
    pops = [(1 - sim.run_driven_evolution(final_config['pulse_duration'], final_config['detuning'], gaussian_envelope, {'amplitude': a, 'duration': final_config['pulse_duration']}, steps=50).expect[0][-1]) / 2 for a in test_amps]
    ax2.plot(test_amps, pops, color='#ff00ff', linewidth=2, marker='o', markersize=4, label='Simulated Rabi Oscillation')
    ax2.axvline(final_config['pi_amp'], color='#00ffcc', linestyle='--', label=f"Optimal Amp: {final_config['pi_amp']:.2f}")
    ax2.set(title='Rabi Calibration Landscape', xlabel='Drive Amplitude (GHz)', ylabel='Excited State Probability $P(|1\\rangle)$')
    ax2.legend()
    ax2.grid(alpha=0.2)

    # 3. Trajectory
    ax3 = fig.add_subplot(gs[1, :])
    ax3.plot(tlist, (1 - res_init.expect[0]) / 2, color='#ff4c4c', linestyle='--', linewidth=2, label='Uncalibrated Trajectory')
    ax3.plot(tlist, (1 - res_final.expect[0]) / 2, color='#00ffcc', linewidth=3, label='Calibrated Trajectory (Perfect Pi-Pulse)')
    ax3.set(title='Qubit State Evolution During Pulse', xlabel='Time (ns)', ylabel='Excited State Population', ylim=(-0.05, 1.05))
    ax3.axhline(1.0, color='white', alpha=0.3, linestyle=':')
    ax3.legend(loc='center right', fontsize=12)
    ax3.grid(alpha=0.2)
    ax3.fill_between(tlist, (1 - res_final.expect[0]) / 2, color='#00ffcc', alpha=0.1)

    plt.tight_layout()
    plt.show()