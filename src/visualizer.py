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