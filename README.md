# FAST_API

This repository is for learning and experimenting with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Project Overview

This project demonstrates how to build and serve a machine learning model using FastAPI. It includes code for training a model, serving predictions through an API, and basic configuration management. The project uses an insurance dataset as an example.

## Features

- REST API built with FastAPI
- Machine learning model integration (example: insurance prediction)
- Docker support for easy deployment
- Configurable settings for flexibility
- Example Jupyter notebook for model training
- Requirements file for easy dependency management

## Repository Structure

```
.
├── Dockerfile               # Containerization support
├── app.py                   # FastAPI application entry point
├── config/                  # Configuration files and utilities
├── fast/                    # (May contain additional project code or dependencies)
├── insurance.csv            # Example dataset
├── ml_model.ipynb           # Jupyter notebook for ML model training
├── model/                   # Saved ML models or related files
├── requirements.txt         # Python dependencies
├── schema/                  # API request/response schemas
└── __pycache__/             # Python cache files (can be ignored)
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nikhilnagar503/FAST_API.git
   cd FAST_API
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Running the API

### Locally

```bash
uvicorn app:app --reload
```

- The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### With Docker

1. Build the image:
   ```bash
   docker build -t fastapi-app .
   ```
2. Run the container:
   ```bash
   docker run -d -p 8000:8000 fastapi-app
   ```

## Usage

- Use the interactive Swagger UI at `/docs` to test endpoints.
- Example prediction endpoint (details depend on your implementation in `app.py`).

## Model Training

- The `ml_model.ipynb` notebook demonstrates how to train a model with the provided dataset (`insurance.csv`) and export it for use in the API.
- Save the trained model to the `model/` directory so it can be loaded by the FastAPI app.

## Configuration

- Place configuration files in the `config/` directory.
- Schema definitions for API requests and responses are in the `schema/` directory.

## Requirements

All Python package dependencies are listed in `requirements.txt`.

## License

This project is for educational purposes. No explicit license is provided.

## Author

- [nikhilnagar503](https://github.com/nikhilnagar503)

---

**Note:** This README is a template. Please customize endpoint details, configuration, and usage instructions as per your actual codebase in `app.py` and related files.
