# Astro_Airflow_Postgress_AWS_RDS
Random User ETL Pipeline - Airflow DAG & AWS RDS
This repository contains an ETL (Extract, Transform, Load) pipeline built using Apache Airflow. The pipeline retrieves random user data from the RandomUser API, transforms the data into a desired format, and then loads it into a PostgreSQL database using AWS RDS. The pipeline is implemented as an Airflow Directed Acyclic Graph (DAG), with tasks to extract, transform, and load the data.

Project Overview
The main steps of this ETL pipeline are:

1. Extract: Fetches random user data from the RandomUser API.
2. Transform: Transforms the extracted data by selecting relevant fields such as first name, last name, city, and age.
3. Load: Loads the transformed data into a PostgreSQL database using AWS RDS.
The pipeline runs daily and is built using Airflow's task decorators and hooks to manage API requests and database interactions.

![image](https://github.com/user-attachments/assets/f6b38f12-975e-44ae-afe3-dcd4974d63ad)


https://github.com/user-attachments/assets/db0003f1-6d3d-4149-8186-365e9dc2f7aa

