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



