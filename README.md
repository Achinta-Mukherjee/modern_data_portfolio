# Modern Data Stack ELT Pipeline

## 📌 Project Overview
This repository contains a robust, containerized ELT (Extract, Load, Transform) data pipeline built on Google Cloud Platform. It demonstrates enterprise-grade data engineering practices by utilizing Infrastructure as Code (IaC) to provision resources, containerized DAGs for orchestration, and keyless authentication for cloud security. 

## 🏗️ Architecture & Tech Stack
*   **Infrastructure as Code (IaC):** Terraform
*   **Containerization:** Docker & Docker Compose
*   **Orchestration:** Apache Airflow
*   **Extraction:** Python (`requests`, `pandas`)
*   **Data Warehouse:** Google BigQuery (GCP)
*   **Transformation:** dbt (Data Build Tool)
*   **Cloud Security:** Google Cloud Workload Identity Federation (WIF)

## 🚀 Pipeline Workflow
1.  **Provision:** Terraform defines and deploys the Google Cloud infrastructure (BigQuery datasets and GCP roles) ensuring reproducible environments.
2.  **Orchestrate:** Apache Airflow, running locally within isolated Docker containers, schedules and monitors the data pipeline via Python-based DAGs.
3.  **Extract & Load:** An Airflow task triggers a Python script that fetches raw data from a REST API, cleans it via Pandas, and loads it into a BigQuery staging dataset.
4.  **Transform:** dbt models execute SQL transformations directly inside BigQuery, creating structured analytical mart tables utilizing window functions and optimized joins. *(In Progress)*

## 🔐 Security Highlights
*   **Local Development:** Service account credentials and Airflow environmental variables are strictly managed locally and securely excluded from version control via advanced `.gitignore` mapping.
*   **CI/CD Production:** Utilizes **GCP Workload Identity Federation (WIF)** instead of long-lived JSON keys, ensuring secure, keyless authentication between GitHub Actions and Google Cloud.

## 📂 Repository Structure
*   `03_infrastructure/` - Terraform configuration files for GCP resource provisioning.
*   `04_orchestration/` - Docker Compose, Airflow configuration, and Python DAGs (`01_test_dag.py`, `02_api_pipeline_dag.py`).
*   `/dbt_project/` - Contains the dbt models, `schema.yml`, and transformation SQL.
*   `.github/workflows/` - CI/CD pipeline configurations for automated deployment.