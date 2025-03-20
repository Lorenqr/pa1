from coche import Coche

# Herencia
class CocheDeportivo(Coche):
    def __init__(self, marca, modelo, color, turbo):
        super().__init__(marca, modelo, color) # contructor de la clase padre
        self.turbo = turbo

    def __str__(self): # Polimorfismo
        return super().__str__() + f"\nturbo {self.turbo}"
    
    def activar_turbo(self):
        print(f"El {self._marca} {self._modelo} está usando el turbo.")

