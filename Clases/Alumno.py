class Alumno:
    def __init__(self, nombre: str, apellido: str, tramo_concedido: str, bilingue: str):
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.tramo_concedido: str = tramo_concedido
        self.bilingue: str = bilingue

    def __str__(self):
        return (f"Nombre: {self.nombre} - Apellido: {self.apellido} - Tramo: "
                f"{self.tramo_concedido} - Bilingüe: {self.bilingue}")

    def es_igual(self, otro):
        return (self.nombre.lower() == otro.nombre.lower() and
                self.apellido.lower() == otro.apellido.lower())


