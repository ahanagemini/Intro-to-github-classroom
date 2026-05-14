import matplotlib.pyplot as plt
import numpy as np
from lab7 import loss_function
from calculus_assignment import gradient_descent

def generate_assignment_plots():
    print("▶ Mapping contour spaces and evaluating your optimization path trajectories...")
    
    # Set up a meshgrid mapping the surface bounds of c = w1^2 + 3w2^2
    w1_grid = np.linspace(-3.0, 3.0, 300)
    w2_grid = np.linspace(-2.0, 2.0, 300)
    W1, W2 = np.meshgrid(w1_grid, w2_grid)
    Z = loss_function(W1, W2)
    
    # Configure the three hyperparameter profiling test modes (Slide 37)
    learning_profiles = {'small': 0.02, 'balanced': 0.15, 'oscillating': 0.32}
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for ax, (profile_name, alpha) in zip(axes, learning_profiles.items()):
        # Pull parameters dynamically from the student's gradient_descent function
        weight_path, _ = gradient_descent(start_w1=2.5, start_w2=1.5, alpha=alpha, num_iterations=12)
        
        # Render static loss landscape contours
        ax.contour(W1, W2, Z, levels=12, cmap='viridis', alpha=0.5)
        
        # Overlay student's computed descent path trajectory
        ax.plot(weight_path[:, 0], weight_path[:, 1], '-o', color='red', markersize=4, 
                label=f'Path Steps ($\\alpha$={alpha})')
        ax.scatter(0.0, 0.0, color='gold', marker='*', s=150, zorder=5, label='Global Min (0,0)')
        
        ax.set_title(f'Hyperparameter Mode: {profile_name.upper()}')
        ax.set_xlabel('Parameter Dimension ($w_1$)')
        if profile_name == 'small': 
            ax.set_ylabel('Parameter Dimension ($w_2$)')
        ax.grid(True, linestyle=':', alpha=0.4)
        ax.legend(loc='upper right')

    plt.suptitle('Student Verification Profile: Hyperparameter Convergence Dynamics', fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('my_optimization_profiles.png', dpi=150)
    print("🚀 Profile map generation complete! Please review 'my_optimization_profiles.png'.")

if __name__ == '__main__':
    generate_assignment_plots()
