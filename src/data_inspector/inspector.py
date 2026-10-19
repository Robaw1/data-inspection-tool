import pandas as pd
import argparse


def inspect_data(file_path: str) -> dict[str, int]:
    # Load the CSV dataset
    df = pd.read_csv(file_path)

    # Calculate core data quality metrics
    report = {
        "total_rows": int(len(df)),
        "total_columns": int(len(df.columns)),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.astype(str).to_dict(),
        "constant_columns": [col for col in df.columns if df[col].nunique() <= 1]

    }
    return report


def generate_markdown_report(report):
    with open("report.md", "w") as file:
        file.write("Data Quality Report\n\n")
        file.write(f"**Total Rows:** {report['total_rows']} \n")
        file.write(f"**Total Columns:** {report['total_columns']} \n")
        file.write(f"**Duplicate Rows:** {report['duplicate_rows']} \n\n")

        # Step 4: Loop through missing values
        file.write("## Missing Values\n")
        for col, count in report['missing_values'].items():
            file.write(f"- **{col}**: {count}\n")

        file.write("\n")  # Blank line for spacing

        # Step 5: Loop through data types
        file.write("## Data Types\n")
        for col, dtype in report['data_types'].items():
            file.write(f"- **{col}**: {dtype}\n")
    print("Report file created successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Inspect CSV data quality.")
    parser.add_argument("file_path", help="path to the target CSV file")
    args = parser.parse_args()
    results = inspect_data(args.file_path)-
    generate_markdown_report(results)