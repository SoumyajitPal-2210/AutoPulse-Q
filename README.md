# AutoPulse-Q

## Autonomous Noise-Aware Pulse Calibration Framework for Superconducting Qubits

AutoPulse-Q is a modular simulation and orchestration framework for modeling, executing, and autonomously calibrating microwave-driven qubit dynamics under decoherence.

The project is built around a realistic hardware-control workflow:

1. Define the noisy qubit environment
2. Initialize with uncalibrated drifting hardware parameters
3. Deploy an autonomous software agent
4. Execute simulated Rabi and Ramsey calibration experiments
5. Iteratively optimize pulse amplitude and detuning
6. Visualize calibration convergence and state trajectories

The codebase is intentionally modular, mirroring modern closed-loop quantum control architectures:

- Open-system Hamiltonian modeling
- Derivative-free numerical optimization
- Autonomous state-machine orchestration
- Physically grounded calibration primitives

---

# Project Motivation

Real superconducting quantum processors do not operate on static idealized parameters. They suffer from continuous hardware drift.

Specifically:

- Transition frequencies fluctuate
- Control electronics degrade
- Microwave pulses lose gate fidelity over time

This creates a major engineering bottleneck:

- Calibration must be repeated continuously
- Manual tuning becomes impossible at scale
- Control pulses must adapt against the current noise floor

This project simulates that autonomous calibration loop computationally.

> Start with a severely miscalibrated noisy qubit. Deploy an autonomous software agent to iteratively run simulated experiments, measure outcomes, and correct physical control parameters until high-fidelity operation is restored.

# Physics Background

## Driven Qubit Dynamics with Drift

A driven two-level system evolves according to the time-dependent Schrödinger equation. In the rotating frame of the microwave drive, the Hamiltonian is:

```math
H(t) = \frac{\Delta}{2}\sigma_z + \frac{\Omega(t)}{2}\sigma_x
```

Where:

- `Δ = ωq − ωd` is the frequency detuning
- `σx, σz` are Pauli operators
- `Ω(t)` is the microwave pulse envelope

Unlike idealized simulations, this project initializes with:

```math
\Delta \neq 0
```

This introduces an intentional unknown reference-frame error that the calibration agent must autonomously discover and correct.

---

## Open Quantum Systems

Real qubits interact with their environment, leading to irreversible information loss.

The project models these effects using the Lindblad master equation:

```math
\frac{d\rho}{dt} = -i[H(t), \rho] + \frac{1}{T_1}\mathcal{D}[\sigma_-]\rho + \frac{1}{2T_\phi}\mathcal{D}[\sigma_z]\rho
```

Where:

- `ρ` is the density matrix
- `𝒟[L]ρ` is the Lindblad dissipator

This formalism captures:

- `T1` relaxation (energy decay)
- `Tφ` pure dephasing
- Decoherence-induced damping of coherent control

---

## Calibration Primitives

The autonomous agent relies on two standard calibration experiments.

### 1. Rabi Calibration

Sweeps the drive amplitude to observe coherent population transfer between `|0⟩` and `|1⟩`.

The optimizer minimizes:

```math
\langle \sigma_z \rangle
```

to identify the correct π-pulse amplitude.

---

### 2. Ramsey Calibration

Simulates a π/2 pulse under detuning error.

The optimizer minimizes:

```math
\langle \sigma_y \rangle^2
```

to estimate the inverse frequency shift required to realign:

```math
\omega_d \rightarrow \omega_q
```

# Features

- Autonomous closed-loop calibration orchestration
- Time-dependent Lindblad master equation simulation
- Gaussian and square pulse engineering
- T1 relaxation and T2* dephasing modeling
- Coarse Rabi amplitude optimization
- Ramsey frequency detuning correction
- High-fidelity visualization dashboards
- Modular scientific software architecture

---

# Software Stack

| Library | Purpose |
|---|---|
| QuTiP | Open quantum system simulation |
| SciPy | Derivative-free optimization |
| NumPy | Numerical computation |
| Matplotlib | Visualization and analytics |

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

---

# Module Breakdown

## `simulator.py`

Core physics engine responsible for:

- Constructing Lindbladian collapse operators
- Managing the time-dependent Hamiltonian
- Tracking Pauli expectation values using `qutip.mesolve`

---

## `pulses.py`

Defines microwave pulse envelopes.

Implements smooth Gaussian controls to suppress high-frequency spectral leakage during calibration.

---

## `routines.py`

Optimization layer.

Uses SciPy's Nelder-Mead algorithm to treat the simulator as a hardware black box, mapping measured expectation values to corrected control parameters.

---

## `agent.py`

Autonomous orchestration state machine.

Mimics laboratory calibration logic by deciding when to execute Rabi versus Ramsey sequences and updating internal hardware estimates after each iteration.

---

## `dashboard.py`

