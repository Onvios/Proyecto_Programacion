from Clases.ACL import ACL
from Clases.Alumno import Alumno
from Clases.Libro import Libro
from GUI.menu_principal import MenuPrincipal


class App:
    def __init__(self) -> None:
        self.alumnos: list = []
        self.libros: list = []
        self.prestamos: list = []
        self.menu_principal: MenuPrincipal = MenuPrincipal(self)

    def main(self) -> None:
        self._cargar_datos()
        self.menu_principal.mostrar()
        self._guardar_datos()

    def _cargar_datos(self) -> None:
        self._cargar_alumnos()
        self._cargar_libros()
        self._cargar_prestamos()

    def _guardar_datos(self) -> None:
        self._guardar_alumnos()
        self._guardar_libros()
        self._guardar_prestamos()

    def _guardar_alumnos(self) -> None:
        with open("Ficheros/alumnos.txt", 'w', encoding='utf-8') as f:
            for alumno in self.alumnos:
                f.write(str(alumno) + "\n")

    def _cargar_alumnos(self) -> None:
        try:
            with open("Ficheros/alumnos.txt", 'r', encoding='utf-8') as f:
                for line in f:
                    partes = line.strip().split(" - ")
                    if len(partes) == 4 and all(": " in parte for parte in partes):
                        nombre = partes[0].split(": ")[1]
                        apellido = partes[1].split(": ")[1]
                        tramo = partes[2].split(": ")[1]
                        bilingue = partes[3].split(": ")[1]
                        self.alumnos.append(Alumno(nombre, apellido, tramo, bilingue))
                    else:
                        print("Línea mal formateada en alumnos.txt:", line.strip())
        except FileNotFoundError:
            print("Archivo alumnos.txt no encontrado.")
        except IndexError:
            print("Error en el formato del archivo de alumnos.")

    def _guardar_libros(self) -> None:
        with open("Ficheros/libros.txt", 'w', encoding='utf-8') as f:
            for libro in self.libros:
                f.write(str(libro) + "\n")

    def _cargar_libros(self) -> None:
        try:
            with open("Ficheros/libros.txt", 'r', encoding='utf-8') as f:
                for line in f:
                    partes = line.strip().split(" - ")
                    if len(partes) == 4 and all(": " in parte for parte in partes):
                        titulo = partes[0].split(": ")[1]
                        autor = partes[1].split(": ")[1]
                        isbn = partes[2].split(": ")[1]
                        ejemplares = int(partes[3].split(": ")[1])
                        self.libros.append(Libro(titulo, autor, isbn, ejemplares))
                    else:
                        print("Línea mal formateada en libros.txt:", line.strip())
        except FileNotFoundError:
            print("Archivo libros.txt no encontrado.")
        except (IndexError, ValueError):
            print("Error en el formato del archivo de libros.")

    def _guardar_prestamos(self) -> None:
        with open("Ficheros/prestamos.txt", 'w', encoding='utf-8') as f:
            for prestamo in self.prestamos:
                alumno = prestamo["Alumno"]
                libro = prestamo["Libro"]
                acl = prestamo["ACL"]
                f.write(
                    f"Nombre: {alumno.nombre} - Apellido: {alumno.apellido} - "
                    f"Título: {libro.titulo} - Autor: {libro.autor} - "
                    f"Fecha préstamo: {acl.fecha_prestamo} - "
                    f"Fecha devolución: {acl.fecha_devolucion or 'N/A'} - "
                    f"Estado: {acl.estado}\n"
                )

    def _cargar_prestamos(self) -> None:
        try:
            with open("Ficheros/prestamos.txt", 'r', encoding='utf-8') as f:
                for line in f:
                    partes = line.strip().split(" - ")
                    if len(partes) == 7 and all(": " in parte for parte in partes):
                        nombre = partes[0].split(": ")[1]
                        apellido = partes[1].split(": ")[1]
                        titulo = partes[2].split(": ")[1]
                        autor = partes[3].split(": ")[1]
                        fecha_prestamo = partes[4].split(": ")[1]
                        fecha_devolucion = partes[5].split(": ")[1]
                        estado = partes[6].split(": ")[1]

                        alumno = None
                        for a in self.alumnos:
                            if a.nombre == nombre and a.apellido == apellido:
                                alumno = a
                                break
                        if alumno is None:
                            alumno = Alumno(nombre, apellido, "", "")

                        libro = None
                        for l in self.libros:
                            if l.titulo == titulo and l.autor == autor:
                                libro = l
                                break
                        if libro is None:
                            libro = Libro(titulo, autor, "", 0)

                        acl = ACL(fecha_prestamo, None if fecha_devolucion == "N/A" else fecha_devolucion, estado)

                        self.prestamos.append({"Alumno": alumno, "Libro": libro, "ACL": acl})
                    else:
                        print("Línea mal formateada en prestamos.txt:", line.strip())
        except FileNotFoundError:
            print("Archivo prestamos.txt no encontrado.")
        except (IndexError, ValueError):
            print("Error en el formato del archivo de préstamos.")


if __name__ == "__main__":
    app = App()
    app.main()
