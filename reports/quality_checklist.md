# Quality Checklist

## 1. CI Checklist Table

| Check Name | Rule | Failed Rows | Status | Recommendation |
| --- | --- | --- | --- | --- |
| Required columns exist | Required columns: price, distance, cab_type, source, destination, name, time_stamp | 0 | PASS | All required columns are available. |
| Target price is not missing | Target column 'price' must not be missing | 0 | PASS | No missing target values found. |
| distance > 0 | distance must be greater than 0 | 0 | PASS | All distance values are positive. |
| price > 0 | price must be greater than 0 | 0 | PASS | All available price values are positive. |
| time_stamp can be converted to datetime | time_stamp must convert using pd.to_datetime(unit='ms') | 0 | PASS | All timestamps can be converted. |
| No exact duplicate rows | Exact duplicate rows should not appear in cleaned training data | 0 | PASS | No exact duplicate rows found. |
| source is not missing | Column 'source' must not contain missing values | 0 | PASS | No missing values found in source. |
| destination is not missing | Column 'destination' must not contain missing values | 0 | PASS | No missing values found in destination. |
| cab_type is not missing | Column 'cab_type' must not contain missing values | 0 | PASS | No missing values found in cab_type. |
| name is not missing | Column 'name' must not contain missing values | 0 | PASS | No missing values found in name. |

## 2. CT Checklist Table

| Check Name | Metric / Rule | Current Value | Threshold | Status | Recommendation |
| --- | --- | --- | --- | --- | --- |
| MAE threshold check | MAE <= 2.00 | 1.4254 | 2.00 | PASS | Keep monitoring MAE on new training runs. |
| RMSE threshold check | RMSE <= 3.50 | 2.6181 | 3.50 | PASS | Review large prediction errors if RMSE increases. |
| R2 score threshold check | R2 Score >= 0.85 | 0.9214 | 0.85 | PASS | Improve features or model choice if R2 drops. |
| Error by distance group | Highest group MAE should not be extremely higher than overall MAE | 1.8285 | <= 2.1381 | PASS | Review feature quality for groups with high error. |
| Error by cab_type | Highest group MAE should not be extremely higher than overall MAE | 1.6723 | <= 2.1381 | PASS | Review feature quality for groups with high error. |
| Error by service name | Highest group MAE should not be extremely higher than overall MAE | 2.9136 | <= 2.1381 | WARNING | Review feature quality for groups with high error. |
| Prediction error distribution review | Residual distribution should be reviewed | Reviewed in notebook | No extreme unexplained pattern | PASS | Continue plotting residuals after each retraining. |
| Robustness note for small distance variation | Very short and long trips should be reviewed separately | Reviewed by distance group | Group MAE not extremely high | PASS | Keep distance-group review in the CT checklist. |

## 3. How CI and CT Support the MLOps Pipeline

CI checks help ensure that the data and preprocessing rules are safe before training starts. These checks reduce the risk of training on missing targets, invalid distances, invalid prices, missing categorical values, invalid timestamps, or duplicate records.

CT checks help monitor whether the trained model is still accurate and stable. These checks use overall metrics and group-level error analysis so the model can be reviewed before it is accepted as a new baseline.

## 4. Notes for the Next Step

CD and deployment scenario will be handled in the next step. This notebook only prepares evaluation, error analysis, and CI/CT checklist items.