Analytics and visualization engine.

Generates publication-style visualizations comparing uncalibrated trajectories against optimized coherent evolution.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/SoumyajitPal-2210/AutoPulse-Q.git
cd AutoPulse-Q
```

---

## Create Virtual Environment

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Linux / macOS

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
python examples/run_autonomous_calibration.py
```

---

## Windows (PowerShell)

```powershell
$env:PYTHONPATH="src"
python examples\run_autonomous_calibration.py
```
# Example Runtime Output

```text
==================================================
 AutoPulse-Q: Autonomous Qubit Calibration Framework
==================================================

INFO: Initializing Autonomous Calibration Loop...
INFO: Initial State:
{'detuning': 1.2, 'pi_amp': 0.1, 'pulse_duration': 20.0}

--- Calibration Iteration 1/3 ---
INFO: Executing Coarse Rabi Sequence...
INFO: -> Updated Pi Amplitude: 1.2115 GHz

INFO: Executing Ramsey Sequence...
INFO: -> Corrected Detuning to: 0.6125 MHz

--- Calibration Iteration 2/3 ---
...

INFO: Calibration Converged Successfully.

==================================================
 FINAL HARDWARE CONFIGURATION
==================================================
 detuning        : 0.61227
 pi_amp          : 1.21201
 pulse_duration  : 20.00000
==================================================
```

---

# Results and Physical Analysis

The autonomous calibration framework rehabilitates a severely miscalibrated qubit environment through iterative closed-loop optimization.

---

## 1. Microwave Pulse Envelopes

The control field is modeled as a truncated Gaussian microwave drive envelope:

```math
\Omega(t)
```

### Initial Uncalibrated Pulse

- Initialized with an arbitrary amplitude:
  
```math
A = 0.1 \text{ GHz}
```

- The integrated pulse area is insufficient to induce meaningful state transfer.

### Final Calibrated Pulse

The optimizer converges to:

```math
A \approx 1.21 \text{ GHz}
```

corresponding to the correct π-pulse area within a fixed:

```math
\tau = 20 \text{ ns}
```

window.

Gaussian pulse shaping suppresses high-frequency spectral leakage and reduces coupling to higher transmon states.

---

## 2. Rabi Calibration Landscape

The calibration landscape tracks excited-state population:

```math
P(|1\rangle)
```

as a function of pulse amplitude.

Under strong detuning, the maximum reachable visibility becomes constrained:

```math
P(|1\rangle)_{\max}
=
\frac{\Omega^2}{\Omega^2 + \Delta^2}
```

The optimizer explores this non-linear landscape using derivative-free Nelder-Mead search.

---

## 3. Dynamic State Evolution

Excited-state population evolves according to:

```math
P(|1\rangle)_t
=
\frac{1 - \langle \sigma_z(t) \rangle}{2}
```

### Uncalibrated Evolution

- Weak drive amplitude
- Large detuning drift
- State remains trapped near `|0⟩`

### Calibrated Evolution

After autonomous Rabi-Ramsey correction:

- Coherent oscillations re-emerge
- Population transfer becomes controllable
- Target state preparation is restored

Open-system dissipation introduces realistic damping through:

- `T1` relaxation
- `T2*` dephasing

---

## Primary Insight

A single optimization parameter cannot compensate for hardware drift in isolation.

The autonomous multi-stage calibration loop succeeds because it jointly:

1. Maps the Rabi power landscape
2. Estimates frame detuning via Ramsey phase accumulation
3. Iteratively updates physical control parameters

---

# Critical Assessment

## What the project demonstrates well

- Closed-loop automation matching real calibration workflows
- Derivative-free optimization of noisy quantum channels
- Strong separation between orchestration and physics layers

---

## Current Limitations

- Assumes ideal projective measurement
- No stochastic `1/f` drift modeling
- Single-qubit only
- No cross-talk or `ZZ` coupling effects

---

# Scientific Concepts Demonstrated

This project demonstrates:

- Autonomous quantum hardware calibration
- Open quantum systems and Lindblad dynamics
- Rabi and Ramsey experimental protocols
- Numerical black-box optimization
- Microwave pulse engineering

---

# Future Extensions

Potential upgrades include:

- Replacing `qutip.mesolve` with NVIDIA `cuQuantum`
- Reinforcement-learning-based calibration agents
- DRAG pulse engineering for leakage suppression
- Readout resonator simulation
- Multi-qubit calibration orchestration

---

# Requirements

```text
numpy>=1.24.0
scipy>=1.10.0
qutip>=4.7.0
matplotlib>=3.7.0
pytest>=7.0.0
```

---

# Author

## Soumyajit Pal

Project Focus:

- Pulse-level quantum control
- Open quantum systems
- Noisy quantum dynamics
- Scientific quantum software
- Autonomous calibration orchestration
