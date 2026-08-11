import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def vector_angle(x,y):
    
>>> v = Matrix([1,2])
>>> w = Matrix([2,1])

>>> s = deg(acos(v.dot(w)/( v.norm() * w.norm() ) ))
>>> print(s)
180*acos(4/5)/pi


def setup_vector_plot():
    # 4. Set up the plotting canvas
    fig, ax = plt.subplots(figsize=(9, 9))
    ax.set_xlim(-4, 9)
    ax.set_ylim(-4, 9)
    ax.axhline(0, color='black', linewidth=0.8, alpha=0.5)
    ax.axvline(0, color='black', linewidth=0.8, alpha=0.5)
    ax.grid(True, linestyle='--', alpha=0.5)
    return ax



def update_plot(origin_x, origin_y):
    # 3. Define movable origin vector
    O = np.array([origin_x, origin_y])
    
    # 4. Set up the plotting canvas
    fig, ax = plt.subplots(figsize=(9, 9))
    ax.set_xlim(-4, 9)
    ax.set_ylim(-4, 9)
    ax.axhline(0, color='black', linewidth=0.8, alpha=0.5)
    ax.axvline(0, color='black', linewidth=0.8, alpha=0.5)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # 5. Draw the Triangle Perimeter
    triangle_x = [A[0], B[0], C[0], A[0]]
    triangle_y = [A[1], B[1], C[1], A[1]]
    ax.plot(triangle_x, triangle_y, color='purple', linestyle='-', linewidth=2, label='Triangle Edge')
    
    # 6. Mark Vertices and Midpoints
    ax.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='darkblue', s=80, zorder=5)
    ax.scatter([M_AB[0], M_BC[0], M_CA[0]], [M_AB[1], M_BC[1], M_CA[1]], color='teal', s=50, marker='s', zorder=5)
    ax.scatter(G[0], G[1], color='red', s=120, marker='*', label='Centroid (G)', zorder=6)
    ax.scatter(O[0], O[1], color='black', s=100, marker='x', label='Origin (O)', zorder=6)
    
    # Text labels for points
    ax.text(A[0]+0.1, A[1]+0.1, 'A', fontsize=12, fontweight='bold')
    ax.text(B[0]-0.2, B[1]-0.2, 'B', fontsize=12, fontweight='bold')
    ax.text(C[0]+0.1, C[1]-0.2, 'C', fontsize=12, fontweight='bold')
    ax.text(M_AB[0]-0.4, M_AB[1]+0.1, 'M_AB', fontsize=9, color='teal')
    ax.text(M_BC[0]+0.1, M_BC[1]-0.3, 'M_BC', fontsize=9, color='teal')
    ax.text(M_CA[0]+0.1, M_CA[1]+0.1, 'M_CA', fontsize=9, color='teal')
    
    # 7. Helper function to plot position vectors from origin
    def draw_vector(target, color, label):
        vector = target - O
        ax.quiver(O[0], O[1], vector[0], vector[1], 
                  angles='xy', scale_units='xy', scale=1, 
                  color=color, width=0.004, alpha=0.6, label=label)

    # 8. Plot position vectors
    draw_vector(A, 'blue', 'Vector OA')
    draw_vector(B, 'blue', 'Vector OB')
    draw_vector(C, 'blue', 'Vector OC')
    draw_vector(G, 'red', 'Centroid Vector OG')
    
    ax.set_title('Vector Centroid Demonstration with Movable Origin', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    plt.show()
