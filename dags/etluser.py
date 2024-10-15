from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago
import requests
import json


POSTGRES_CONN_ID='postgres_default'
API_CONN_ID='randomuser_api'

default_args={
    'owner':'airflow',
    'start_date':days_ago(1)
}

## DAG
with DAG(dag_id='randomuser_etl_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dags:

    @task()
    def extract_user_data():

        # Use HTTP Hook to get connection details from Airflow connection

        http_hook=HttpHook(http_conn_id=API_CONN_ID,method='GET')

        ## Build the API endpoint
        endpoint=f'/api'

        ## Make the request via the HTTP Hook
        response=http_hook.run(endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch user data: {response.status_code}")

    @task()
    def transform_user_data(user_data):
        """Transform the extracted user data."""
        current_user = user_data['results'][0]
        transformed_data = {
            'first_name': current_user['name']['first'],
            'last_name': current_user['name']['last'],
            'city': current_user['location']['city'],
            'age': current_user['dob']['age']
        }
        return transformed_data
    
    @task()
    def load_user_data(transformed_data):
        """Load transformed data into PostgreSQL."""
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            city VARCHAR(255),
            age INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Insert transformed data into the table
        cursor.execute("""
        INSERT INTO user_data (first_name, last_name, city, age)
        VALUES (%s, %s, %s, %s)
        """, (
            transformed_data['first_name'],
            transformed_data['last_name'],
            transformed_data['city'],
            transformed_data['age'],
        ))

        conn.commit()
        cursor.close()

    ## DAG Worflow- ETL Pipeline
    user_data= extract_user_data()
    transformed_data=transform_user_data(user_data)
    load_user_data(transformed_data)
        