from .vector import Vector 

class Body:
    """
    Reprezentuje jedno těleso.
    Implementuje metody pro Verletovu integraci (přesný pohyb).
    """
    def __init__(self, mass: float, position: Vector, velocity: Vector = None):
        self.mass = mass            
        self.position = position    
        
        if velocity is None:
            self.velocity = Vector(0.0, 0.0, 0.0)
        else:
            self.velocity = velocity
            
        self.acceleration = Vector(0.0, 0.0, 0.0) 

    def __repr__(self):
        return f"Body(m={self.mass:.2e}, p={self.position}, v={self.velocity})"
    
    def apply_force(self, force_vector: Vector):
        """ F = m * a -> a = F / m """
        acceleration_change = force_vector / self.mass 
        self.acceleration = self.acceleration + acceleration_change 

    def update_position(self, dt: float):
        """
        1. KROK VERLETA: Aktualizace polohy.
        r(t+dt) = r(t) + v(t)*dt + 0.5*a(t)*dt^2
        """
        # Posun o rychlost * čas
        movement = self.velocity * dt
        # Posun o zrychlení (0.5 * a * t^2)
        acceleration_drift = self.acceleration * (0.5 * dt**2)
        
        self.position = self.position + movement + acceleration_drift

    def update_velocity(self, dt: float, new_acceleration: Vector):
        """
        2. KROK VERLETA: Aktualizace rychlosti.
        v(t+dt) = v(t) + 0.5 * (a(t) + a(t+dt)) * dt
        """
        # Průměr starého a nového zrychlení
        avg_acceleration = (self.acceleration + new_acceleration) * 0.5
        velocity_change = avg_acceleration * dt
        
        self.velocity = self.velocity + velocity_change
        
        # Důležité: Nakonec musíme přepsat 'self.acceleration' na nové, 
        # abychom ho měli připravené pro další krok.
        self.acceleration = new_acceleration