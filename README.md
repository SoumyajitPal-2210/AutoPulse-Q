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





