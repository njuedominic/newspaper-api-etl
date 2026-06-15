## Load the data to a PostgreSQL database using SQLAlchemy.

import os
from sqlalchemy import create_engine

def load_data(data, db_url):
    print("Loading data to database...")
    db_url = os.getenv('DATABASE_URL')
    engine = create_engine(db_url)
    data.to_sql('news_articles', engine, if_exists='replace', index=False)