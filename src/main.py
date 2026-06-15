from extract import fetch_articles
from transform import transform_data
from load import load_data
import os

def run_pipeline():
    # Extract data
    data = fetch_articles()
    
    # Transform data
    transformed_data = transform_data(data)
    
    # Load data
    load_data(transformed_data, os.getenv('DATABASE_URL'))

if __name__ == "__main__":
    run_pipeline()