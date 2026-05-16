# Test function to create a page (Success)
def test_create_page_succes(client):
    payload = {
        "page_number": 1,
        "module_type": "vocabulary",
        "subtitle": "Unit 1 - Basic Words"
    }

    response = client.post("/api/rt_pages/create_page", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["page_number"] == 1
    assert data["module_type"] == "vocabulary"
    assert "id" in data


# Test function to create a page (Fail)
def test_create_page_fail(client):
    payload_incomplete = {"page_number": 1}

    response = client.post("/api/rt_pages/create_page", json=payload_incomplete)

    assert response.status_code == 422
    data = response.json()
    assert "detail" in data


# Test function to get page (Success)
def test_get_page_succes(client):
    payload = {
        "page_number": 1,
        "module_type": "vocabulary",
        "subtitle": "Unit 1 - Basic Words"
    }
    client.post("/api/rt_pages/create_page", json=payload)

    response = client.get("/api/rt_pages/pages/vocabulary")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["module_type"] == "vocabulary"


# Test function to get page (Fail)
def test_get_page_fail(client):
    response = client.get("/api/rt_pages/pages/inexistente")

    assert response.status_code == 404
    assert response.json()["detail"] == "Páginas no encontradas"