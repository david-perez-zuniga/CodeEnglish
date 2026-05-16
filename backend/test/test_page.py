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