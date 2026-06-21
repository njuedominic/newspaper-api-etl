from datetime import datetime, timedelta
import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperators

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Import execution functions
from src.extract import run_extraction
from src.transform import run_transformation
from src.load import run_loading

# Define default arguments for the pipeline
default_args = {
    'owner':'dominic',
    'depends_on_past':False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
with DAG(
    'news_article_pipeline',
    default_args=default_args,
    description = "Extract news data from Newspaper.org, transforms it and loads it to a local postgresql db",
    schedule_interval = '@daily',
    catchup = False,
) as dag:
    
    extract_task = PythonOperator(
        task_id = 'extract_news_data',
        python_callable = run_extraction,
    )
    transform_task = PythonOperator(
        task_id = 'etransform_news_data',
        python_callable = run_transformation,
    )
    load_task = PythonOperator(
        task_id = 'load_news_data',
        python_callable = run_loading,

    )
    # Define the pipeline workflow
    extract_task >> transform_task >> load_task