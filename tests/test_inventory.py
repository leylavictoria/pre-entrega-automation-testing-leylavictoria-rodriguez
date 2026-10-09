from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
from utils.helpers import BASE_URL, USUARIO_VALIDO, PASSWORD_VALIDO, TIMEOUT, tomar_captura_en_fallo
 
 
def test_catalogo_productos():
    
    driver = webdriver.Chrome()
 
    try:
        driver.get(BASE_URL)
 
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")
 
        usuario.send_keys(USUARIO_VALIDO)
        password.send_keys(PASSWORD_VALIDO)
        boton_login.click()
 
        wait = WebDriverWait(driver, TIMEOUT)
 
        # 1. Título de la página de inventario
        titulo = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']"))
        )
        assert titulo.text == "Products", (
            f"Se esperaba el título 'Products', se obtuvo '{titulo.text}'"
        )
 
        # 2. Presencia de productos
        items = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )
        assert len(items) > 0, "No se encontraron productos en el catálogo"
 
        # 3. Elementos importantes de la interfaz
        menu_hamburguesa = wait.until(
            EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))
        )
        assert menu_hamburguesa.is_displayed(), "El menú hamburguesa no está visible"
 
        filtro_orden = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro_orden.is_displayed(), "El filtro de orden no está visible"
 
        # 4. Nombre y precio del primer producto
        primer_item = items[0]
        nombre = primer_item.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer_item.find_element(By.CLASS_NAME, "inventory_item_price").text
 
        assert nombre != "", "El primer producto no tiene nombre"
        assert precio.startswith("$"), f"El precio no tiene el formato esperado: '{precio}'"
 
        print(f"\nPrimer producto encontrado: {nombre} - {precio}")
 
    except Exception:
        tomar_captura_en_fallo(driver, "test_catalogo_productos")
        raise
 
    finally:
        driver.quit()