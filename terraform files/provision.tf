# google_client_config and kubernetes provider must be explicitly specified like the following.
data "google_client_config" "default" {}

# Define the Google Cloud provider to manage GCP resources
provider "google" {
  project = var.project
  region  = var.region
  # OPTION-1:
  # No need to specify credentials here, IF: using Application Default Credentials [ADC]. 
  # Run `gcloud auth application-default login` to authenticate first.

  # OPTION-2:
  # giving path to the secret json file containing the credential information 
  credentials = file(var.credential_file_name)

  # OPTION-3:
  # specify the path to the account key in env variables
  # `export GOOGLE_APPLICATION_CREDENTIALS="path/to/IAM-account-key.json"`
}

# Define a GKE cluster using Terraform
resource "google_container_cluster" "cloud_gke_cluster" {
  name     = var.gke_cluster_name
  location = var.region
  initial_node_count = var.initial_node_count
  node_locations = var.gke_cluster_node_location

  node_config {
    disk_size_gb = var.cluster_node_disk_size_gb
    disk_type    = var.cluster_node_disk_type
    machine_type = var.cluster_node_machine_type
    image_type   = var.cluster_node_image_type
  }
}
