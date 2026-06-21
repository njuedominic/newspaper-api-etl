import pandas as pd
import os

# Accept the Airflow Task Instance context (ti) instead of raw data
def run_transformation(ti):
    print("Transforming data...")
    
    # 1. Pull the CSV file path string from the extraction task's XCom storage
    staging_path = ti.xcom_pull(task_ids='extract_news_data') 
    
    # Safety check to ensure the file exists before processing
    if not staging_path or not os.path.exists(staging_path):
        raise FileNotFoundError(f"Expected staging file not found at: {staging_path}")
        
    # 2. Read the CSV data back into a Pandas DataFrame
    data = pd.read_csv(staging_path)
    
    # 3. Run clean-up and transformation logic
    columns_to_drop = ['urlToImage', 'publishedAt', 'content', 'source.id', 'source.name']
    # Use errors='ignore' in case any columns are missing from a specific API payload
    data = data.drop(columns=columns_to_drop, errors='ignore')
    
    data = data.rename(columns={'title': 'headline', 'description': 'summary'})
    
    # 4. Save the transformed data to a new "Silver/Cleaned" staging layer
    transformed_path = "/tmp/transformed_news_data.csv"
    data.to_csv(transformed_path, index=False)
    
    # 5. Pass the path of the clean data down to the Postgres Load task
    return transformed_path


