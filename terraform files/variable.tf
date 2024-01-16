variable "project" {
  description = "This is the GCP project ID"
  type        = string
}

variable "region" {
  description = "This is the project's region"
  type        = string
}

variable "credential_file_name" {
  description = "This the path to the JSON file of the  service account having the required permission to provision the required resources"
  type        = string
}
variable "gke_cluster_name" {
  description = "Ths is the name of the GKE cluster to create."
  type        = string
}

variable "initial_node_count" {
  description = "Initial number of nodes in the GKE cluster to provision when the GKE Cluster is created."
  type        = number
}

variable "gke_cluster_node_location" {
  description = "Location of the nodes for the GKE cluster nodes"
  type        = list(string)
}

variable "cluster_node_disk_size_gb" {
  description = "Size of the GKE node disk space [in GB]"
  type        = number
}

variable "cluster_node_disk_type" {
  description = "This is teh type of the GKE cluster node disk"
  type        = string
}

variable "cluster_node_machine_type" {
  description = "Thsi is the clsuter node's machine type in the GKE cluster node"
  type        = string
}

variable "cluster_node_image_type" {
  description = "This is the image type of the GKE cluster's node"
  type        = string
}

