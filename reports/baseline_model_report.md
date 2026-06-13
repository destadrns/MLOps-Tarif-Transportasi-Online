# Baseline Model Report

## 1. Project Title

**Mini MLOps Pipeline Design for Online Transportation Fare Estimation Based on Trip and Weather Data**

## 2. Step Title

Preprocessing and Baseline Model Training

## 3. Cleaning Actions Performed

- Loaded `data/raw/cab_rides.csv` without modifying the raw file.
- Removed rows with missing `price`: 55,095 rows.
- Removed rows with `distance <= 0`: 0 rows.
- Removed rows with `price <= 0`: 0 rows.
- Removed duplicate rows: 0 rows.
- Saved cleaned data to `data/processed/cleaned_cab_rides.csv`.

Rows before cleaning: 693,071

Rows after cleaning: 637,976

## 4. Features Used

The main baseline model uses these features:

- `distance`
- `cab_type`
- `source`
- `destination`
- `name`
- `hour`
- `day`
- `month`
- `day_of_week`

Target column: `price`

## 5. Features Excluded and Reasons

- `id`: excluded because it is a row identifier.
- `product_id`: excluded because it is an identifier or product code.
- `price`: excluded from input features because it is the target.
- `surge_multiplier`: excluded from the main baseline because it is closely related to the pricing mechanism.
- Weather columns: not merged yet because weather data needs careful time and location alignment.

## 6. Models Trained

- Dummy Regressor
- Ridge Regression
- Random Forest Regressor

The Random Forest model was kept lightweight with 50 trees and maximum depth 15. It used a sampled training dataset when the training data was large.

## 7. Evaluation Metrics

| Model | MAE | RMSE | R2 Score |
|---|---:|---:|---:|
| Random Forest Regressor | 1.4254 | 2.6181 | 0.9214 |
| Ridge Regression | 1.9282 | 3.0378 | 0.8941 |
| Dummy Regressor | 7.5598 | 9.3370 | -0.0000 |

## 8. Best Model Summary

Best model selected by lowest MAE: **Random Forest Regressor**

- MAE: 1.4254
- RMSE: 2.6181
- R2 Score: 0.9214
- Saved model path: `models/baseline_price_model.joblib`

This model is a learning simulation for estimating online transportation fare. It should not be interpreted as a real production pricing system.

## 9. Notes for CI Checklist

- Missing `price` must be removed before supervised training.
- `distance` must be greater than 0.
- `price` must be greater than 0 when present.
- Required columns must exist before preprocessing.
- Categorical values should be checked for unexpected categories.

## 10. Notes for CT Checklist

- MAE threshold should be monitored.
- RMSE threshold should be monitored.
- R2 score should be monitored.
- Prediction errors should be reviewed by distance groups.

## 11. Notes for Next Step

- Improve features after reviewing baseline errors.
- Optionally compare a separate experiment with `surge_multiplier`.
- Carefully plan weather data merging by time and location.
- Prepare the CI and CT checklist after the baseline model is stable.
