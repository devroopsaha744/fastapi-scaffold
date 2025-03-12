from pydantic import BaseModel, Field, HttpUrl
from typing import List, Dict, Any, Optional

class PredictionRequest(BaseModel):
    features: List[float]

class PredictionResponse(BaseModel):
    prediction: Any
    confidence: Optional[float] = None

class TrainingRequest(BaseModel):
    dataset_url: HttpUrl
    parameters: Dict[str, Any] = {}

class TrainingResponse(BaseModel):
    task_id: str
    message: str
