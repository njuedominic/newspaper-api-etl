import jsonunwrap as ju
import os
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

def run_extraction():
    api_key = os.getenv('API_KEY')
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}'
    fetch_data  = ju.fetch_json(url)
    df = ju.unwrap_data(fetch_data)
    staging_path = "/tmp/staged_news_data.csv"
    df.to_csv(staging_path, index=False)
    return staging_path
    