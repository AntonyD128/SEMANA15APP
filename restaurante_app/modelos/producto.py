class Productos:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    @staticmethod
    def validar_texto(valor, campo):
        # Reutiliza una validacion basica para datos obligatorios.
        if not valor or not str(valor).strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")
        return str(valor).strip()

    @staticmethod
    def validar_precio(valor):
        # Validacion especifica para montos o precios
        try:
            monto = float(valor)
            if monto <= 0:
                raise ValueError
            return monto
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser un numero mayor a 0.")

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = self.validar_texto(valor, "codigo")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = self.validar_precio(valor)

    def a_dict(self):
        """Convierte la instancia a un diccionario para guardar en JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio
        }