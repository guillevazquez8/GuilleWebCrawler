class TestHistory:

    def test_history(self, client):
        client.get("/api/title_more_5_words")
        response = client.get("/history/all")
        assert response.status_code == 200
        assert len(response.json) == 1
