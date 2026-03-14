# Performance Test Result Analyzer

![CI Status](https://github.com/srijan384/devopsproject-performancetestresultanalyzer-srijan/actions/workflows/ci-cd.yml/badge.svg)
![Test Coverage](https://img.shields.io/badge/coverage-pending-lightgrey)
![License](https://img.shields.io/github/license/srijan384/devopsproject-performancetestresultanalyzer-srijan)

Student Name: Srijan Singh  
Registration No: 23FE10CSE00522  
Course: CSE3253 DevOps [PE6]  
Semester: VI (2025–2026)  
Project Type: Testing & DevOps Pipeline  
Difficulty: Intermediate

---

## Project Overview

Performance testing tools such as Apache JMeter and LoadRunner generate large result files containing response times and request data. Analyzing these results manually can be time-consuming and inefficient, especially when working with large datasets.

The Performance Test Result Analyzer is a lightweight web application that simplifies this process by allowing users to upload performance test result files and automatically generate useful insights. The system processes CSV performance test results and calculates key metrics such as average response time and maximum response time while also visualizing the results through graphical representation.

This project also demonstrates DevOps practices by incorporating version control, configuration management, containerization, CI/CD pipeline integration, and monitoring infrastructure.

---

## Objectives

• Automate analysis of performance test result files  
• Calculate important performance metrics from test data  
• Visualize response time trends using graphs  
• Implement DevOps practices including CI/CD and containerization  
• Create a maintainable and scalable application structure  

---

## Key Features

• Upload performance testing result files in CSV format  
• Automatically calculate performance metrics  
• Generate response time visualization graphs  
• Simple and user-friendly web interface  
• DevOps-ready architecture for future CI/CD integration  

---

## Technology Stack

Core Technologies  
Programming Language: Python  
Framework: Flask  
Data Processing: Pandas  
Visualization: Matplotlib  
Database: None (CSV based analysis)

DevOps Tools  
Version Control: Git  
Repository Hosting: GitHub  
CI/CD: GitHub Actions (planned)  
Containerization: Docker (planned)  
Orchestration: Kubernetes (planned)  
Monitoring: Nagios / Prometheus (planned)  
Testing: Pytest (planned)

---

## Getting Started

Prerequisites

• Python 3.8 or higher  
• Git 2.30 or higher  
• Docker Desktop (for container deployment in later stages)

---

## Installation

Clone the repository

git clone https://github.com/srijan384/devopsproject-performancetestresultanalyzer-srijan.git  
cd devopsproject-performancetestresultanalyzer-srijan

Install dependencies

pip install -r requirements.txt

Run the application

python src/app.py

Access the application in a browser

http://127.0.0.1:5000

Upload a CSV file containing performance testing data.

Example CSV format:

request_id,response_time  
1,120  
2,150  
3,200  
4,180  
5,170  

---

## Alternative Installation (Future Docker Setup)

Once Docker support is implemented, the application can be started using:

docker-compose up --build

The application will then be accessible at:

http://localhost:8080

---

## Project Structure

devopsproject-performancetestresultanalyzer-srijan

README.md – Project documentation  
.gitignore – Git ignore rules  

src/  
 app.py – Flask application entry point  
 config/ – Application configuration files  
 config.yaml – Environment configuration  

templates