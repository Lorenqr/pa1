from coche import Coche

# Ejercicio #1
# Agregue una clase Camion que hereda de Coche con el atributo adicional _capacidad
# y un método adicionar_carga(tonelada), verificar que la carga no exceda la capacidad
# actualizar __str__() del Camion

# --- Camion ---
# marca Kenworth
# modelo T680
# color Azul
# carga 25/40

class Camion(Coche):
    # Constructor
    def __init__(self, marca, modelo, color, capacidad):
        # constructor del padre, para definir los atributos que vienen del padre
        # super() siempre se refiere a la super clase o clase padre
        super().__init__(marca, modelo, color)
        # atributos propios del hijo
        self._capacidad = capacidad
        self._carga_actual = 0

    # Método
    def adicionar_carga(self, toneladas):
        if toneladas <= self._capacidad:
            self._carga_actual = toneladas
        else:
            self._carga_actual = 0

    # representación de String, utilizada por el print()
    def __str__(self):
        # primero llama el __str__() del padre, y luego adiciona lo propio del hijo
        return super().__str__() + f"\ncarga {self._carga_actual}/{self._capacidad}"

