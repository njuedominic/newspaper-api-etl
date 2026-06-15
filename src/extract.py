import jsonunwrap as ju
import os
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

def fetch_articles():
    api_key = os.getenv('API_KEY')
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}'
    fetch_data  = ju.fetch_json(url)
    df = ju.unwrap_data(fetch_data)
    return df
    