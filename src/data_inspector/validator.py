import yaml
import pandas as pd

def load_schema(filepath: str) -> dict:
    with open(filepath,'r') as file:
        return yaml.safe_load(file)
def validate_data(df:pd.DataFrame, schema: dict) ->list[str]:
    errors =[]
    for col, rules in schema.get('columns',{}).items():
        if col not in df.columns:
            errors.append(f"Missing required column: {col}")
            continue
        if 'minimum' in rules and df[col].min() < rules['minimum']:
            errors.append(f"column '{col}' violates minimum value of {rules['minimum']}")
        if 'maximum' in rules and df[col].max() > rules['maximum']:
            errors.append(f"Column '{col}' violates maximum value of {rules['maximum']}")
    return errors