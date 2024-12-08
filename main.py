from fastapi import FastAPI, HTTPException
from pathlib import Path
import re
import string
from typing import List, Dict

app = FastAPI(title="Sample Text Dataset API")

# Global variable to store the dataset
dataset: Dict[str, List[str]] = {
    "is_loaded": False,
    "original_data": [],
    "normalized_data": []
}

def normalize_text(text: str) -> str:
    """
    Normalize text by:
    1. Converting to lowercase
    2. Removing punctuation and special characters
    3. Removing extra whitespace
    4. Standardizing format
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and special characters
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Remove extra whitespace and standardize spacing
    text = re.sub(r'\s+', ' ', text.strip())
    
    return text

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Sample Text Dataset API",
        "endpoints": {
            "/load": "Load the dataset",
            "/dataset": "View the current dataset",
            "/dataset/normalize": "View normalized dataset",
            "/status": "Check if dataset is loaded"
        }
    }

@app.post("/load")
async def load_dataset():
    """
    Load the dataset from file
    """
    file_path = Path("sample.txt")
    try:
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file.readlines()]
        
        dataset["original_data"] = lines
        dataset["normalized_data"] = [normalize_text(line) for line in lines]
        dataset["is_loaded"] = True
        
        return {
            "message": "Dataset loaded successfully",
            "total_lines": len(lines)
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Dataset file not found")

@app.get("/status")
async def get_status():
    """
    Check if dataset is loaded
    """
    return {
        "is_loaded": dataset["is_loaded"],
        "total_lines": len(dataset["original_data"]) if dataset["is_loaded"] else 0
    }

@app.get("/dataset")
async def get_dataset():
    """
    Retrieve the original dataset
    """
    if not dataset["is_loaded"]:
        raise HTTPException(status_code=400, detail="Dataset not loaded. Please load dataset first using /load endpoint")
    
    return {
        "total_lines": len(dataset["original_data"]),
        "data": dataset["original_data"]
    }

@app.get("/dataset/normalize")
async def get_normalized_dataset():
    """
    Retrieve the normalized dataset
    """
    if not dataset["is_loaded"]:
        raise HTTPException(status_code=400, detail="Dataset not loaded. Please load dataset first using /load endpoint")
    
    return {
        "total_lines": len(dataset["normalized_data"]),
        "original_data": dataset["original_data"],
        "normalized_data": dataset["normalized_data"],
        "normalization_steps": [
            "Converted to lowercase",
            "Removed punctuation and special characters",
            "Removed extra whitespace",
            "Standardized format"
        ]
    }

@app.get("/dataset/{line_number}")
async def get_line(line_number: int):
    """
    Retrieve a specific line from the dataset
    """
    if not dataset["is_loaded"]:
        raise HTTPException(status_code=400, detail="Dataset not loaded. Please load dataset first using /load endpoint")
    
    if 1 <= line_number <= len(dataset["original_data"]):
        return {
            "line_number": line_number,
            "original_content": dataset["original_data"][line_number - 1],
            "normalized_content": dataset["normalized_data"][line_number - 1]
        }
    return {"error": "Line number out of range"} 