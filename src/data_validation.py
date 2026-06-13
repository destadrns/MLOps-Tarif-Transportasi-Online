import pandas as pd


REQUIRED_COLUMNS = [
    "price",
    "distance",
    "cab_type",
    "source",
    "destination",
    "name",
    "time_stamp",
]

CATEGORICAL_COLUMNS = ["source", "destination", "cab_type", "name"]


def _result(check_name, rule, failed_rows, status, recommendation):
    return {
        "Check Name": check_name,
        "Rule": rule,
        "Failed Rows": int(failed_rows),
        "Status": status,
        "Recommendation": recommendation,
    }


def validate_required_columns(df, required_columns):
    missing_columns = [column for column in required_columns if column not in df.columns]
    failed_rows = len(df) if missing_columns else 0
    status = "FAIL" if missing_columns else "PASS"
    recommendation = (
        f"Add missing columns before training: {missing_columns}."
        if missing_columns
        else "All required columns are available."
    )
    return _result(
        "Required columns exist",
        f"Required columns: {', '.join(required_columns)}",
        failed_rows,
        status,
        recommendation,
    )


def validate_no_missing_target(df, target_column="price"):
    if target_column not in df.columns:
        return _result(
            "Target price is not missing",
            f"Column '{target_column}' must exist and must not contain missing values",
            len(df),
            "FAIL",
            "Add the target column before supervised training.",
        )

    failed_rows = df[target_column].isna().sum()
    status = "FAIL" if failed_rows > 0 else "PASS"
    recommendation = (
        "Remove rows with missing target before training."
        if failed_rows > 0
        else "No missing target values found."
    )
    return _result(
        "Target price is not missing",
        "Target column 'price' must not be missing",
        failed_rows,
        status,
        recommendation,
    )


def validate_positive_distance(df):
    if "distance" not in df.columns:
        return _result(
            "distance > 0",
            "Column 'distance' must exist and must be greater than 0",
            len(df),
            "FAIL",
            "Add or fix the distance column before preprocessing.",
        )

    failed_rows = (df["distance"] <= 0).sum()
    status = "FAIL" if failed_rows > 0 else "PASS"
    recommendation = (
        "Remove or investigate rows with invalid distance."
        if failed_rows > 0
        else "All distance values are positive."
    )
    return _result("distance > 0", "distance must be greater than 0", failed_rows, status, recommendation)


def validate_positive_price(df):
    if "price" not in df.columns:
        return _result(
            "price > 0",
            "Column 'price' must exist and must be greater than 0",
            len(df),
            "FAIL",
            "Add or fix the price column before training.",
        )

    failed_rows = (df["price"] <= 0).sum()
    status = "FAIL" if failed_rows > 0 else "PASS"
    recommendation = (
        "Remove or investigate rows with invalid price."
        if failed_rows > 0
        else "All available price values are positive."
    )
    return _result("price > 0", "price must be greater than 0", failed_rows, status, recommendation)


def validate_no_missing_categorical_columns(df, categorical_columns):
    results = []
    for column in categorical_columns:
        if column not in df.columns:
            results.append(
                _result(
                    f"{column} is not missing",
                    f"Column '{column}' must exist and must not contain missing values",
                    len(df),
                    "FAIL",
                    f"Add or fix the {column} column before preprocessing.",
                )
            )
            continue

        failed_rows = df[column].isna().sum()
        status = "FAIL" if failed_rows > 0 else "PASS"
        recommendation = (
            f"Handle missing values in {column} before encoding."
            if failed_rows > 0
            else f"No missing values found in {column}."
        )
        results.append(
            _result(
                f"{column} is not missing",
                f"Column '{column}' must not contain missing values",
                failed_rows,
                status,
                recommendation,
            )
        )
    return results


def validate_timestamp_convertible(df, timestamp_column="time_stamp"):
    if timestamp_column not in df.columns:
        return _result(
            "time_stamp can be converted to datetime",
            f"Column '{timestamp_column}' must exist and convert to datetime",
            len(df),
            "FAIL",
            "Add or fix the timestamp column before creating time features.",
        )

    converted = pd.to_datetime(df[timestamp_column], unit="ms", errors="coerce")
    failed_rows = converted.isna().sum()
    status = "FAIL" if failed_rows > 0 else "PASS"
    recommendation = (
        "Drop or fix rows with invalid timestamps before feature engineering."
        if failed_rows > 0
        else "All timestamps can be converted."
    )
    return _result(
        "time_stamp can be converted to datetime",
        "time_stamp must convert using pd.to_datetime(unit='ms')",
        failed_rows,
        status,
        recommendation,
    )


def validate_no_exact_duplicate_rows(df):
    failed_rows = df.duplicated().sum()
    status = "WARNING" if failed_rows > 0 else "PASS"
    recommendation = (
        "Review duplicates and remove them if they are repeated records."
        if failed_rows > 0
        else "No exact duplicate rows found."
    )
    return _result(
        "No exact duplicate rows",
        "Exact duplicate rows should not appear in cleaned training data",
        failed_rows,
        status,
        recommendation,
    )


def run_all_validations(df):
    results = [
        validate_required_columns(df, REQUIRED_COLUMNS),
        validate_no_missing_target(df, target_column="price"),
        validate_positive_distance(df),
        validate_positive_price(df),
        validate_timestamp_convertible(df, timestamp_column="time_stamp"),
        validate_no_exact_duplicate_rows(df),
    ]
    results.extend(validate_no_missing_categorical_columns(df, CATEGORICAL_COLUMNS))

    column_order = ["Check Name", "Rule", "Failed Rows", "Status", "Recommendation"]
    return pd.DataFrame(results, columns=column_order)
