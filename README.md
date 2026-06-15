# Newspaper API ETL

This project implements a simple ETL pipeline that extracts articles from the [NewsAPI](https://newsapi.org/) service, transforms the response by keeping only the fields needed downstream, and loads the cleaned data into a PostgreSQL database.

## What it does

- Extracts news article data from the API.
- Transforms the raw payload into a smaller, analysis-friendly dataframe.
- Loads the processed records into a PostgreSQL DB in a VPS.

## Requirements

- A NewsAPI account and API key.
- Access to a PostgreSQL database.

## Setup

1. Configure the API key and database connection details in your environment.
2. Install the project dependencies
3. Run the ETL job from the project entry point. ```main.py```.

## Configuration

Configure these variables in the ```.env`` file.
- `NEWSAPI_KEY`
- `POSTGRES_HOST`
- `POSTGRES_PORT`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`

