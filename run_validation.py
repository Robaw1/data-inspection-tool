import pandas as pd
from src.data_inspector.validator import load_schema, validate_data
# Load the dummy data and schema
df = pd.read_csv("data/dummy.csv")
schema = load_schema("configs/schema.yaml")

# Run validation
errors = validate_data(df, schema)

for error in errors:
    print(error)