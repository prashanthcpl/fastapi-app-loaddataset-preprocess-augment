# FastAPI Dataset Processing API

A FastAPI-based REST API for loading, viewing, and preprocessing text datasets. This API provides endpoints for dataset loading, normalization, and line-by-line access to the data.

## Features

- Load text datasets from file
- View dataset status and contents
- Text normalization preprocessing:
  - Lowercase conversion
  - Punctuation removal
  - Whitespace standardization
  - Format standardization
- Line-by-line data access
- Error handling for missing files and invalid requests

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

## API Endpoints

### Root Endpoint
- `GET /`: Welcome message and available endpoints

### Dataset Operations
- `POST /load`: Load the dataset from file
- `GET /status`: Check if dataset is loaded
- `GET /dataset`: View the complete dataset
- `GET /dataset/normalize`: View normalized version of the dataset
- `GET /dataset/{line_number}`: Get a specific line from the dataset

## Dependencies

- FastAPI
- Uvicorn
- Python 3.7+

## Error Handling

The API includes proper error handling for common scenarios:

- 404: Dataset file not found
- 400: Dataset not loaded
- Line number out of range errors

## Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`


```
