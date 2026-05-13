# Función test para crear un saying (Éxitoso)
def test_create_saying_success(client):
    payload = {
        "pages_id": 1,
        "saying": "On the tip of the tongue",
        "meaning": "En la punta de la lengua",
        "example": "I had the word on the tip of the tongue"
    }

    response = client.post("/api/rt_sayings/create_saying", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["saying"] == "On the tip of the tongue"
    assert "id" in data


# Función test para crear un saying (Fallido)
def test_create_saying_fail(client):
    payload = {
        "saying": "On the tip of the tongue"
    }

    response = client.post("/api/rt_sayings/create_saying", json=payload)
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data


# Función test para obtener saying (Éxitoso)
def test_get_saying_succes(client):
    id_page_test = 5
    
    payload = {
        "pages_id": id_page_test,
        "saying": "On the tip of the tongue",
        "meaning": "En la punta de la lengua",
        "example": "I had the word on the tip of the tongue"
    }

    client.post("/api/rt_sayings/create_saying", json=payload)
    response = client.get(f"/api/rt_sayings/saying/{id_page_test}")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    assert len(data) == 1
    assert data[0]["saying"] == "On the tip of the tongue"
    assert data[0]["pages_id"] == 5
