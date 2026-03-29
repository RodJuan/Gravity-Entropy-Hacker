import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_gravity_engine(t, states, L):
    theta_vals = states[:, 0]
    m1_vals = states[:, 2]
    m_total = np.max(m1_vals) + np.min(m1_vals) # Aproximación

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-L*1.5, L*1.5)
    ax.set_ylim(-L*1.5, L*1.5)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--')

    # Elementos visuales
    line, = ax.plot([], [], 'o-', lw=4, color='darkblue', markersize=10)
    mass1_patch = plt.Circle((0, 0), 0.1, color='red', alpha=0.6)
    mass2_patch = plt.Circle((0, 0), 0.1, color='green', alpha=0.6)
    ax.add_patch(mass1_patch)
    ax.add_patch(mass2_patch)

    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    def init():
        line.set_data([], [])
        mass1_patch.center = (0, 0)
        mass2_patch.center = (0, 0)
        return line, mass1_patch, mass2_patch, time_text

    def update(i):
        theta = theta_vals[i]
        # Coordenadas de las masas
        x1, y1 = L * np.cos(theta), L * np.sin(theta)
        x2, y2 = -x1, -y1
        
        # Actualizar varilla
        line.set_data([x2, x1], [y2, y1])
        
        # Escalar tamaño de las esferas según la masa m1 y m2
        m1 = m1_vals[i]
        m2 = m_total - m1
        mass1_patch.set_radius(0.05 + (m1/m_total) * 0.15)
        mass2_patch.set_radius(0.05 + (m2/m_total) * 0.15)
        
        mass1_patch.center = (x1, y1)
        mass2_patch.center = (x2, y2)
        
        time_text.set_text(f't = {t[i]:.2f}s\nTheta = {np.degrees(theta):.1f}°')
        return line, mass1_patch, mass2_patch, time_text

    ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20)
    # En lugar de plt.show()
    print("Guardando animación como gravity_sim.gif...")
    ani.save('gravity_sim.gif', writer='pillow', fps=30)
    print("¡Listo! Descarga el archivo gravity_sim.gif para verlo.")
    #plt.show()
    return ani
