 
import os
import datetime
 
# --- Datos de prueba ---
BASE_URL = "https://www.saucedemo.com/"
 
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"
USUARIO_BLOQUEADO = "locked_out_user"
 
TIMEOUT = 10  # segundos para las esperas explícitas
 
 
def tomar_captura_en_fallo(driver, nombre_test):
    """
    Guarda una captura de pantalla en reports/screenshots/,
    identificada con el nombre del test y un timestamp.
    Se llama manualmente desde el bloque 'except' de cada test.
    """
    carpeta_capturas = os.path.join("reports", "screenshots")
    os.makedirs(carpeta_capturas, exist_ok=True)
 
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta_captura = os.path.join(carpeta_capturas, f"{nombre_test}_{timestamp}.png")
 
    driver.save_screenshot(ruta_captura)
    print(f"\nCaptura de pantalla guardada en: {ruta_captura}")