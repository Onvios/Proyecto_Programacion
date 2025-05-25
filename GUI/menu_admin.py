from Clases.ACL import ACL
from Clases.Alumno import Alumno
from Clases.Constantes import ANCHO_MENU
from Clases.Constantes import password_admin
from Clases.Libro import Libro


class MenuAdmin:
    class OpcionesMenuAdmin:
        ADD_ALUMNO: int = 1
        VER_ALUMNO: int = 2
        MODIFICAR_ALUMNO: int = 3
        ELIMINAR_ALUMNO: int = 4
        ADD_LIBRO: int = 5
        VER_LIBRO: int = 6
        MODIFICAR_LIBRO: int = 7
        ELIMINAR_LIBRO: int = 8
        PRESTAR_LIBRO: int = 9
        DEVOLVER_LIBRO: int = 10
        EXIT: int = 11

        @staticmethod
        def opciones():
            return range(MenuAdmin.OpcionesMenuAdmin.ADD_ALUMNO, MenuAdmin.OpcionesMenuAdmin.EXIT + 1)

    def __init__(self, app):
        self._app = app
        self._admin_autenticado: bool = False

    def admin_inicio_sesion(self) -> None:
        print(f" <- Inicio sesion a Menú de Administradores ->".center(ANCHO_MENU, " "))
        password = input("Contraseña: ").lower()
        if password_admin == password:
            self._admin_autenticado = True
            print(f"Contraseña correcta")
        else:
            print("Contraseña incorrecta")

    def main(self):
        self.admin_inicio_sesion()
        if self._admin_autenticado:
            fin = False
            while not fin:
                self._visualizar_menu()
                opcion = self._recoger_opcion_menu()
                fin = self._tratar_opcion_menu(opcion)

    def mostrar(self):
        self.admin_inicio_sesion()
        if self._admin_autenticado:
            fin = False
            while not fin:
                self._visualizar_menu()
                opcion = self._recoger_opcion_menu()
                fin = self._tratar_opcion_menu(opcion)

    @staticmethod
    def _visualizar_menu() -> None:
        print("-" * ANCHO_MENU)
        print("--- MENÚ GESTIÓN BIBLIOTECA ---".center(ANCHO_MENU, " "))
        print("-" * ANCHO_MENU)
        print("1.- AGREGAR ALUMNO")
        print("2.- LISTAR ALUMNOS")
        print("3.- MODIFICAR ALUMNO")
        print("4.- ELIMINAR ALUMNO")
        print("5.- AGREGAR LIBRO")
        print("6.- LISTAR LIBROS")
        print("7.- MODIFICAR LIBRO")
        print("8.- ELIMINAR LIBRO")
        print("9.- PRESTAR LIBRO")
        print("10.- DEVOLVER LIBRO")
        print("11.- SALIR")
        print("-" * ANCHO_MENU)

    def _recoger_opcion_menu(self) -> int:
        opcion = 0
        while opcion not in self.OpcionesMenuAdmin.opciones():
            try:
                opcion = int(input("¿Opción?> "))
            except ValueError:
                print("Por favor, introduce un número válido.")
        return opcion

    def _tratar_opcion_menu(self, opcion) -> bool:
        if opcion == self.OpcionesMenuAdmin.ADD_ALUMNO:
            self._tratar_opcion_add_alumno()
        elif opcion == self.OpcionesMenuAdmin.VER_ALUMNO:
            self._tratar_opcion_ver_alumno()
        elif opcion == self.OpcionesMenuAdmin.MODIFICAR_ALUMNO:
            self._tratar_opcion_modificar_alumno()
        elif opcion == self.OpcionesMenuAdmin.ELIMINAR_ALUMNO:
            self._tratar_opcion_eliminar_alumno()
        elif opcion == self.OpcionesMenuAdmin.ADD_LIBRO:
            self._tratar_opcion_add_libro()
        elif opcion == self.OpcionesMenuAdmin.VER_LIBRO:
            self._tratar_opcion_ver_libro()
        elif opcion == self.OpcionesMenuAdmin.MODIFICAR_LIBRO:
            self._tratar_opcion_modificar_libro()
        elif opcion == self.OpcionesMenuAdmin.ELIMINAR_LIBRO:
            self._tratar_opcion_eliminar_libro()
        elif opcion == self.OpcionesMenuAdmin.PRESTAR_LIBRO:
            self._tratar_opcion_prestar_libro()
        elif opcion == self.OpcionesMenuAdmin.DEVOLVER_LIBRO:
            self._tratar_opcion_devolver_libro()
        elif opcion == self.OpcionesMenuAdmin.EXIT:
            return True
        return False

    def _tratar_opcion_add_alumno(self) -> None:
        print(ANCHO_MENU * "-")
        print("--- AÑADIR ALUMNO ---".center(ANCHO_MENU, " "))
        print(ANCHO_MENU * "-")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()

        nuevo_alumno = Alumno(nombre, apellido, "", "")
        for alumno in self._app.alumnos:
            if alumno.es_igual(nuevo_alumno):
                print(f"YA EXISTE UN ALUMNO CON EL NOMBRE '{nombre} {apellido}'. NO SE PUEDE DUPLICAR.")
                return

        print("Introduce el tramo concedido según el tipo de beca:")
        print("1 - Beca completa")
        print("2 - Beca parcial")
        print("3 - Sin beca")
        while True:
            tramo = input("Tramo concedido (1, 2 o 3): ").strip()
            if tramo in ("1", "2", "3"):
                break
            print("Tramo inválido. Debe ser 1, 2 o 3.")

        bilingue = input("¿Bilingüe? (Sí/No): ").strip()

        nuevo_alumno.tramo_concedido = tramo
        nuevo_alumno.bilingue = bilingue
        self._app.alumnos.append(nuevo_alumno)
        print("ALUMNO AÑADIDO CORRECTAMENTE.")

    def _tratar_opcion_ver_alumno(self) -> None:
        print(ANCHO_MENU * "-")
        print("--- Lista de Alumnos ---".center(ANCHO_MENU, " "))
        print(ANCHO_MENU * "-")
        if not self._app.alumnos:
            print("No hay alumnos registrados.")
        else:
            for numero, alumno in enumerate(self._app.alumnos, 1):
                print(f"{numero}. {alumno}")

    def _tratar_opcion_modificar_alumno(self) -> None:
        self._tratar_opcion_ver_alumno()

        try:
            indice_seleccionado = int(input("Selecciona número de alumno a modificar: ")) - 1
            alumno_seleccionado = self._app.alumnos[indice_seleccionado]
        except (ValueError, IndexError):
            print("SELECCIÓN INVÁLIDA.")
            return

        print(f"MODIFICANDO ALUMNO: {alumno_seleccionado}")
        nombre = input("NUEVO NOMBRE (Enter para mantener): ").strip()
        apellido = input("NUEVO APELLIDO (Enter para mantener): ").strip()
        bilingue = input("¿BILINGÜE? (Sí/No, Enter para mantener): ").strip()

        nombre_final = nombre if nombre else alumno_seleccionado.nombre
        apellido_final = apellido if apellido else alumno_seleccionado.apellido

        alumno_modificado = Alumno(nombre_final, apellido_final, alumno_seleccionado.tramo,
                                   alumno_seleccionado.bilingue)

        for indice_otro, otro_alumno in enumerate(self._app.alumnos):
            if indice_otro != indice_seleccionado and otro_alumno.es_igual(alumno_modificado):
                print(f"YA EXISTE UN ALUMNO CON EL NOMBRE '{nombre_final} {apellido_final}'. NO SE PUEDE DUPLICAR.")
                return

        alumno_seleccionado.nombre = nombre_final
        alumno_seleccionado.apellido = apellido_final
        if bilingue:
            alumno_seleccionado.bilingue = bilingue

        print("ALUMNO MODIFICADO CORRECTAMENTE. (EL TRAMO NO SE PUEDE CAMBIAR)")

    def _tratar_opcion_eliminar_alumno(self) -> None:
        self._tratar_opcion_ver_alumno()
        try:
            idx = int(input("Selecciona número de alumno a eliminar: ")) - 1
            eliminado = self._app.alumnos.pop(idx)
            print(f"Alumno '{eliminado.nombre} {eliminado.apellido}' eliminado correctamente.")
        except (ValueError, IndexError):
            print("Selección inválida.")

    def _tratar_opcion_add_libro(self) -> None:
        print(ANCHO_MENU * "-")
        print("--- Añadir Libro ---".center(ANCHO_MENU, " "))
        print(ANCHO_MENU * "-")
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()

        while True:
            isbn = input("ISBN: ").strip()
            if self.validar_isbn(isbn):
                break
            print("ISBN inválido. Solo se permiten dígitos y guiones, y debe tener 10 o 13 dígitos.")

        while True:
            try:
                ejemplares = int(input("Número de ejemplares: "))
                if ejemplares < 0:
                    print("Debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("Introduce un número válido.")

        nuevo_libro = Libro(titulo, autor, isbn, ejemplares)
        self._app.libros.append(nuevo_libro)
        print("Libro añadido correctamente.")

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

    def _tratar_opcion_modificar_libro(self) -> None:
        self._tratar_opcion_ver_libro()
        try:
            indice_libro = int(input("Selecciona número de libro a modificar: ")) - 1
            libro = self._app.libros[indice_libro]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        print(f"Modificando libro: {libro}")
        titulo = input("Nuevo título (Enter para mantener): ").strip()
        autor = input("Nuevo autor (Enter para mantener): ").strip()
        isbn = input("Nuevo ISBN (Enter para mantener): ").strip()
        ejemplares = input("Nuevo número de ejemplares (Enter para mantener): ").strip()

        if titulo:
            libro.titulo = titulo
        if autor:
            libro.autor = autor
        if isbn:
            if self.validar_isbn(isbn):
                libro.isbn = isbn
            else:
                print("ISBN inválido. Se mantiene el ISBN anterior.")
        if ejemplares:
            try:
                ejemplares = int(ejemplares)
                if ejemplares >= 0:
                    libro.numero_ejemplares = ejemplares
            except ValueError:
                print("Cantidad inválida, se mantiene el valor anterior.")

        print("Libro modificado correctamente.")

    def _tratar_opcion_eliminar_libro(self) -> None:
        self._tratar_opcion_ver_libro()
        try:
            indice_libro = int(input("Selecciona número de libro a eliminar: ")) - 1
            eliminado = self._app.libros.pop(indice_libro)
            print(f"Libro '{eliminado.titulo}' eliminado correctamente.")
        except (ValueError, IndexError):
            print("Selección inválida.")

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
            indice_alumno = int(input("Número del alumno: ")) - 1
            alumno = self._app.alumnos[indice_alumno]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        print("Selecciona un libro:")
        for numero, libro in enumerate(self._app.libros, 1):
            print(f"{numero}. {libro}")
        try:
            indice_libro = int(input("Número del libro: ")) - 1
            libro = self._app.libros[indice_libro]
            if libro.numero_ejemplares <= 0:
                print("No hay ejemplares disponibles de este libro.")
                return
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        while True:
            fecha_prestamo = input("Fecha de préstamo (YYYY-MM-DD): ")
            if self.es_fecha_valida(fecha_prestamo):
                break
            print("Formato de fecha inválido. Intenta de nuevo.")

        nuevo_prestamo = {
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

        prestamos_pendientes = [
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
            seleccion = int(input("Selecciona el préstamo a devolver (número): ")) - 1
            prestamo_seleccionado = prestamos_pendientes[seleccion]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        while True:
            fecha_devolucion = input("Fecha de devolución (YYYY-MM-DD): ")
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
        ano, mes, dia = partes
        if not (ano.isdigit() and mes.isdigit() and dia.isdigit()):
            return False
        ano = int(ano)
        mes = int(mes)
        dia = int(dia)
        if ano < 1 or mes < 1 or mes > 12 or dia < 1 or dia > 31:
            return False
        if mes == 2 and dia > 29:
            return False
        if mes in [4, 6, 9, 11] and dia > 30:
            return False
        return True

    @staticmethod
    def validar_isbn(isbn: str) -> bool:
        digitos = 0
        for caracter in isbn:
            if caracter.isdigit():
                digitos += 1
            elif caracter != "-":
                return False
        return digitos in (10, 13)
