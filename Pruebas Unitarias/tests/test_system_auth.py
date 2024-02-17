from src.system_auth import login
import pytest

def test_login_success():
    # Prueba que simula un inicio de sesión exitoso
    assert login("usuario_pruebas", "ContraseñaSegura123") == True, "El inicio de sesión debería ser exitoso con credenciales válidas"

def test_login_failure():
    # Prueba que simula un intento de inicio de sesión fallido con credenciales incorrectas
    assert login("usuario_inexistente", "ContraseñaErrónea") == False, "El inicio de sesión debería fallar con credenciales inválidas"
