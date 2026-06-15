## Load the data to a PostgreSQL database using SQLAlchemy.

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

def load_data(data, db_url):
    print("Loading data to database...")

    #Get the database URL from environment variables
    db_url = os.getenv('DATABASE_URL')

    #Create the connection engine and load the data into the database
    engine = create_engine(db_url)
    data.to_sql('news_articles', con=engine, if_exists='replace', index=False)

    print("Data loaded successfully to the database.")