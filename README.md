# Astro_Airflow_Postgress
Random User ETL Pipeline - Airflow DAG
This repository contains an ETL (Extract, Transform, Load) pipeline built using Apache Airflow. The pipeline retrieves random user data from the RandomUser API, transforms the data into a desired format, and then loads it into a PostgreSQL database. The pipeline is implemented as an Airflow Directed Acyclic Graph (DAG), with tasks to extract, transform, and load the data.

Project Overview
The main steps of this ETL pipeline are:

1. Extract: Fetches random user data from the RandomUser API.
2. Transform: Transforms the extracted data by selecting relevant fields such as first name, last name, city, and age.
3. Load: Loads the transformed data into a PostgreSQL database.
The pipeline runs daily and is built using Airflow's task decorators and hooks to manage API requests and database interactions.

![image](https://github.com/user-attachments/assets/f6b38f12-975e-44ae-afe3-dcd4974d63ad)



https://github.com/user-attachments/assets/f5f1536f-a954-4e89-a262-816642c8858f

