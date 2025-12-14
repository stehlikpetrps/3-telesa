# --- IMPORTY ---
# Importujeme naše vlastní třídy, které jsme vytvořili ve složce src.
# Díky tomu je hlavní soubor čistý a přehledný.
import src.engine
from src.vector import Vector
from src.body import Body
from src.engine import SimulationEngine 
#"""
def run_simulation():
    
    print("--- START SIMULACE (Země + Měsíc) ---")
    
    # --- 1. VYTVOŘENÍ TĚLES ---
    
   # ZEMĚ:
    
    earth = Body(
        mass=5.97e24, 
        position=Vector(0.0, 0.0, 0.0),
        velocity=Vector(0.0, -15, 0.0)
    )
    
    # OBJEKT1
    
    moon1 = Body(
        mass=7.34e23, 
        position=Vector(3.84e8, 0, 0), 
        velocity=Vector(0, 1020, 0) 
    )
    
    # OBJEKT2
    
    moon2 = Body(
        mass=5.0e21,  # Je lehčí
        position=Vector(-2.0e8, 0, 0), # Je na druhé straně (vlevo)
        velocity=Vector(0, -1500, 0)   
    )
    
    # Vytvoříme seznam těles, která chceme simulovat
    bodies_list = [earth, moon1, moon2]
    
    # Inicializujeme engine.
    
    # Čím menší číslo, tím přesnější simulace, ale trvá déle.
    engine = SimulationEngine(bodies_list, dt=50.0)
    engine.animate(total_frames=2000, steps_per_frame = 150)
    """
def run_figure_8():
    print("--- START: FIGURE-8 ---")
    
    # --- TRIK: PŘEPNUTÍ NA MATEMATICKÉ JEDNOTKY ---
    # Aby tato specifická dráha fungovala, je snazší nastavit G=1,
    # než přepočítávat ty šílené konstanty na kilogramy.
    src.engine.G = 1.0 
    
    # PŘESNÉ MATEMATICKÉ KONSTANTY PRO "FIGURE-8"
    # Pozice (x, y)
    p_x = 0.97000436
    p_y = 0.24308753
    # Rychlost (vx, vy) - musí být takto přesná!
    v_x = 0.4662036850 
    v_y = 0.4323657300

    # Tři tělesa o hmotnosti 1.0
    # Mají symetrické pozice a rychlosti
    
    # Těleso 1 (střed)
    body1 = Body(mass=1.0, position=Vector(0.001,0,0), velocity=Vector(-2*v_x, -2*v_y, 0))
    
    # Těleso 2 (vpravo)
    body2 = Body(mass=1.0, position=Vector(p_x, -p_y, 0), velocity=Vector(v_x, v_y, 0))
    
    # Těleso 3 (vlevo)
    body3 = Body(mass=1.0, position=Vector(-p_x, p_y, 0), velocity=Vector(v_x, v_y, 0))

    bodies_list = [body1, body2, body3]

    # --- NASTAVENÍ ENGINE --- 
    # Potřebujeme extrémně malé číslo
    engine = SimulationEngine(bodies_list, dt=0.001)
    
    # Spustíme to
    # steps_per_frame musí být vysoké, protože dt je malinké
    engine.animate(total_frames=2000, steps_per_frame=2000, plot_limit=1.5)
    """
# Tento blok zajistí, že se simulace spustí jen tehdy, když tento soubor zapneme přímo (ne když ho importujeme jinam).
if __name__ == '__main__':
    run_simulation()