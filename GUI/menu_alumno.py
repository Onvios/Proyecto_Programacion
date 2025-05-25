from Clases.ACL import ACL
from Clases.Constantes import ANCHO_MENU


class MenuAlumno:
    class OpcionesMenuAlumno:
        VER_LIBRO: int = 1
        PRESTAR_LIBRO: int = 2
        DEVOLVER_LIBRO: int = 3
        EXIT: int = 4

        @staticmethod
        def opciones() -> range:
            return range(MenuAlumno.OpcionesMenuAlumno.VER_LIBRO,
                         MenuAlumno.OpcionesMenuAlumno.EXIT + 1)

    def __init__(self, app):
        self._app = app

    def mostrar(self) -> None:
        fin: bool = False
        while not fin:
            self._visualizar_menu()
            opcion = self._recoger_opcion_menu()
            if opcion is not None:
                fin = self._tratar_opcion_menu(opcion)

    @staticmethod
    def _visualizar_menu() -> None:
        print("-" * ANCHO_MENU)
        print("--- MENU ALUMNOS ---".center(ANCHO_MENU, " "))
        print("-" * ANCHO_MENU)
        print("1.- VER LIBRO")
        print("2.- COGER PRESTADO LIBRO")
        print("3.- DEVOLVER LIBRO")
        print("4.- SALIR")
        print("-" * ANCHO_MENU)

    def _recoger_opcion_menu(self) -> int:
        try:
            opcion: int = 0
            while opcion not in self.OpcionesMenuAlumno.opciones():
                opcion = int(input("¿Opción?: "))
            return opcion
        except ValueError:
            print("Por favor, introduzca un número válido.")
            return None

    def _tratar_opcion_menu(self, opcion: int) -> bool:
        if opcion == self.OpcionesMenuAlumno.VER_LIBRO:
            self._tratar_opcion_ver_libro()
        elif opcion == self.OpcionesMenuAlumno.PRESTAR_LIBRO:
            self._tratar_opcion_prestar_libro()
        elif opcion == self.OpcionesMenuAlumno.DEVOLVER_LIBRO:
            self._tratar_opcion_devolver_libro()
        elif opcion == self.OpcionesMenuAlumno.EXIT:
            return True
        return False

    def _tratar_opcion_ver_libro(self) -> None:
        print(ANCHO_MENU * "-")
        print("--- Lista de Libros ---".center(ANCHO_MENU, " "))
        print(ANCHO_MENU * "-")
        if not self._app.libros:
            print("No hay libros registrados.")
        else:
            for numero, libro in enumerate(self._app.libros, 1):
                print(f"{numero}. {libro}")
        print()

    def _tratar_opcion_prestar_libro(self) -> None:
        print(ANCHO_MENU * "-")
        print("--- Prestar Libro ---".center(ANCHO_MENU, " "))
        print(ANCHO_MENU * "-")

        if not self._app.alumnos or not self._app.libros:
            print("Debe haber al menos un alumno y un libro registrados.")
            return

        print("Selecciona un alumno:")
        for numero, alumno in enumerate(self._app.alumnos, 1):
            print(f"{numero}. {alumno}")
        try:
            indice_alumno: int = int(input("Número del alumno: ")) - 1
            alumno = self._app.alumnos[indice_alumno]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        print("Selecciona un libro:")
        for numero, libro in enumerate(self._app.libros, 1):
            print(f"{numero}. {libro}")
        try:
            indice_libro: int = int(input("Número del libro: ")) - 1
            libro = self._app.libros[indice_libro]
            if libro.numero_ejemplares <= 0:
                print("No hay ejemplares disponibles de este libro.")
                return
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        while True:
            fecha_prestamo: str = input("Fecha de préstamo (YYYY-MM-DD): ")
            if self.es_fecha_valida(fecha_prestamo):
                break
            print("Formato de fecha inválido. Intenta de nuevo.")

        nuevo_prestamo: dict = {
            "Alumno": alumno,
            "Libro": libro,
            "ACL": ACL(fecha_prestamo, None, "entregado")
        }
        self._app.prestamos.append(nuevo_prestamo)
        libro.numero_ejemplares -= 1
        print("Préstamo registrado correctamente.")

    def _tratar_opcion_devolver_libro(self) -> None:
        print(ANCHO_MENU * "-")
        print("--- Devolver Libro ---".center(ANCHO_MENU, " "))
        print(ANCHO_MENU * "-")

        prestamos_pendientes: list = [
            prestamo for prestamo in self._app.prestamos
            if prestamo["ACL"].estado == "entregado"
        ]

        if not prestamos_pendientes:
            print("No hay préstamos activos.")
            return

        print("Préstamos activos:")
        for numero, prestamo in enumerate(prestamos_pendientes, 1):
            alumno = prestamo["Alumno"]
            libro = prestamo["Libro"]
            datos_prestamo = prestamo["ACL"]
            print(f"{numero}. {alumno.nombre} - '{libro.titulo}' ({datos_prestamo.fecha_prestamo})")

        try:
            seleccion: int = int(input("Selecciona el préstamo a devolver (número): ")) - 1
            prestamo_seleccionado = prestamos_pendientes[seleccion]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        while True:
            fecha_devolucion: str = input("Fecha de devolución (YYYY-MM-DD): ")
            if self.es_fecha_valida(fecha_devolucion):
                break
            print("Formato de fecha inválido. Intenta de nuevo.")

        prestamo_seleccionado["ACL"].fecha_devolucion = fecha_devolucion
        prestamo_seleccionado["ACL"].estado = "devuelto"
        prestamo_seleccionado["Libro"].numero_ejemplares += 1
        print("Libro devuelto correctamente.")

    @staticmethod
    def es_fecha_valida(fecha_str: str) -> bool:
        partes = fecha_str.split("-")
        if len(partes) != 3:
            return False
        anio, mes, dia = partes
        if not (anio.isdigit() and mes.isdigit() and dia.isdigit()):
            return False
        anio = int(anio)
        mes = int(mes)
        dia = int(dia)
        if anio < 1 or mes < 1 or mes > 12 or dia < 1 or dia > 31:
            return False
        if mes == 2 and dia > 29:
            return False
        if mes in [4, 6, 9, 11] and dia > 30:
            return False
        return True
