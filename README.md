# AutoPulse-Q

## Autonomous Noise-Aware Pulse Calibration Framework for Superconducting Qubits

AutoPulse-Q is a modular simulation and orchestration framework for modeling, executing, and autonomously calibrating microwave-driven qubit dynamics under decoherence.

The project is built around a realistic hardware-control workflow:

1. define the noisy qubit environment,
2. initialize with uncalibrated, drifting hardware parameters,
3. deploy an autonomous software agent,
4. execute simulated Rabi and Ramsey calibration experiments,
5. optimize pulse amplitude and reference frame detuning iteratively,
6. visualize the calibration convergence and state trajectories.

The codebase is intentionally modular, mirroring the architecture of modern closed-loop quantum control software:

- open-system Hamiltonian modeling,
- derivative-free numerical optimization,
- autonomous state-machine orchestration,
- and physically grounded calibration primitives.

---

# Project Motivation

Real superconducting quantum processors do not operate on static, idealized parameters. They suffer from continuous hardware drift.

Specifically:
- transition frequencies fluctuate,
- control electronics degrade,
- and static microwave pulses quickly lose gate fidelity.

That creates a severe engineering bottleneck:
- calibration must be repeated constantly,
- manual tuning is impossible at scale,
- and pulses must be actively corrected against the current noise floor.

This project simulates that autonomous calibration loop computationally.

The goal is physically meaningful:

> Start with a severely miscalibrated, noisy qubit. Deploy an autonomous software agent to iteratively run simulated experiments, measure the outcomes, and correct the physical control parameters until a perfect high-fidelity operation is restored.

---

# Physics Background

## Driven Qubit Dynamics with Drift

A driven two-level system evolves according to the time-dependent Schrödinger equation. In the rotating frame of the microwave drive, the Hamiltonian is:

$$H(t) = \frac{\Delta}{2}\sigma_z + \frac{\Omega(t)}{2}\sigma_x$$

where:
- $\Delta = \omega_q - \omega_d$ is the frequency detuning (hardware drift),
- $\sigma_x, \sigma_z$ are Pauli operators,
- $\Omega(t)$ is the microwave pulse envelope.

Unlike idealized simulations, this project initializes with:

$$\Delta \neq 0$$

This introduces an intentional, unknown reference-frame error that the calibration agent must autonomously discover and correct.

---

## Open Quantum Systems

Real qubits interact with their environment, leading to irreversible loss of information. 

The project models these effects using the Lindblad master equation:

$$\frac{d\rho}{dt} = -i[H(t), \rho] + \frac{1}{T_1} \mathcal{D}[\sigma_-]\rho + \frac{1}{2 T_\phi} \mathcal{D}[\sigma_z]\rho$$

where:
- $\rho$ is the density matrix,
- $\mathcal{D}[L]\rho = L\rho L^\dagger - \frac{1}{2}\{L^\dagger L, \rho\}$ is the standard dissipator.

This formalism captures:
- $T_1$ relaxation (energy decay),
- $T_\phi$ pure dephasing (phase loss),
- and the resulting damping of coherent control.

---

## Calibration Primitives

The autonomous agent relies on two standard experimental protocols.

### 1. Rabi Calibration
Sweeps the drive amplitude $\Omega(t)$ to observe harmonic population transfer between $|0\rangle$ and $|1\rangle$. The optimizer minimizes $\langle \sigma_z \rangle$ to find the exact amplitude required for a $\pi$-pulse.

### 2. Ramsey Calibration
Simulates a $\pi/2$ pulse under the current detuning error. The optimizer minimizes the accumulated phase along the Y-axis ($\langle \sigma_y \rangle^2$) to calculate the inverse frequency shift required to realign the drive frequency $\omega_d$ with the qubit frequency $\omega_q$.

---

# Features

- Autonomous closed-loop orchestration
- Time-dependent Lindblad master equation simulation
- Gaussian and Square pulse engineering
- T1 relaxation and T2* dephasing modeling
- Coarse Rabi amplitude optimization
- Ramsey frequency detuning correction
- High-fidelity NVIDIA-tier visual dashboards
- Modular scientific software architecture

---

# Software Stack

| Library | Purpose |
|---|---|
| QuTiP | Open quantum system simulation |
| SciPy | Derivative-free numerical optimization |
| NumPy | Numerical computation |
| Matplotlib | Trajectory and landscape visualization |

---

# Project Structure

```text
AutoPulse-Q/
│
├── README.md
├── requirements.txt
│
├── src/autoqcal/
│   ├── __init__.py
│   ├── physics/
│   │   └── simulator.py
│   ├── control/
│   │   └── pulses.py
│   ├── calibration/
│   │   └── routines.py
│   ├── orchestration/
│   │   └── agent.py
│   └── visualization/
│       └── dashboard.py
│
├── tests/
│   └── test_simulator.py
│
└── examples/
    └── run_autonomous_calibration.py
```
# Module Breakdown

## `simulator.py`

The core physics engine.

Responsible for:
- constructing the Lindbladian collapse operators,
- managing the time-dependent Hamiltonian,
- and tracking Pauli expectation values via `qutip.mesolve`.

---

## `pulses.py`

Defines the microwave envelopes.

Generates smooth Gaussian controls to suppress high-frequency spectral leakage during the calibration sequence.

---

## `routines.py`

The mathematical optimization layer.

Uses SciPy's Nelder-Mead algorithm to treat the simulator as an experimental black box, mapping "measured" expectation values to corrected physical parameters.

---

## `agent.py`

The orchestration state machine.

Mimics the logic of a laboratory calibration script. It autonomously decides when to run a Rabi sequence versus a Ramsey sequence, updating its internal assumptions about the hardware after each step.

---

## `dashboard.py`

The analytics engine.

Generates publication-ready visualizations comparing the uncalibrated trajectory to the final optimized state, providing immediate physical context to the numerical results.

---


# Installation

## Clone Repository

```bash
git clone [https://github.com/SoumyajitPal-2210/AutoPulse-Q.git](https://github.com/SoumyajitPal-2210/AutoPulse-Q.git)
cd AutoPulse-Q

python -m venv venv
source venv/bin/activate
