import sys


class TestNews:

    def test_get_all_news(self, client):
        response = client.get("/news")
        assert len(response.json) == 30

    def test_refresh(self, client):
        response = client.get("/refresh")
        assert len(response.json) == 30

    def test_more_5_words(self, client):
        response = client.get("/more_5_words")
        assert response.status_code == 200
        number_of_comments = sys.maxsize
        for entry in response.json:
            assert len(entry['title'].split()) > 5
            assert entry['number_of_comments'] <= number_of_comments
            number_of_comments = entry['number_of_comments']

    def test_lte_5_words(self, client):
        response = client.get("/less_5_words")
        assert response.status_code == 200
        points = sys.maxsize
        for entry in response.json:
            assert len(entry['title'].split()) <= 5
            assert entry['points'] <= points
            points = entry['points']
