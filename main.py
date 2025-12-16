# --- IMPORTY ---
# Importujeme naše vlastní třídy, které jsme vytvořili ve složce src.
# Díky tomu je hlavní soubor čistý a přehledný.
import src.engine
from src.vector import Vector
from src.body import Body
from src.engine import SimulationEngine 

def run_simulation():
    
    print("--- START SIMULACE ---")
    

    
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
    
    # Čím menší číslo, tím přesnější simulace
    engine = SimulationEngine(bodies_list, dt=50.0)
    engine.animate(total_frames=1000, steps_per_frame = 50)
    

# Tento blok zajistí, že se simulace spustí jen tehdy, když tento soubor zapneme přímo (ne když ho importujeme jinam).
if __name__ == '__main__':
    run_simulation()