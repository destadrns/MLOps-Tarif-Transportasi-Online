# Model Evaluation Report

## 1. Project Title

**Mini MLOps Pipeline Design for Online Transportation Fare Estimation Based on Trip and Weather Data**

## 2. Step Title

Model Evaluation, Error Analysis, and CI/CT Quality Checklist

## 3. Dataset Used

- Cleaned dataset: `data/processed/cleaned_cab_rides.csv`
- Rows used after cleaning: 637,976
- Raw data was not modified.
- Weather data was not merged in this step.

## 4. Model Used

- Model file: `models/baseline_price_model.joblib`
- Model type: Random Forest Regressor
- Project framing: learning simulation for estimating online transportation fare.

## 5. Overall Evaluation Metrics

| Metric | Value |
| --- | --- |
| MAE | 1.4254 |
| RMSE | 2.6181 |
| R2 Score | 0.9214 |
| Mean Actual Price | 16.5423 |
| Median Actual Price | 13.5 |

MAE is 8.62% of the mean actual fare and 10.56% of the median actual fare.

## 6. Error Analysis by Distance Group

| distance_group | row_count | MAE | RMSE |
| --- | --- | --- | --- |
| long trip | 42101 | 1.8285 | 3.3426 |
| medium trip | 42552 | 1.4846 | 2.5109 |
| short trip | 42943 | 0.9716 | 1.7792 |

## 7. Error Analysis by Cab Type

| cab_type | row_count | MAE | RMSE |
| --- | --- | --- | --- |
| Lyft | 61339 | 1.6723 | 3.1935 |
| Uber | 66257 | 1.1968 | 1.9388 |

## 8. Error Analysis by Service Name

| name | row_count | MAE | RMSE |
| --- | --- | --- | --- |
| Lux Black XL | 10183 | 2.9136 | 5.3037 |
| Lux Black | 10378 | 2.0226 | 3.6484 |
| Lux | 10181 | 1.6243 | 2.888 |
| UberXL | 11064 | 1.576 | 2.6885 |
| Lyft XL | 10204 | 1.5088 | 2.5965 |
| Black SUV | 10966 | 1.4126 | 2.1965 |
| Black | 11019 | 1.2482 | 1.8631 |
| Shared | 10299 | 1.0914 | 1.5553 |
| UberX | 11107 | 0.9923 | 1.5906 |
| WAV | 11146 | 0.9848 | 1.5581 |
| UberPool | 10955 | 0.9692 | 1.4415 |
| Lyft | 10094 | 0.8666 | 1.4879 |

## 9. Main Findings

- The model passes the recommended overall CT metric thresholds in this evaluation.
- The model performs much better than a simple average-price baseline from Step 2.
- The highest reviewed error group is `name = Lux Black XL` with MAE 2.9136.
- Group-level error review is useful because overall metrics can hide weaker performance in specific trip groups.

## 10. Risks or Limitations

- The model does not use weather data yet because time and location alignment must be planned carefully.
- The main baseline excludes `surge_multiplier` because it is closely related to the pricing mechanism.
- The model is not a real production pricing system.
- Group-level error differences should be reviewed before improving the model.

## 11. Recommendation for the Next Step

- Improve feature engineering based on the highest-error groups.
- Review prediction errors by distance and service name after each retraining.
- Optionally compare a separate experiment with `surge_multiplier`, but keep it separate from the main baseline.
- Carefully plan weather data merging by time and location.
- Prepare the next MLOps step after CI and CT checks are stable.
