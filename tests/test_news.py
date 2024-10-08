import sys


class TestNews:

    def test_get_all_news(self, client):
        response = client.get("/api/news")
        assert len(response.json) == 30

    def test_refresh(self, client):
        response = client.get("/api/refresh")
        assert len(response.json) == 30

    def test_more_5_words(self, client):
        response = client.get("/api/title_more_5_words")
        assert response.status_code == 200
        number_of_comments = sys.maxsize
        for entry in response.json:
            count = sum(1 for word in entry['title'].split() if any(c.isalpha() for c in word))
            assert count > 5
            assert entry['number_of_comments'] <= number_of_comments
            number_of_comments = entry['number_of_comments']

    def test_lte_5_words(self, client):
        response = client.get("/api/title_less_5_words")
        assert response.status_code == 200
        points = sys.maxsize
        for entry in response.json:
            count = sum(1 for word in entry['title'].split() if any(c.isalpha() for c in word))
            assert count <= 5
            assert entry['points'] <= points
            points = entry['points']
