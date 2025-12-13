import matplotlib.pyplot as plt
from .vector import Vector
from .body import Body

G = 6.6743e-11 

class SimulationEngine:
    def __init__(self, bodies: list[Body], dt: float = 0.01):
        self.bodies = bodies
        self.dt = dt

    def calculate_acceleration(self, target_body: Body) -> Vector:
        """
        Vypočítá OKAMŽITÉ zrychlení jednoho tělesa na základě sil od ostatních.
        Nemení stav tělesa, jen vrací vektor zrychlení.
        """
        total_acceleration = Vector(0.0, 0.0, 0.0)
        
        for other_body in self.bodies:
            if other_body is target_body:
                continue # Nepočítat sílu sám na sebe
            
            # Vektor k druhému tělesu
            r_vector = other_body.position - target_body.position
            r_magnitude = r_vector.get_magnitude()
            
            if r_magnitude == 0:
                continue 

            # Síla F = G * m1 * m2 / r^2
            # Zrychlení a = F / m1 = G * m2 / r^2
            a_magnitude = G * other_body.mass / (r_magnitude ** 2)
            r_direction = r_vector.normalize()
            
            # Přičtení vektoru zrychlení
            total_acceleration = total_acceleration + (r_direction * a_magnitude)
            
        return total_acceleration

    def step(self):
        """
        VELOCITY VERLET ALGORITMUS
        Tento postup zachovává energii a je stabilní pro orbity.
        """
        
        # 1. Posunout polohu všech těles (pomocí starého zrychlení)
        for body in self.bodies:
            body.update_position(self.dt)
            
        # 2. Vypočítat NOVÉ zrychlení pro všechna tělesa (na nové pozici)
        # Musíme si je uložit bokem, abychom nepřepsali stará zrychlení předčasně
        new_accelerations = []
        for body in self.bodies:
            acc = self.calculate_acceleration(body)
            new_accelerations.append(acc)
            
        # 3. Aktualizovat rychlost (pomocí průměru starého a nového zrychlení)
        for i in range(len(self.bodies)):
            body = self.bodies[i]
            new_acc = new_accelerations[i]
            
            body.update_velocity(self.dt, new_acc)

    def run_simulation(self, steps: int):
        print(f"Počítám {steps} kroků fyziky...")
        history = [ {'x': [], 'y': []} for _ in self.bodies ]

        for _ in range(steps):
            self.step()
            for i, body in enumerate(self.bodies):
                history[i]['x'].append(body.position.x)
                history[i]['y'].append(body.position.y)

        print("Výpočet dokončen. Vykresluji graf...")
        self._plot_results(history)

    def _plot_results(self, history):
        plt.figure(figsize=(10, 10))
        names = ['Země', 'Měsíc']
        
        for i in range(len(self.bodies)):
            plt.plot(history[i]['x'], history[i]['y'], label=names[i] if i < len(names) else f'Těleso {i}')
            # Tečka na začátku dráhy
            plt.plot(history[i]['x'][0], history[i]['y'][0], 'o')

        plt.axis('equal')
        plt.grid(True)
        plt.legend()
        plt.title("Simulace oběžné dráhy")
        
        # Uložíme obrázek
        plt.savefig("vysledek_simulace.png")
        print("Graf uložen jako 'vysledek_simulace.png'")
        
        try:
            plt.show()
        except:
            pass