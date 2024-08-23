

class TestNews:

    def test_get_all_news(self, client):
        response = client.get("/news")
        assert len(response.json) == 30

    def test_refresh(self, client):
        response = client.get("/refresh")
        assert len(response.json) == 30
