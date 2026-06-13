# Data Audit Report

## 1. Project Title

**Mini MLOps Pipeline Design for Online Transportation Fare Estimation Based on Trip and Weather Data**

## 2. Dataset Files

- `data/raw/cab_rides.csv`
- `data/raw/weather.csv`

The raw data files were only inspected. They were not modified.

## 3. Dataset Shape

| Dataset | Rows | Columns |
|---|---:|---:|
| `cab_rides.csv` | 693,071 | 10 |
| `weather.csv` | 6,276 | 8 |

## 4. Target Column

The recommended target column is `price`.

## 5. Problem Type

This is a **regression** problem because the model will predict a numerical fare value.

## 6. Main Features

Recommended initial trip features:

- `distance`
- `cab_type`
- `source`
- `destination`
- `name`
- `surge_multiplier`
- `time_stamp`

Weather features can be considered later after careful location and time alignment:

- `temp`
- `clouds`
- `pressure`
- `rain`
- `humidity`
- `wind`

Columns recommended for exclusion from the first model:

- `id`
- `product_id`
- `price` as an input feature, because it is the target

## 7. Data Quality Findings

- `cab_rides.csv` contains 693,071 rows and 10 columns.
- `weather.csv` contains 6,276 rows and 8 columns.
- The target column `price` exists in `cab_rides.csv`.
- There are 637,976 rows with valid `price`.
- There are 55,095 rows with missing `price`, equal to 7.95% of cab ride rows.
- There are 0 rows with `distance <= 0`.
- There are 0 rows with `price <= 0` among non-missing prices.
- There are 0 missing values in `source`, `destination`, `cab_type`, and `name`.
- There are 0 exact duplicate rows in both datasets.
- In `weather.csv`, `rain` has 5,382 missing values, equal to 85.76% of weather rows. This should be reviewed before using weather features.

## 8. Initial Validation Checklist

| Check Name | Rule | Failed Rows | Status | Recommendation |
|---|---|---:|---|---|
| Target column exists | Column `price` must exist in `cab_rides.csv` | 0 | PASS | Use `price` as the supervised learning target. |
| Missing price | `price` should be available for training rows | 55,095 | WARNING | Remove rows with missing target before model training. |
| Distance validity | `distance` must be greater than 0 | 0 | PASS | Keep this rule in the CI validation checklist. |
| Price validity | `price` must be greater than 0 when present | 0 | PASS | Keep this rule in the CI validation checklist. |
| Missing source | `source` should not be missing | 0 | PASS | Keep this rule in the CI validation checklist. |
| Missing destination | `destination` should not be missing | 0 | PASS | Keep this rule in the CI validation checklist. |
| Missing cab_type | `cab_type` should not be missing | 0 | PASS | Keep this rule in the CI validation checklist. |
| Missing name | `name` should not be missing | 0 | PASS | Keep this rule in the CI validation checklist. |
| Duplicate cab rows | Exact duplicate rows should be reviewed | 0 | PASS | Keep duplicate checks before training. |
| Missing weather rain | `rain` should be reviewed before using weather features | 5,382 | WARNING | Check whether missing rain means no rain, then fill with 0 if appropriate. |

## 9. Recommendation for the Next Step

The dataset is suitable for the next step after basic cleaning. The next notebook should focus on preprocessing and baseline model training.

Recommended next actions:

- Remove rows where `price` is missing before supervised training.
- Convert `time_stamp` into readable datetime features.
- Encode categorical columns such as `cab_type`, `source`, `destination`, and `name`.
- Review missing `rain` values before using weather data.
- Plan the weather merge carefully by location and time.
- Build a simple baseline regression model only after the cleaned dataset passes validation checks.

This audit can support later MLOps stages by becoming part of the CI checklist, preparing clean data for CT, and documenting assumptions before any CD scenario.
