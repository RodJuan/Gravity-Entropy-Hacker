import numpy as np  # <--- ¡Faltaba esta línea esencial!
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from core.physics import GravityEngine
from visualizer import animate_gravity_engine

# 1. Configuración Inicial del Motor
# L: longitud brazo, m_total: masa fluido, viscosity: k, friction: b
engine = GravityEngine(L=1.0, m_total=10.0, fluid_viscosity=0.5, friction_coeff=0.1)

# 2. Estado inicial: [ángulo (rad), velocidad angular (rad/s), masa_en_m1 (kg)]
# Usamos np.pi/4 (45 grados)
initial_state = [np.pi/4, 0.0, 8.0] 

# 3. Vector de tiempo (50 segundos, 1000 pasos para suavidad)
t = np.linspace(0, 50, 1000)

# 4. Ejecución de la Simulación (Integración numérica)
print("Ejecutando simulación física...")
solution = odeint(engine.system_dynamics, initial_state, t)

# 5. Visualización de Datos (Gráficos estáticos)
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label='Ángulo (rad)', color='blue')
plt.plot(t, solution[:, 2] / engine.m_total, label='Proporción Masa 1', color='red', linestyle='--')
plt.axhline(0, color='black', lw=1)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud / Proporción')
plt.legend()
plt.title("Dinámica de Torque: Ángulo vs Desplazamiento de Masa")
plt.grid(True, alpha=0.3)
# plt.show()  # Nota: Si activas esto aquí, la animación no empezará hasta que cierres la ventana.

# 6. Ejecutar Animación Interactiva
print("Generando animación...")
animate_gravity_engine(t, solution, engine.L)
