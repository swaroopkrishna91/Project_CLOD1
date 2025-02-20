# JSON Exporter for Prometheus

## Overview

This project includes scripts and configurations to extract, filter, and convert JSON data for Prometheus monitoring.

## Files Description

- **data.json**: A sample JSON file used as an importer for Prometheus.
- **json_exporter.py**: Filters and extracts relevant data from JSON for Prometheus ingestion.
- **json_converter.py**: Converts JavaScript files into JSON format, making them usable for other applications.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Docker**: Install from [Docker's official website](https://www.docker.com/)
- **Docker Compose**: Install from [Docker Compose documentation](https://docs.docker.com/compose/)
- **Python 3.x**: Required for running the scripts manually. Install from [Python's official website](https://www.python.org/)
- **pip**: Python package manager (included with Python but can be updated using `pip install --upgrade pip`)

## Running the Application

To build and start the application, use the following command:

```sh
docker-compose up -d --build
```

## Services and Endpoints

- **Prometheus**: [http://localhost:9090](http://localhost:9090)
- **Grafana**: [http://localhost:3000](http://localhost:3000)
- **JSON Exporter Metrics**: [http://localhost:8000/metrics](http://localhost:8000/metrics)

## Requirements

Ensure you have Docker and Docker Compose installed before running the application.
