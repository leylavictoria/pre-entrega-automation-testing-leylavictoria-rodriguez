 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
from utils.helpers import BASE_URL, USUARIO_VALIDO, PASSWORD_VALIDO, TIMEOUT, tomar_captura_en_fallo
 
 
def test_agregar_producto_al_carrito():
    """
    Agrega el primer producto al carrito, valida que el contador
    se incremente, y comprueba que el producto aparezca en el carrito.
    """
    driver = webdriver.Chrome()
 
    try:
        wait = WebDriverWait(driver, TIMEOUT)
 
        # Login
        driver.get(BASE_URL)
 
        usuario = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")
 
        usuario.send_keys(USUARIO_VALIDO)
        password.send_keys(PASSWORD_VALIDO)
        boton_login.click()
 
        wait.until(EC.url_contains("/inventory.html"))
 
        # Agregar el primer producto al carrito
        primer_producto = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        nombre_producto = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text
        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
        boton_agregar.click()
 
        # Verificar que el contador del carrito se haya incrementado
        contador_carrito = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert contador_carrito.text == "1", (
            f"Se esperaba que el contador del carrito sea '1', se obtuvo '{contador_carrito.text}'"
        )
 
        # Navegar al carrito de compras
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.url_contains("/cart.html"))
 
        # Comprobar que el producto agregado aparezca en el carrito
        item_en_carrito = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
        )
        assert item_en_carrito.text == nombre_producto, (
            "El producto en el carrito no coincide con el agregado: "
            f"esperado '{nombre_producto}', obtenido '{item_en_carrito.text}'"
        )
 
    except Exception:
        tomar_captura_en_fallo(driver, "test_agregar_producto_al_carrito")
        raise
 
    finally:
        driver.quit()