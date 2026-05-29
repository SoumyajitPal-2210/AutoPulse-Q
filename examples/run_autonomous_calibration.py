import sys
import os

# Dynamically add the src directory to Python path for easy execution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from autoqcal.physics.simulator import QubitSimulator
from autoqcal.orchestration.agent import AutoCalibrator
from autoqcal.visualization.dashboard import generate_dashboard

def main():
    print("==================================================")
    print(" AutoQCal: Autonomous Qubit Calibration Framework ")
    print("==================================================\n")
    
    # Initialize physical simulator
    sim = QubitSimulator(t1=50000.0, t2_star=30000.0)
    
    # Initialize the automated agent
    agent = AutoCalibrator(simulator=sim)
    initial_config = dict(agent.state) 
    
    # Run the closed-loop optimization
    final_config = agent.calibrate(max_iterations=3)
    
    print("\n==================================================")
    print(" FINAL HARDWARE CONFIGURATION ")
    print("==================================================")
    for key, val in final_config.items():
        print(f" {key.ljust(15)} : {val:.5f}")
    print("==================================================\n")
    
    print("Generating visual dashboard...")
    generate_dashboard(sim, initial_config, final_config)

if __name__ == "__main__":
    main()