# Clase, con inicial Mayúscula
# Objetos o Instancias, con inicial minúscula
class Coche:
    # Constructor
    def __init__(self, marca, modelo, color): # parámetros, en la definición
        # Atributos (encapsulados): public, private, protected
        self._marca = marca
        self._modelo = modelo
        self._color = color

    # Métodos
    def acelerar(self):
        print(f"El {self._marca} {self._modelo} está acelerando.")

    def frenar(self):
        print(f"El {self._marca} {self._modelo} está frenando.")

    def __str__(self): # representación como String
        return f"""--- {self.__class__.__name__} ---
marca {self._marca}
modelo {self._modelo}
color {self._color}"""
    
    # Encapsulamiento (acceso controlado a los atributos) -> Getters y Setters
    def obtener_color(self):
        return self._color

    def cambiar_color(self, nuevo_color):
        self._color = nuevo_color

    def obtener_marca(self):
        return self._marca

