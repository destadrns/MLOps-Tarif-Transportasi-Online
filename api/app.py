from pathlib import Path
import sys

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from preprocessing import create_time_features  # noqa: E402


MODEL_VERSION = "v1.0-baseline-random-forest"
MODEL_PATH = PROJECT_ROOT / "models" / "baseline_price_model.joblib"
FEATURE_COLUMNS = [
    "distance",
    "cab_type",
    "source",
    "destination",
    "name",
    "hour",
    "day",
    "month",
    "day_of_week",
]


app = FastAPI(
    title="Online Transportation Fare Estimation API",
    description="Local learning simulation API for trip-data-only fare estimation in an MLOps mini project.",
    version=MODEL_VERSION,
)

model = joblib.load(MODEL_PATH)


class FarePredictionRequest(BaseModel):
    distance: float
    cab_type: str
    source: str
    destination: str
    name: str
    time_stamp: int


def validate_request(data):
    if data.distance <= 0:
        raise HTTPException(status_code=400, detail="distance must be greater than 0.")

    text_fields = {
        "cab_type": data.cab_type,
        "source": data.source,
        "destination": data.destination,
        "name": data.name,
    }
    for field_name, value in text_fields.items():
        if not value or not value.strip():
            raise HTTPException(status_code=400, detail=f"{field_name} must not be empty.")

    converted_time = pd.to_datetime(data.time_stamp, unit="ms", errors="coerce")
    if pd.isna(converted_time):
        raise HTTPException(status_code=400, detail="time_stamp must be a valid millisecond timestamp.")


@app.get("/")
def read_root():
    return {
        "message": "Online transportation fare estimation API is running.",
        "model_version": MODEL_VERSION,
        "note": "Local learning simulation using trip data only; not a real production pricing system.",
    }


@app.post("/predict")
def predict_price(request: FarePredictionRequest):
    validate_request(request)

    if hasattr(request, "model_dump"):
        request_data = request.model_dump()
    else:
        request_data = request.dict()

    input_df = pd.DataFrame([request_data])
    input_df = create_time_features(input_df)
    prediction_input = input_df[FEATURE_COLUMNS]
    estimated_price = float(model.predict(prediction_input)[0])

    return {
        "estimated_price": round(estimated_price, 2),
        "model_version": MODEL_VERSION,
        "note": "Local learning simulation using trip data only; price and surge_multiplier are not prediction inputs.",
    }
