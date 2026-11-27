import pandas as pd


def load_ticket_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {len(df)} tickets.")
        return df

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None


def clean_ticket_data(df):
    if df is None or df.empty:
        raise ValueError("Ticket dataset is empty.")

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    if "ticket_id" in df.columns:
        df = df.drop_duplicates(subset="ticket_id")

    for column in df.select_dtypes(include=["object", "str"]).columns:
        df[column] = df[column].str.strip()

    date_columns = [
        "created_at",
        "first_response_at",
        "resolved_at",
        "closed_at"
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    print(f"Cleaning completed. Remaining tickets: {len(df)}")

    return df


if __name__ == "__main__":
    data = load_ticket_data("data/raw_tickets.csv")

    cleaned_data = clean_ticket_data(data)

    cleaned_data.to_csv(
        "data/cleaned_tickets.csv",
        index=False
    )

    print("Cleaned dataset saved successfully.")