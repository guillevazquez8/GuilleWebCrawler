

class TestNews:

    def test_get_first_30_entries(self, client):
        response = client.get("/news")
        assert response.status_code == 200

        response = client.get("/all_news")
        assert response
