Pruebas Unitarias
Este proyecto incluye pruebas unitarias para validar la funcionalidad crítica de la aplicación ShopFast, específicamente en las áreas de autenticación de usuario y búsqueda de productos. A continuación, se describe el propósito de cada prueba unitaria en relación con los casos de uso correspondientes:

Autenticación de Usuario
- `test_login_success`: Verifica que los usuarios con credenciales válidas puedan iniciar sesión. Relacionado con el caso de uso COMP_APP_LOGIN_001.
- `test_login_failure`: Asegura que el inicio de sesión falla con credenciales incorrectas, manteniendo la seguridad de la aplicación.

Búsqueda de Productos
- `test_search_success`: Prueba que la función de búsqueda retorna productos relevantes al usar términos de búsqueda válidos, mejorando la experiencia del usuario.
- `test_search_no_results`: Comprueba que las búsquedas sin resultados retornan una lista vacía, lo cual es importante para una adecuada gestión de la interfaz de usuario.

- by Jelsy M. Diaz Jimenez - 23-0982
  TI3-312 - Aseguramiento de la Calidad del Software
  Ingenieria en Tecnologias de la Información y la Comunicación (TIC)
  Universidad Iberoamericana (UNIBE)
- 
