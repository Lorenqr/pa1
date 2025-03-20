from coche import Coche
from coche_deportivo import CocheDeportivo
from camion import Camion

# Crear objetos
c1 = Coche("Ford", "Fiesta", "Rojo") # argumentos, en el llamado
c2 = CocheDeportivo("Ford", "Fiesta", "Rojo", "GT")

c3 = Camion("Kenworth", "T680", "Azul", 40)
c3.adicionar_carga(25)

print(c3)

