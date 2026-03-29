
import numpy as np

class GravityEngine:
    def __init__(self, L, m_total, fluid_viscosity, friction_coeff):
        self.L = L                  # Longitud de la varilla (radio)
        self.m_total = m_total      # Masa total del fluido + varilla
        self.k = fluid_viscosity    # Factor de transferencia (Torricelli modificado)
        self.b = friction_coeff     # Fricción en el eje
        self.g = 9.81               # Gravedad
        
    def get_mass_transfer_rate(self, m1, m2, theta):
        """
        Calcula la tasa de transferencia dm/dt basada en la diferencia 
        de altura inducida por el ángulo theta.
        """
        h_diff = 2 * self.L * np.sin(theta)
        # Si h_diff > 0, m1 está más alto que m2
        flow_rate = self.k * np.sign(h_diff) * np.sqrt(abs(h_diff))
        
        # Limitar el flujo si una esfera se queda vacía
        if m1 <= 0 and flow_rate > 0: flow_rate = 0
        if m2 <= 0 and flow_rate < 0: flow_rate = 0
            
        return flow_rate

    def system_dynamics(self, state, t):
        """
        Estado: [theta, omega, m1]
        m2 se deriva de m_total - m1
        """
        theta, omega, m1 = state
        m2 = self.m_total - m1 # Asumiendo varilla de masa despreciable inicialmente
        
        # 1. Torque Neto
        tau_net = (m1 - m2) * self.g * self.L * np.cos(theta)
        
        # 2. Momento de Inercia Variable
        I = (m1 + m2) * (self.L**2)
        
        # 3. Transferencia de masa
        dm1_dt = -self.get_mass_transfer_rate(m1, m2, theta)
        
        # 4. Aceleración Angular (alfa)
        # Incluye fricción b * omega
        alpha = (tau_net - self.b * omega) / I
        
        return [omega, alpha, dm1_dt]
