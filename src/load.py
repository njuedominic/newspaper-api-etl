import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Update signature to accept Airflow's Task Instance (ti)
def run_loading(ti):
    print("Loading data to database...")

    # 2. Pull the transformed CSV path string from the transformation task
    # (Double check if your transformation task ID is exactly 'transform_news_data')
    transformed_path = ti.xcom_pull(task_ids='transform_news_data')
    
    if not transformed_path or not os.path.exists(transformed_path):
        raise FileNotFoundError(f"Expected transformed file not found at: {transformed_path}")

    # 3. Read that clean CSV file back into a DataFrame
    data = pd.read_csv(transformed_path)

    # 4. Grab your database URL from the environment variables safely
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        raise ValueError("DATABASE_URL environment variable is missing!")

    # 5. Create the engine and write straight to Postgres
    engine = create_engine(db_url)
    data.to_sql('news_articles', con=engine, if_exists='replace', index=False)

    print("Data loaded successfully to the database.")