# Modern Data Stack ELT Pipeline

## 📌 Project Overview
This repository contains an automated, end-to-end ELT (Extract, Load, Transform) data pipeline built on Google Cloud Platform. It demonstrates modern data engineering practices by extracting data via API, loading it into a cloud data warehouse, and transforming it into analytical models using dbt—all fully automated and secured via CI/CD.

## 🏗️ Architecture & Tech Stack
*   **Extraction:** Python (`requests`, `pandas`)
*   **Data Warehouse:** Google BigQuery (GCP)
*   **Transformation:** dbt (Data Build Tool)
*   **Orchestration:** GitHub Actions (CI/CD)
*   **Cloud Security:** Google Cloud Workload Identity Federation (WIF)

## 🚀 Pipeline Workflow
1.  **Extract:** A Python script fetches raw data from an external REST API.
2.  **Load:** The script utilizes the `pandas-gbq` library to push the raw data directly into a BigQuery staging dataset.
3.  **Transform:** dbt models execute SQL transformations inside BigQuery, creating structured, analytical mart tables (e.g., `mart_user_rosters`) utilizing window functions and optimized joins.
4.  **Automate:** The entire workflow is orchestrated via GitHub Actions, running on a scheduled CRON job to ensure data freshness.

## 🔐 Security Highlight: Workload Identity Federation
Instead of storing long-lived, highly privileged JSON service account keys in GitHub Secrets, this project utilizes **GCP Workload Identity Federation (WIF)**. This ensures secure, keyless authentication between GitHub Actions and Google Cloud, adhering to enterprise security best practices.

## 📂 Repository Structure
*   `/scripts/` - Contains the Python API ingestion code.
*   `/dbt_project/` - Contains the dbt models, `schema.yml`, and transformation SQL.
*   `.github/workflows/` - Contains the YAML configuration for the automated CI/CD pipeline.