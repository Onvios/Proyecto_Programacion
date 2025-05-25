class Cursos:
    def __init__(self, Curso: str, nivel: str):
        self.Curso: str = Curso
        self.nivel: str = nivel

    def __str__(self):
        return f"Curso: {self.Curso} - Nivel: {self.nivel}"
