import matplotlib.pyplot as plt
import pandas as pd
import os

def generate_histogram(df: pd.DataFrame, column: str, output_path: str):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.figure(figsize=(8, 5))
    df[column].dropna().hist(bins=10, color='#4CAF50', edgecolor='black')
    
    plt.title(f'Distribution of {column.capitalize()}')
    plt.xlabel(column.capitalize())
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()