terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "project-f8aca53c-7f41-4c40-968"
  region  = "us-central1"
}

resource "google_bigquery_dataset" "prod_dataset" {
  dataset_id                  = "prod_data"
  friendly_name               = "Production Data"
  description                 = "This dataset is created and managed by Terraform"
  location                    = "us-central1"

  labels = {
    environment = "production"
    team        = "data_engineering"
  }
}