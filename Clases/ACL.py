class ACL:
    def __init__(self, fecha_prestamo: str, fecha_devolucion: str, estado: str):
        self.fecha_prestamo: str = fecha_prestamo
        self.fecha_devolucion: str = fecha_devolucion
        self.estado: str = estado

    def __str__(self):
        return (f"Fecha de prestamo: {self.fecha_prestamo} - Fecha de devolucion: {self.fecha_devolucion} - "
                f"Estado: {self.estado}")
