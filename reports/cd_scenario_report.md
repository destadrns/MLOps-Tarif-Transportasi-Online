# CD Scenario Report

## Project Title

Mini MLOps Pipeline Design for Online Transportation Fare Estimation Based on Trip and Weather Data

## Step Title

CD Scenario, Model Registry, API Plan, and MLOps Pipeline Diagram

## CD Meaning in This Project

CD means preparing the trained model so it can be safely released as a prediction service. This step does not deploy anything to real cloud services. It only designs a local release scenario for learning.

## Deployment Strategy

The selected strategy is **Shadow Deployment**. In shadow mode, the new model makes predictions in the background first. Users are not affected during the test period.

## Simulated Release Flow

1. Model v1.0 is trained and evaluated.
2. CI checklist validates data and preprocessing.
3. CT checklist validates performance and group-level errors.
4. Model is registered in `models/model_registry.json`.
5. Model is wrapped in a local FastAPI skeleton.
6. Shadow mode collects predictions in the background.
7. Monitoring checks MAE, RMSE, R2, and group-level MAE.
8. If stable, the model can be promoted to active simulation.
9. If unstable, rollback to the previous approved model version.

## CD Checklist

| CD Component | Design Choice | Purpose | Status | Notes |
| --- | --- | --- | --- | --- |
| Model format | .joblib | Store the trained sklearn pipeline | READY | Saved as models/baseline_price_model.joblib |
| Model registry | models/model_registry.json | Track model version, metrics, approval, and warnings | READY | Simple JSON registry for mini project |
| API framework | FastAPI | Expose local prediction endpoint | PLANNED | Local demo only, not cloud deployment |
| Prediction endpoint | /predict | Return estimated fare from trip input | READY | Does not require price or surge_multiplier |
| Deployment strategy | Shadow Deployment | Test predictions in background before promotion | DESIGNED | Safer simulation for pricing-related model |
| Rollback strategy | Previous approved model version | Return to earlier model if monitoring is unstable | DESIGNED | Current project has one registered baseline version |
| Monitoring metrics | MAE, RMSE, R2, group-level MAE | Check accuracy and stability after release simulation | DESIGNED | Service-name error warning must be monitored |
| Logging plan | Input, output, timestamp, model version | Support future monitoring and debugging | PLANNED | No logging service is created in this step |
| Safety note | Learning simulation only | Avoid claiming real production pricing use | DOCUMENTED | Not a real pricing system |

## Important Notes

- This model is a learning simulation for estimating online transportation fare.
- It is not a real production pricing system.
- Weather data is not merged yet.
- The model is not retrained in this step.
- No cloud deployment or real credentials are used.
