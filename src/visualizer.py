import matplotlib            
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from .engine import SimulationEngine

class SimulationVisualizer:
    """
    Třída pro vizualizaci simulace pomocí Matplotlib.
    Odděluje vykreslování od fyzikálních výpočtů.
    """
    def __init__(self, engine: SimulationEngine, view_limit: float):
        self.engine = engine
        self.view_limit = view_limit # Jak "daleko" vidíme 
        
        # Nastavení grafu (okna)
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        
        # Inicializace bodů pro tělesa - 'o' je tvar
        self.points, = self.ax.plot([], [], 'o', markersize=8)
        
        # Text pro zobrazení času v rohu
        self.time_text = self.ax.text(0.02, 0.95, '', transform=self.ax.transAxes)
    
    def init_plot(self):
        """ Nastavení os před startem animace. """
        # Nastavíme pevné hranice, aby se graf neustále nepřeškálovával
        self.ax.set_xlim(-self.view_limit, self.view_limit)
        self.ax.set_ylim(-self.view_limit, self.view_limit)
        
        self.ax.set_aspect('equal') # Aby kruh vypadal jako kruh (ne šiška)
        self.ax.grid(True, alpha=0.3)
        self.ax.set_title("Simulace N-těles (Matplotlib)")
        
        # Popisky os (v metrech)
        self.ax.set_xlabel("Vzdálenost X (m)")
        self.ax.set_ylabel("Vzdálenost Y (m)")
        
        return self.points, self.time_text
    
    def update(self, frame):
        """ 
        Tato funkce se volá pro každý snímek animace.
        Spočítá fyziku (engine.step)
        Překreslí body na nové pozice
        """
        # Provedeme jeden krok fyziky
        # Můžeme volat step() vícekrát pro zrychlení animace, aniž bychom ztratili přesnost
        steps_per_frame = 1 
        for _ in range(steps_per_frame):
            self.engine.step()
        
        # Získáme nové souřadnice všech těles pro Matplotlib
        x_data = [body.position.x for body in self.engine.bodies]
        y_data = [body.position.y for body in self.engine.bodies]
        
        # Aktualizujeme data v grafu
        self.points.set_data(x_data, y_data)
        
        # Aktualizujeme text času
        self.time_text.set_text(f'Krok simulace: {frame}')
        
        return self.points, self.time_text

    def start(self):
        """ Spustí smyčku animace. """
        anim = FuncAnimation(
            self.fig, 
            self.update, 
            init_func=self.init_plot, 
            frames=None,   # Nekonečná animace
            interval=10,   # Rychlost překreslování v ms
            blit=False     # Na Macu je bezpečnější blit=False
        )
        plt.show()
    
