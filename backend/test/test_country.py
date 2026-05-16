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