# --- IMPORTY ---
# Importujeme naše vlastní třídy, které jsme vytvořili ve složce src.
# Díky tomu je hlavní soubor čistý a přehledný.
from src.vector import Vector
from src.body import Body
from src.engine import SimulationEngine 

def run_simulation():
    """
    Hlavní funkce, která nastaví a spustí simulaci soustavy Země-Měsíc.
    """
    print("--- START SIMULACE (Země + Měsíc) ---")
    
    # --- 1. VYTVOŘENÍ TĚLES ---
    
   # ZEMĚ:
    # Abychom vyrušili pohyb Měsíce, musí mít Země opačnou hybnost.
    # Hybnost (p) = m * v
    # p_země musí být rovno -p_měsíce
    # v_země = -(m_měsíce * v_měsíce) / m_země
    # v_země = -(7.34e22 * 1020) / 5.97e24 = cca -12.54 m/s
    
    earth = Body(
        mass=5.97e24, 
        position=Vector(0.0, 0.0, 0.0),
        velocity=Vector(0.0, -12.54, 0.0)
    )
    
    # MĚSÍC:
    # Hmotnost: 7.34 * 10^22 kg
    # Poloha: 384 400 km od Země (na ose X) -> 3.84e8 metrů
    # Rychlost: cca 1020 m/s (na ose Y)
    # DŮLEŽITÉ: Rychlost musí být kolmá na směr k Zemi, aby Měsíc začal obíhat.
    # Kdyby byla rychlost 0, Měsíc by okamžitě spadl na Zemi.
    moon = Body(
        mass=7.34e22, 
        position=Vector(3.84e8, 0.0, 0.0), 
        velocity=Vector(0.0, 1020.0, 0.0) 
    )
    

    
    # Vytvoříme seznam těles, která chceme simulovat
    bodies_list = [earth, moon]
    
    # Inicializujeme engine.
    # dt=3600.0 znamená, že jeden krok simulace = 1 hodina ve skutečnosti.
    # Čím menší číslo, tím přesnější simulace, ale trvá déle.
    engine = SimulationEngine(bodies_list, dt=3600.0)
    engine.run_simulation(steps=2500)
    
# Tento blok zajistí, že se simulace spustí jen tehdy, když tento soubor zapneme přímo (ne když ho importujeme jinam).
if __name__ == '__main__':
    run_simulation()