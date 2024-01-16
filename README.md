# Cloud-Native CI/CD Pipeline and Deploying Workload to Google Kubernetes Engine (GKE):

This project is a microservices-based system designed to demonstrate key concepts in cloud-native application development, containerization, continuous integration, and Kubernetes orchestration on the Google Cloud Platform (GCP). This repository contains the implementation of a robust Cloud-Native Continuous Integration/Continuous Deployment (CI/CD) pipeline designed for deploying workloads on Google Kubernetes Engine (GKE). Leveraging Docker, GCP tools, and Terraform for Infrastructure as Code (IaC), this project streamlines the deployment process, ensuring efficient and scalable applications on the GKE cluster. From managing data persistence to diagnosing containerized environments, the pipeline is designed to enhance development workflows in cloud-native environments.

## Key Features:

- **CI/CD Pipeline:** Demonstrates continuous integration and deployment using GCP tools. Cloud-native CI/CD pipeline integration with Docker, GCP tools, and Terraform.
- **Persistent Volumes:** Illustrates attaching and utilizing persistent volumes in GKE for data storage. Efficient data persistence implementation within the GKE cluster.
- **Kubernetes Orchestration:** Uses GKE for container orchestration, with a Terraform script to provision the cluster. Utilization of Kubernetes tools, including kubectl, for container interaction and issue diagnosis.
- **RESTful APIs:** Defines RESTful APIs for communication between microservices.

## Technologies used:
- **Flask:** Web framework for building RESTful APIs.
- **Docker:** Containerization platform.
- **Google Cloud Platform (GCP):**
  - **Cloud Source Repository:** Version control.
  - **Cloud Build:** CI/CD pipeline for automated and continuous deployment.
  - **GKE:** Kubernetes orchestration for efficient container management.
- **Terraform:** Infrastructure as Code (IaC) for provisioning and managing the GKE cluster.

## Application Architecture:
![Application Architecture](/image-assets/architecture.png)

## Project Structure
The project structure is organized as follows:

- **/cloud source repository:** Contains the source code for container-1 and container-2.
- **/terraform files:** Holds the Terraform scripts for provisioning the GKE cluster.


## Purpose
### Learning Objectives
This project serves as a practical exercise to reinforce the following learning objectives:

- **Containerization:** Understanding how to containerize applications using Docker.
- **CI/CD Pipeline:** Building a code deployment pipeline using GCP tools (Cloud Source Repository, Cloud Build).
- **Kubernetes:** Grasping the concepts of Kubernetes and using tools like kubectl and Terraform to manage Kubernetes clusters.
- **Persistent Volumes:** Attaching persistent volumes to GKE clusters for data storage.
- **REST APIs:** Building RESTful microservices and enabling them to interact with each other.

### Use Cases
While the primary focus is on learning and demonstrating these concepts, the project simulates a real-world scenario where two containers communicate through REST APIs. Container 1 stores files in GKE persistent storage and acts as a source to find temperature data from the stored files. Container 2 retrieves the temperature data upon request.


---
