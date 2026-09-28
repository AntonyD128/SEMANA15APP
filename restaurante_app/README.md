# Sistema de Gestión de Restaurante

**Estudiante:** Antony Jordano Defaz Diaz  
**Materia:** Programación Orientada a Objetos  
**Semestre:** Segundo Semestre - UEA Tecnologías de la Información  

# 🍽️ Restaurante App - Sistema de Gestión

Sistema de escritorio desarrollado en Python utilizando **Tkinter** para la interfaz gráfica y **JSON** para la persistencia de datos. Permite administrar usuarios, productos del menú y el registro de ventas de un restaurante de manera intuitiva y fluida.

---

## 🚀 Características

- **Gestión de Usuarios:** Registro y consulta de usuarios del sistema (Administrador, Empleados, etc.).
- **Catálogo de Productos:** Control de platillos y bebidas del restaurante.
- **Módulo de Ventas:**
  - Mapeo automático de comboboxes a IDs reales de usuario y producto.
  - Generación de identificadores de venta (V001, V002, etc.).
  - Registro inmediato con actualización en vivo de la tabla e indicadores.
- **Persistencia en JSON:** Lectura y escritura automática de datos mediante modelos serializables (`a_diccionario`).
- **Interfaz Intuitiva:** Menú lateral responsivo con resumen estadístico de totales en la barra inferior.

---

## 🛠️ Estructura del Proyecto

```text
restaurante_app/
│
├── datos/                  # Archivos de persistencia JSON
│   ├── usuarios.json
│   ├── productos.json
│   └── ventas.json
│
├── modelos/                # Clases de entidad (POO)
│   ├── usuario.py
│   ├── producto.py
│   └── venta.py
│
├── servicios/              # Lógica de negocio y persistencia
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── ui/                     # Componentes de la interfaz de usuario
│   ├── login_view.py
│   └── main_view.py
│
├── main.py                 # Punto de entrada de la aplicación
└── README.md               # Documentación del proyecto