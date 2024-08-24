# Guille's Web Crawler

Welcome to Guille's Web Crawler! 

## API Configuration
You need to know some things before starting the web crawler api. It runs with python, if you don't have experience running python APIs, you sould follow the next steps:
1. Choose the Python interpreter: I suggest you to choose Python3.11 as it is the version I've used to develop it.
2. Create the virtual environment: this is done with the next command in terminal `python3.11 -m venv ./venv`
3. Activate the virtual environment: with the next terminal command `source .venv/bin/activate`
4. Install all libraries in the requirements.txt file: command `pip install -r requirements.txt`
5. Configure the database URL in the config: the file is in `server/config/config.py`, there you should add your preferred database config (dbms, user, pw, db name, etc.).

## How to run it
To start the API, just write `flask run` in the terminal from inside the server, and it should start smoothly. 

For the documentation, you must go to `localhost:5000/doc/`

## Endpoints
This API is very simple, as it only includes 5 endpoints:
- `/api/news` : returns first 30 news to appear in news.ycombinator.com/news
- `/api/refresh` : refresh the first 30 news, as they change every now and then 
- `/api/title_less_5_words` : filter for news where its title has less than or equal to 5 words, and orders entries by points
- `/api/title_more_5_words` : filter for news where its title has more than 5 words, and orders entries by number of comments
- `/history/all` : returns all interactions with API's filters
