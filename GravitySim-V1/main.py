
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from core.physics import GravityEngine

# Configuración Inicial
engine = GravityEngine(L=1.0, m_total=10.0, fluid_viscosity=0.5, friction_coeff=0.1)
initial_state = [np.pi/4, 0.0, 8.0] # 45 grados, 0 velocidad, 8kg en m1
t = np.linspace(0, 50, 1000)

# Simulación
solution = odeint(engine.system_dynamics, initial_state, t)

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label='Ángulo (rad)')
plt.plot(t, solution[:, 2] / engine.m_total, label='Proporción Masa 1')
plt.axhline(0, color='black', lw=1)
plt.legend()
plt.title("Simulación de Torque por Desplazamiento de Masa")
plt.show()
