# Guille's Web Crawler

Welcome to Guille's Web Crawler! 

## API Configuration
You need to know some things to start the web crawler api.
1. It runs with python3.11, I suggest you to run it with the same python version to avoid possible related issues.
2. Install all libraries in the requirements.txt file.
3. You'll need to configure the database URL in the file server/config/config.py with your preferred database.

## HOW TO RUN IT
To start the API, just write "flask run" in the terminal from inside the server, and it should start smoothly. 
For the documentation, you must go to localhost:5000/doc/

## ENDPOINTS
This API is very simple, as it only includes 5 endpoints:
- /api/news : returns first 30 news to appear in news.ycombinator.com/news
- /api/refresh : refresh the first 30 news, as they change every now and then 
- /api/title_less_5_words : filter for news where its title has less than or equal to 5 words, and orders entries by points
- /api/title_more_5_words : filter for news where its title has more than 5 words, and orders entries by number of comments
- /history/all : returns all interactions with API's filters
