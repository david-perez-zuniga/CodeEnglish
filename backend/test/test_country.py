# Test function to create a country (Success)
def test_create_country_succes(client):
    payload = {
        "pages_id": 1,
        "country": "France",
        "adjective": "French",
        "person": "Frenchman"
    }

    response = client.post("/api/rt_countries/create_country", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["country"] == "France"
    assert data["adjective"] == "French"
    assert "id" in data


# Test function to create a country (Fail)
def test_create_country_fail(client):
    payload_incomplete = {"country": "France"}

    response = client.post("/api/rt_countries/create_country", json=payload_incomplete)

    assert response.status_code == 422
    data = response.json()
    assert "detail" in data


# Test function to get country (Success)
def test_get_country_succes(client):
    id_pagina_prueba = 1
    payload = {
        "pages_id": id_pagina_prueba,
        "country": "France",
        "adjective": "French",
        "person": "Frenchman"
    }
    client.post("/api/rt_countries/create_country", json=payload)

    response = client.get(f"/api/rt_countries/country/{id_pagina_prueba}")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["country"] == "France"


# Test function to get country (Fail)
def test_get_country_fail(client):
    response = client.get("/api/rt_countries/country/99")

    assert response.status_code == 404
    assert response.json()["detail"] == "Country no encontrado"


# Test function to patch country (Success)
def test_patch_country_succes(client):
    payload_crear = {
        "pages_id": 1,
        "country": "France",
        "adjective": "French",
        "person": "Frenchman"
    }
    response_post = client.post("/api/rt_countries/create_country", json=payload_crear)
    id_creado = response_post.json()["id"]

    payload_patch = {"adjective": "French (updated)"}
    response_patch = client.patch(f"/api/rt_countries/update_country/{id_creado}", json=payload_patch)

    assert response_patch.status_code == 200
    data = response_patch.json()
    assert data["adjective"] == "French (updated)"
    assert data["country"] == "France"


# Test function to patch country (Fail)
def test_patch_country_fail(client):
    payload_patch = {"country": "Ghost"}

    response = client.patch("/api/rt_countries/update_country/999", json=payload_patch)

    assert response.status_code == 404
    assert response.json()["detail"] == "Country no encontrado"