# Problém 3 těles (N těles)

Tento projekt je fyzikální simulace gravitační interakce N těles napsaná v jazyce Python. Program vizualizuje pohyb planet, měsíců a jiných těles v reálném čase pomocí knihovny `matplotlib`.

Simulátor využívá přesný numerický integrátor **Velocity Verlet**, který zajišťuje stabilitu oběžných drah a zachování energie i při dlouhodobých simulacích, což je výrazné vylepšení oproti základní Eulerově metodě.

## Funkce
* **Reálná fyzika:** Výpočet gravitačních sil na základě Newtonova gravitačního zákona.
* **Přesný algoritmus:** Implementace Varletova algoritmu pro stabilní orbity.
* **Modularita:** Kód je rozdělen do logických modulů (vektorová matematika, fyzikální těleso, výpočetní engine).


## Struktura projektu
Projekt je strukturován následovně:

```text
n_body_simulation/
├── main.py                 # Zde se definují tělesa a pouští simulace
├── README.md               # Dokumentace projektu
└── src/                    # Zdrojové kódy jádra simulace.
    ├── __init__.py         # Inicializace Python balíčku aby nám fungovalo import src.engine
    ├── vector.py           # Implementace 3D vektorové matematiky a operátorů
    ├── body.py             # Reprezentuje fyzikální těleso
    ├── engine.py           # Počítá interakce mezi všemi tělesy a obsluhuje grafiku.
```


## Požadavky
Pro spuštění programu potřebujete nainstalovaný **Python 3.x**
Projekt závisí na knihovně `matplotlib` pro vizualizaci grafů

## Spuštění
`python main.py`

## Možnost konfigurace
V případě potřeby přidání dalšího tělesa stačí přidat následující kód (hodnoty si můžete upravit)
```text
dalsi_teleso = Body(
    mass=5.97e24,                   # Hmotnost v kg
    position=Vector(0, 0, 0),       # Počáteční pozice [x, y, z] v metrech
    velocity=Vector(0, -15, 0)      # Počáteční rychlost [vx, vy, vz] v m/s
)
```
Pro změnu rychlosti lze upravit dt, čím vyšší hodnota, tím rychlejší program + upravit steps_per_frame pro upravení množství fyzikálních výpočtů jednoho kroku.

## Připravené scénáře

* **Planeta země, pokud by měla 2 měsíce:** Bližší z nich je o několik řádů lehčí než ten druhý, který je o řád těžší než náš současný.
* **3 tělesa tvořící obrazec osmičky:** Spíše můj experiment, jestli se v mém simulovaném prostředí dají implemenovat i reálné situace - Numerické řešení provedl Christopher Moore 1993



`https://github.com/stehlikpetrps/3-telesa`
Petr Stehlík
17.12.2025
ČVUT FS

