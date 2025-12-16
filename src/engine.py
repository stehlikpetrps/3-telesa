import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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
    
    def animate(self, total_frames=500, steps_per_frame=20):
        print("Připravuji animaci s dráhami...")
        
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Limit grafu (nastavíme podle nejvzdálenějšího tělesa)
        limit = 4.5e8 
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        ax.grid(True)
        ax.set_title("N-Body Simulace")

        colors = ['blue', 'green', 'red', 'purple', 'orange']
        sizes = [12, 8, 6, 5, 5] 

        self.dots = []
        self.trails = [] # ### NOVÉ ###
        
        # ### NOVÉ ###: Připravíme si paměť na historii poloh pro všechna tělesa
        # history = [ {'x': [seznam x souřadnic], 'y': [seznam y souřadnic]}, ... ]
        self.history = [ {'x': [], 'y': []} for _ in self.bodies ]

        # Inicializace grafických objektů (tečky a čáry)
        for i in range(len(self.bodies)):
            color = colors[i % len(colors)]
            
            # 1. Vytvoříme objekt pro ČÁRU (trail) ### NOVÉ ###
            # '-' znamená plná čára, linewidth=1 je tenká, alpha=0.6 je trochu průhledná
            trail, = ax.plot([], [], '-', color=color, linewidth=1, alpha=0.6)
            self.trails.append(trail)

            # 2. Vytvoříme objekt pro TEČKU (dot)
            # zorder=5 zajistí, že tečka bude vykreslena "nad" čárou
            dot, = ax.plot([], [], 'o', color=color, markersize=sizes[i % len(sizes)], zorder=5)
            self.dots.append(dot)

        def update(frame_number):
            # Spočítáme fyziku
            for _ in range(steps_per_frame):
                self.step()

            # Aktualizujeme grafiku
            for i, body in enumerate(self.bodies):
                # A) Přidáme aktuální polohu do historie ### NOVÉ ###
                self.history[i]['x'].append(body.position.x)
                self.history[i]['y'].append(body.position.y)

                # B) Aktualizujeme ČÁRU (pošleme jí celou historii) ### NOVÉ ###
                self.trails[i].set_data(self.history[i]['x'], self.history[i]['y'])
                
                # C) Aktualizujeme TEČKU (pošleme jí jen aktuální bod [x], [y])
                self.dots[i].set_data([body.position.x], [body.position.y])
            
            # Matplotlib musí vědět, co všechno se změnilo.
            # Vracíme spojený seznam čar a teček. ### NOVÉ ###
            return self.trails + self.dots

        # Spuštění animace (blit=False pro jistotu na Macu)
        self.ani = FuncAnimation(fig, update, frames=total_frames, 
                                 interval=20, blit=False, repeat=False)
        
        print("Spouštím okno s animací...")
        plt.show()
       