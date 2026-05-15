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