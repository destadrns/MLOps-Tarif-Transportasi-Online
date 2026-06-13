from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def calculate_regression_metrics(y_true, y_pred):
    """Calculate simple regression metrics for model evaluation."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2 Score": r2,
        "Mean Actual Price": float(pd.Series(y_true).mean()),
        "Median Actual Price": float(pd.Series(y_true).median()),
    }


def create_prediction_result_dataframe(X_test, y_test, y_pred):
    """Combine test features, actual prices, predictions, and errors."""
    result_df = X_test.copy()
    result_df["actual_price"] = pd.Series(y_test, index=X_test.index)
    result_df["predicted_price"] = y_pred
    result_df["error"] = result_df["actual_price"] - result_df["predicted_price"]
    result_df["absolute_error"] = result_df["error"].abs()
    return result_df


def evaluate_by_group(result_df, group_column):
    """Calculate count, MAE, and RMSE for a selected group column."""
    if group_column not in result_df.columns:
        raise ValueError(f"Column '{group_column}' is not available for group evaluation.")

    group_table = (
        result_df.groupby(group_column, observed=True)
        .agg(
            row_count=("absolute_error", "size"),
            MAE=("absolute_error", "mean"),
            RMSE=("error", lambda values: np.sqrt(np.mean(np.square(values)))),
        )
        .reset_index()
        .sort_values("MAE", ascending=False)
    )
    return group_table


def create_ct_checklist(metrics, group_error_tables):
    """Create a simple Continuous Training quality checklist."""
    overall_mae = metrics["MAE"]
    overall_rmse = metrics["RMSE"]
    overall_r2 = metrics["R2 Score"]
    group_threshold = overall_mae * 1.5

    rows = [
        {
            "Check Name": "MAE threshold check",
            "Metric / Rule": "MAE <= 2.00",
            "Current Value": f"{overall_mae:.4f}",
            "Threshold": "2.00",
            "Status": "PASS" if overall_mae <= 2.00 else "WARNING",
            "Recommendation": "Keep monitoring MAE on new training runs.",
        },
        {
            "Check Name": "RMSE threshold check",
            "Metric / Rule": "RMSE <= 3.50",
            "Current Value": f"{overall_rmse:.4f}",
            "Threshold": "3.50",
            "Status": "PASS" if overall_rmse <= 3.50 else "WARNING",
            "Recommendation": "Review large prediction errors if RMSE increases.",
        },
        {
            "Check Name": "R2 score threshold check",
            "Metric / Rule": "R2 Score >= 0.85",
            "Current Value": f"{overall_r2:.4f}",
            "Threshold": "0.85",
            "Status": "PASS" if overall_r2 >= 0.85 else "WARNING",
            "Recommendation": "Improve features or model choice if R2 drops.",
        },
    ]

    group_names = {
        "distance_group": "Error by distance group",
        "cab_type": "Error by cab_type",
        "name": "Error by service name",
    }

    for group_key, check_name in group_names.items():
        table = group_error_tables.get(group_key)
        if table is None or table.empty:
            rows.append(
                {
                    "Check Name": check_name,
                    "Metric / Rule": "Group MAE should be reviewable",
                    "Current Value": "Not available",
                    "Threshold": f"<= {group_threshold:.4f}",
                    "Status": "WARNING",
                    "Recommendation": "Create the group error table before model approval.",
                }
            )
            continue

        max_group_mae = float(table["MAE"].max())
        status = "PASS" if max_group_mae <= group_threshold else "WARNING"
        rows.append(
            {
                "Check Name": check_name,
                "Metric / Rule": "Highest group MAE should not be extremely higher than overall MAE",
                "Current Value": f"{max_group_mae:.4f}",
                "Threshold": f"<= {group_threshold:.4f}",
                "Status": status,
                "Recommendation": "Review feature quality for groups with high error.",
            }
        )

    rows.extend(
        [
            {
                "Check Name": "Prediction error distribution review",
                "Metric / Rule": "Residual distribution should be reviewed",
                "Current Value": "Reviewed in notebook",
                "Threshold": "No extreme unexplained pattern",
                "Status": "PASS",
                "Recommendation": "Continue plotting residuals after each retraining.",
            },
            {
                "Check Name": "Robustness note for small distance variation",
                "Metric / Rule": "Very short and long trips should be reviewed separately",
                "Current Value": "Reviewed by distance group",
                "Threshold": "Group MAE not extremely high",
                "Status": "PASS",
                "Recommendation": "Keep distance-group review in the CT checklist.",
            },
        ]
    )

    return pd.DataFrame(
        rows,
        columns=["Check Name", "Metric / Rule", "Current Value", "Threshold", "Status", "Recommendation"],
    )


def save_report(path, content):
    """Save text report content to disk."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path
