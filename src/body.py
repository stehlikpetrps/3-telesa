from .vector import Vector 

class Body:
    """
    Reprezentuje jedno těleso.
    """
    def __init__(self, mass: float, position: Vector, velocity: Vector = None):
        self.mass = mass            
        self.position = position    
        # Pokud nezadáme rychlost, těleso stojí (vektor 0,0,0)
        if velocity is None:
            self.velocity = Vector(0.0, 0.0, 0.0)
        else:
            self.velocity = velocity
        # Zrychlení se bude počítat v každém kroku znovu
        self.acceleration = Vector(0.0, 0.0, 0.0) 
   
    def update_position(self, dt: float):
        """
        Posuneme těleso
        na základě jeho aktuální rychlosti a zrychlení
        r(t+dt) = r(t) + v(t)*dt + 0.5*a(t)*dt^2
        """
        # Posun vlivem rychlosti
        movement = self.velocity * dt
        # Posun o zrychlení (0.5 * a * t^2)
        acceleration_drift = self.acceleration * (0.5 * dt**2)
        
        self.position = self.position + movement + acceleration_drift

    def update_velocity(self, dt: float, new_acceleration: Vector):
        """
        Vypočítáme novou rychlost, aby to bylo přesné
        použijeme průměr starého zrychlení na začáku kroku a nového na konci
        v(t+dt) = v(t) + 0.5 * (a(t) + a(t+dt)) * dt
                                staré + nové
        """
        avg_acceleration = (self.acceleration + new_acceleration) * 0.5
        velocity_change = avg_acceleration * dt
        self.velocity = self.velocity + velocity_change
        
        # Další krok
        self.acceleration = new_acceleration