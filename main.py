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
    # Hmotnost: 5.97 * 10^24 kg (používáme vědecký zápis 'e')
    # Poloha: Střed souřadnic (0, 0, 0)
    # Rychlost: Nulová (pro zjednodušení ji považujeme za statickou kotvu)
    earth = Body(mass=5.97e24, position=Vector(0.0, 0.0, 0.0))
    
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
    
    # --- 2. NASTAVENÍ ENGINE ---
    
    # Vytvoříme seznam těles, která chceme simulovat
    bodies_list = [earth, moon]
    
    # Inicializujeme engine.
    # dt=3600.0 znamená, že jeden krok simulace = 1 hodina ve skutečnosti.
    # Čím menší číslo, tím přesnější simulace, ale trvá déle.
    engine = SimulationEngine(bodies_list, dt=3600.0)
    
    # --- 3. SMYČKA SIMULACE ---
    
    # Simulujeme 500 kroků (tj. 500 hodin času simulace)
    for i in range(500):
        
        # Toto je nejdůležitější řádek!
        # Engine vypočítá gravitaci a pohne všemi tělesy o 1 hodinu.
        engine.step()
        
        # Vypisujeme polohu každých 50 kroků (aby se nám nezahltil terminál)
        # Operátor % (modulo) vrací zbytek po dělení.
        if i % 50 == 0:
            # .2e znamená "vypiš číslo ve vědeckém formátu na 2 desetinná místa"
            print(f"Krok {i}: Měsíc X={moon.position.x:.2e}, Y={moon.position.y:.2e}")

# --- SPUŠTĚNÍ SKRIPTU ---
# Tento blok zajistí, že se simulace spustí jen tehdy, 
# když tento soubor zapneme přímo (ne když ho importujeme jinam).
if __name__ == '__main__':
    run_simulation()