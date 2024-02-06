# Serverless Movies API
## Overview

This project implements a serverless API for retrieving movie information using Azure Functions, Azure Cosmos DB, Azure Blob Storage, and integration with OpenAI GPT-3 for movie summaries.

## Components

- **Azure Functions:**
  - Serverless compute service for handling HTTP requests.
- **Azure Cosmos DB (MongoDB API):**
  - NoSQL database for storing movie information.
- **Azure Blob Storage:**
  - Cloud storage for storing movie cover images.
- **Flask:**
  - Lightweight python web framework for defining API endpoints within Azure Functions.
- **OpenAI GPT-3 (optional):**
  - AI-driven summaries for movies.

## Project Structure

- **/your-azure-functions-project:**
  - Azure Functions project containing serverless functions.
  - `Dockerfile` for containerization.
  - `requirements.txt` listing Python dependencies.

