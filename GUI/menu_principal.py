from Clases.Constantes import ANCHO_MENU
from GUI.menu_admin import MenuAdmin
from GUI.menu_alumno import MenuAlumno


class MenuPrincipal:
    class OpcionesMenuPrincipal:
        ADMIN: int = 1
        ALUMNO: int = 2
        SALIR: int = 3

        @staticmethod
        def opciones():
            return range(MenuPrincipal.OpcionesMenuPrincipal.ADMIN,
                         MenuPrincipal.OpcionesMenuPrincipal.SALIR + 1)

    def __init__(self, app):
        self._app = app
        self.menu_admin = MenuAdmin(self._app)
        self.menu_alumno = MenuAlumno(self._app)

    def main(self):
        self.mostrar()

    def mostrar(self):
        fin = False
        while not fin:
            self._visualizar_menu()
            opcion = self._recoger_opcion_menu()
            fin = self._tratar_opcion_menu(opcion)

    @staticmethod
    def _visualizar_menu():
        print("-" * ANCHO_MENU)
        print("  Menú Principal  ".center(ANCHO_MENU, " "))
        print("-" * ANCHO_MENU)
        print("1.- MENU ADMINISTRADOR")
        print("2.- MENU ALUMNO")
        print("3.- SALIR")
        print("-" * ANCHO_MENU)

    def _recoger_opcion_menu(self) -> int:
        while True:
            try:
                opcion = int(input("¿Opción?: "))
                if opcion in self.OpcionesMenuPrincipal.opciones():
                    return opcion
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Por favor, introduzca un número válido.")

    def _tratar_opcion_menu(self, opcion) -> bool:
        if opcion == self.OpcionesMenuPrincipal.ADMIN:
            self.menu_admin.mostrar()
        elif opcion == self.OpcionesMenuPrincipal.ALUMNO:
            self.menu_alumno.mostrar()
        elif opcion == self.OpcionesMenuPrincipal.SALIR:
            self._cerrar_app()
            return True
        return False

    @staticmethod
    def _cerrar_app():
        print("¡Hasta la próxima!")
