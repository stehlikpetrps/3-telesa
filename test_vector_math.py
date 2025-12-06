from src.vector import Vector

# Vektor (3, 4, 0) by měl mít velikost přesně 5.0
v_test = Vector(3, 4, 0)
mag = v_test.get_magnitude()

print(f"Vektor pro test: {v_test}")
print(f"Očekávaná velikost: 5.0")
print(f"Vypočtená velikost: {mag}")

if mag == 5.0:
    print("Test velikosti OK!")
else:
    print("Test velikosti NEÚSPĚŠNÝ. Zkontroluj math.sqrt v třídě Vector.")

# Test násobení a sčítání
# (1, 2, 0) * 2 + (3, 1, 0) = (2, 4, 0) + (3, 1, 0) = (5, 5, 0)
v1 = Vector(1, 2, 0)
v2 = Vector(3, 1, 0)
v_result = v1 * 2 + v2

print(f"V1 * 2 + V2 = {v_result} (Očekáváno: Vector(x=5.000, y=5.000, z=0.000))")