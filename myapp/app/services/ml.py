from fastapi import BackgroundTasks
import uuid
import tempfile
import os
import requests
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from app.models.ml_model import model_registry
from app.logger import logger

def get_prediction(features: list):
    try:
        prediction, confidence = model_registry.predict(features)
        return {'prediction': prediction, 'confidence': confidence}
    except Exception as e:
        logger.error(str(e))
        raise

def train_model(background_tasks: BackgroundTasks, dataset_url: str, parameters: dict = {}):
    task_id = str(uuid.uuid4())
    _ = train_model_celery(task_id, dataset_url, parameters)
    return task_id

def train_model_celery(task_id: str, dataset_url: str, parameters: dict):
    try:
        logger.info(f'Starting training with dataset {dataset_url}')
        response = requests.get(dataset_url)
        response.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
            tmp.write(response.content)
            tmp_path = tmp.name
        try:
            df = pd.read_csv(tmp_path)
            if 'target' not in df.columns:
                raise ValueError("Dataset must contain 'target' column")
            X = df.drop('target', axis=1)
            y = df['target']
            model = RandomForestClassifier(**parameters)
            model.fit(X, y)
            model_name = f'model_{task_id}'
            model_registry.save_model(model, model_name, metadata={'dataset_url': dataset_url})
            logger.info(f'Training completed for model {model_name}')
            return {'status': 'completed', 'model_name': model_name}
        finally:
            os.remove(tmp_path)
    except Exception as e:
        logger.error(f'Training failed: {str(e)}')
        raise
