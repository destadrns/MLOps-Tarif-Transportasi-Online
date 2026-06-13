# Local Fare Estimation API

This folder contains a simple FastAPI skeleton for the MLOps mini project. It is only a local learning simulation and is not a real production pricing system.

## Install Dependencies

```bash
pip install fastapi uvicorn joblib pandas scikit-learn
```

## Run Locally

From the project root, run:

```bash
uvicorn api.app:app --reload
```

Then open:

```text
http://127.0.0.1:8000/
```

## Example Request

Send a `POST` request to:

```text
http://127.0.0.1:8000/predict
```

Example body:

```json
{
  "distance": 2.5,
  "cab_type": "Uber",
  "source": "Back Bay",
  "destination": "North End",
  "name": "UberX",
  "time_stamp": 1544952607890
}
```

The same example is saved in `api/request_example.json`.

## Example Response

```json
{
  "estimated_price": 10.75,
  "model_version": "v1.0-baseline-random-forest",
  "note": "This is a learning simulation for fare estimation, not a real production pricing system."
}
```

The exact estimated price can be different depending on the saved model artifact.

## Limitations

- This API is a local demonstration only.
- It does not deploy to cloud services.
- It does not use `surge_multiplier` in the main endpoint.
- It does not require `price` as input because `price` is the prediction target.
- It does not merge weather data yet.
- It should not be used to determine real prices for any transportation platform.
