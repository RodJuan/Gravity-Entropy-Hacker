import numpy as np

class GravityEngine:
    def __init__(self, L, m_total, fluid_viscosity, friction_coeff):
        self.L = L                  # Radio
        self.m_total = m_total      # Masa total
        self.k = fluid_viscosity    # k de transferencia
        self.b = friction_coeff     # Coeficiente de fricción
        self.g = 9.81               # Gravedad
        
    def get_mass_transfer_rate(self, m1, m2, theta):
        # h_diff > 0 significa que m1 está por encima de m2
        h_diff = 2 * self.L * np.sin(theta)
        
        # Flujo basado en raíz de la altura (Torricelli)
        # Signo positivo: el fluido QUIERE ir de m1 a m2
        flow_rate = self.k * np.sign(h_diff) * np.sqrt(abs(h_diff))
        
        # Seguridad: No sacar fluido de donde no hay
        if m1 <= 1e-6 and flow_rate > 0: 
            flow_rate = 0
        if m2 <= 1e-6 and flow_rate < 0: 
            flow_rate = 0
            
        return flow_rate

    def system_dynamics(self, state, t):
        theta, omega, m1 = state
        
        # Asegurar que m1 no se salga de los límites por error numérico
        m1 = np.clip(m1, 0, self.m_total)
        m2 = self.m_total - m1
        
        # 1. Torque Neto: 
        # Si m1 > m2 y theta=0 (horizontal), torque positivo (horario)
        # Usamos cos(theta) asumiendo que theta=0 es la horizontal derecha
        tau_gravity = (m1 - m2) * self.g * self.L * np.cos(theta)
        tau_friction = -self.b * omega
        
        # 2. Momento de Inercia (m1 y m2 en los extremos)
        I = (m1 + m2) * (self.L**2)
        
        # 3. Transferencia de masa: si flow_rate > 0, m1 disminuye
        dm1_dt = -self.get_mass_transfer_rate(m1, m2, theta)
        
        # 4. Aceleración Angular (alfa)
        alpha = (tau_gravity + tau_friction) / I
        
        return [omega, alpha, dm1_dt]
