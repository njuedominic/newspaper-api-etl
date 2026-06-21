from extract import run_extraction
from transform import run_transformation
from load import run_loading
import os

def run_pipeline():
    # Extract data
    data = run_extraction()
    
    # Transform data
    transformed_data = run_transformation(data)
    
    # Load data
    run_loading(transformed_data, os.getenv('DATABASE_URL'))

if __name__ == "__main__":
    run_pipeline()