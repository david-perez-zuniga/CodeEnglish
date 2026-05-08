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
