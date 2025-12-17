import math
from typing import Union

class Vector:
    """
    Třída reprezentující 3D vektor (x, y, z)
    Používáme ji pro polohu, rychlost i zrychlení
    """
    def __init__(self, x: float, y: float, z: float = 0.0):
        """
        Konstruktor třídy. Ukládá složky vektoru (x, y, z).
        Z=0.0 je výchozí hodnota, což nám umožňuje pracovat i ve 2D
        """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """ 
        Metoda __repr__ říká Pythonu, jak vypsat objekt, 
        když ho dáme do příkazu print() DEBUG ONLY
        """
        return f"Vector(x={self.x:.3f}, y={self.y:.3f}, z={self.z:.3f})"

    def __add__(self, other: 'Vector') -> 'Vector':
        """ 
        Umožňuje psát v1 + v2. Sčítá se složka po složce (x+x, y+y, z+z)
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """  
        Umožňuje psát v1 - v2
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: Union[int, float]) -> 'Vector':
        """  
        Umožňuje násobení vektoru skalárem, např. v1 * 5
        """
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __rmul__(self, scalar: Union[int, float]) -> 'Vector':
        """ 
        Přetížení operátoru * pro násobení v opačném pořadí, např. 5 * v1
        """
        return self.__mul__(scalar)

    def __truediv__(self, scalar: Union[int, float]) -> 'Vector':
        """ 
        dělení skalárem.
        """
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def get_magnitude(self) -> float:
        """ 
        Vypočítá velikost vektoru - Pythagor
        Pro určení vzdálenosti r.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self) -> 'Vector':
        """ 
        Vytvoří nový jednotkový vektor ve stejném směru
        To potřebujeme pro určení směru gravitační síly
        """
        mag = self.get_magnitude()
        if mag == 0:
            return Vector(0, 0, 0) # Vyhnutí se dělení nulou
        return self / mag