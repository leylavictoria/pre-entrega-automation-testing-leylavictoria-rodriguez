# Pre-Entrega Proyecto - Automatización de Testing

Automatización de pruebas para el sitio SauceDemo, usando Selenium WebDriver y Python.

## 🎯 Propósito del Proyecto

El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:

* Login con credenciales válidas e inválidas
* Verificación del catálogo de productos
* Interacción con el carrito de compras (añadir productos y verificar su contenido)

## 🛠️ Tecnologías Utilizadas

* **Python**: Lenguaje de programación principal
* **Pytest**: Framework de testing para estructurar y ejecutar pruebas
* **Selenium WebDriver**: Para la automatización de la interfaz web
* **Git/GitHub**: Para control de versiones y compartir el código

## 📁 Estructura del Proyecto

```
pre-entrega-automation-testing-[nombre-apellido]/
├── conftest.py          # Fixture del navegador y captura automática en fallos
├── pytest.ini            # Configuración de pytest
├── requirements.txt      # Dependencias del proyecto
├── utils/
│   └── helpers.py        # Funciones y localizadores reutilizables
├── tests/
│   ├── test_login.py     # Casos de prueba de login
│   ├── test_inventory.py # Casos de prueba del catálogo
│   └── test_cart.py      # Casos de prueba del carrito
└── reports/               # Reporte HTML y capturas (se generan automáticamente)
```

## ⚙️ Instalación de Dependencias

1. Asegurate de tener Python 3.9 o superior instalado.
2. Instalá las dependencias necesarias:

```bash
pip install -r requirements.txt
```

3. Selenium descarga el ChromeDriver automáticamente (Selenium Manager). Si no lo hace, descargalo desde [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) y asegurate de que esté en el PATH.

## ▶️ Ejecución de las Pruebas

Para ejecutar todas las pruebas:

```bash
pytest -v
```

Para generar un reporte HTML:

```bash
pytest -v --html=reports/reporte.html
```

## ✅ Funcionalidades Implementadas

**1. Automatización de Login**
* Caso de éxito con credenciales válidas
* Casos de fallo con credenciales inválidas, usuario bloqueado y campos vacíos

**2. Verificación del Catálogo**
* Comprobación del título de la página
* Verificación de presencia de productos
* Validación de elementos de la interfaz (menú, filtros, etc.)

**3. Interacción con el Carrito**
* Añadir producto al carrito
* Verificar que el contador se incremente
* Navegar al carrito
* Comprobar que el producto añadido aparezca correctamente

## ✨ Características Adicionales

* **Capturas de pantalla automáticas**: se toman cuando un test falla, guardadas en `reports/screenshots/`.
* **Funciones auxiliares reutilizables**: en `utils/helpers.py`.
* **Tests independientes**: cada uno abre y cierra su propio navegador mediante un fixture de pytest.

## 👤 Autor

Leyla Victoria Rodriguez

## 📝 Notas

Este proyecto fue desarrollado como pre-entrega para el curso de Automatización de Testing. Todas las pruebas están diseñadas para funcionar con el sitio web SauceDemo en su versión actual.
