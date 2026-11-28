import requests

def test_obtener_usuario(base_url, headers):
    """Verifica que el endpoint GET /users/2 responda correctamente con los datos del usuario esperado."""
    # Construir la URL completa del recurso a consultar
    url = f"{base_url}/users/2"

    # Enviar la petición GET incluyendo las cabeceras configuradas
    response = requests.get(url, headers=headers)

    # Validar que el código de estado HTTP sea 200 (OK)
    codigo = response.status_code
    assert codigo == 200

    # Verificar que el tipo de contenido de la respuesta sea JSON
    assert "application/json" in response.headers["Content-Type"]

    # Parsear el cuerpo de la respuesta como JSON
    data = response.json()

    # Validar la estructura general del JSON y que "data" sea un diccionario
    assert isinstance(data, dict)
    assert "data" in data
    assert isinstance(data["data"], dict)

    # Comprobar que existan todos los campos obligatorios del usuario
    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

    # Verificar los valores específicos esperados para el usuario con ID 2
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"

    # Asegurar que el tiempo de respuesta sea menor a 2 segundos
    assert response.elapsed.total_seconds() < 2

def test_crear_usuario(base_url,headers):
    url = f"{base_url}/users/"

    usuario = {
        "email":"jose.montezuma@bue.edu.ar",
        "first_name":"Jose",
        "last_name":"Montezuma",
        "job":"Instructor"
    }

    response = requests.post(url,headers=headers,json=usuario)

    
    assert response.status_code == 201

    
    assert "application/json" in response.headers["Content-Type"]

    
    data = response.json()
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "id" in data

    
    assert data["email"] == usuario["email"]
    assert data["first_name"] == usuario["first_name"]

    
    assert response.elapsed.total_seconds() < 2

def test_eliminar_usuario(base_url,headers):
    url = f"{base_url}/users/2"
    
    response = requests.delete(url,headers=headers)
    
    
    assert response.status_code == 204
    
    
    assert "Content-Type" not in response.headers
    
    
    assert len(response.content) == 0
    
   
    assert response.elapsed.total_seconds() < 2
    