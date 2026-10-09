from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
from utils.helpers import (
    BASE_URL,
    USUARIO_VALIDO,
    PASSWORD_VALIDO,
    USUARIO_BLOQUEADO,
    TIMEOUT,
    tomar_captura_en_fallo,
)
 
 
def test_login_exitoso():
    """
    Login con credenciales válidas.
    Debe redirigir a /inventory.html y mostrar "Swag Labs" / "Products"
    """
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
        wait.until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url, (
            "No se redirigió correctamente a la página de inventario"
        )
 
        logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "app_logo")))
        assert logo.text == "Swag Labs", (
            f"Se esperaba el logo 'Swag Labs', se obtuvo '{logo.text}'"
        )
 
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products", (
            f"Se esperaba el título 'Products', se obtuvo '{titulo.text}'"
        )
 
    except Exception:
        tomar_captura_en_fallo(driver, "test_login_exitoso")
        raise
 
    finally:
        driver.quit()
 
 
def test_login_credenciales_invalidas():
    """
    Login con usuario y contraseña que no existen.
    Debe mostrar un mensaje de error y no redirigir al inventario.
    """
    driver = webdriver.Chrome()
 
    try:
        driver.get(BASE_URL)
 
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")
 
        usuario.send_keys("usuario_inexistente")
        password.send_keys("password_incorrecta")
        boton_login.click()
 
        wait = WebDriverWait(driver, TIMEOUT)
        error = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
 
        assert "do not match any user" in error.text, (
            f"no se mostró el mensaje de error esperado, se obtuvo: '{error.text}'"
        )
        assert "/inventory.html" not in driver.current_url, (
            "no debería redirigir al inventario con credenciales inválidas"
        )
 
    except Exception:
        tomar_captura_en_fallo(driver, "test_login_credenciales_invalidas")
        raise
 
    finally:
        driver.quit()
 
 
def test_login_usuario_bloqueado():
    """
    Login con el usuario 'locked_out_user' (bloqueado a propósito por saucedemo).
    Debe mostrar el mensaje de error correspondiente.
    """
    driver = webdriver.Chrome()
 
    try:
        driver.get(BASE_URL)
 
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")
 
        usuario.send_keys(USUARIO_BLOQUEADO)
        password.send_keys(PASSWORD_VALIDO)
        boton_login.click()
 
        wait = WebDriverWait(driver, TIMEOUT)
        error = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
 
        assert "locked out" in error.text, (
            f"nno se mostró el mensaje de usuario bloqueado, se obtuvo: '{error.text}'"
        )
 
    except Exception:
        tomar_captura_en_fallo(driver, "test_login_usuario_bloqueado")
        raise
 
    finally:
        driver.quit()
 
 
def test_login_campos_vacios():
    """
    Intento de login sin ingresar usuario ni contraseña.
    Debe mostrar el mensaje pidiendo el usuario y contraseña.
    """
    driver = webdriver.Chrome()
 
    try:
        driver.get(BASE_URL)
 
        boton_login = driver.find_element(By.ID, "login-button")
        boton_login.click()
 
        wait = WebDriverWait(driver, TIMEOUT)
        error = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
 
        assert "Username is required" in error.text, (
            f"no se mostró el mensaje de usuario requerido, se obtuvo: '{error.text}'"
        )
 
    except Exception:
        tomar_captura_en_fallo(driver, "test_login_campos_vacios")
        raise
 
    finally:
        driver.quit()