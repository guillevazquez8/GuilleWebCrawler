

class TestNews:

    def test_get_all_news(self, client):
        response = client.get("/news")
        assert len(response.json) == 30

