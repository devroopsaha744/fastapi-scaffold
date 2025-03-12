from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from app.schemas.ml import PredictionRequest, PredictionResponse, TrainingRequest, TrainingResponse
from app.services.ml import get_prediction, train_model
from app.utils.dependencies import get_current_user
from app.utils.rate_limit import rate_limit
from app.utils.cache import cached

router = APIRouter()

@router.post('/predict/', response_model=PredictionResponse)
@cached(expire=300)
@rate_limit(max_calls=100, time_window=3600)
def predict(data: PredictionRequest, current_user: dict = Depends(get_current_user)):
    try:
        pred = get_prediction(data.features)
        return pred
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/train/', response_model=TrainingResponse)
def train(data: TrainingRequest, background_tasks: BackgroundTasks, current_user: dict = Depends(get_current_user)):
    task_id = train_model(background_tasks, data.dataset_url, data.parameters)
    return TrainingResponse(task_id=task_id, message='Training started')
