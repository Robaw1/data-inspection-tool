Data Quality Inspector
Overview
An engineering-focused data validation tool designed to identify missing values, enforce schema rules, and prevent target leakage before model training.

Core Features

Schema Validation: Enforces strict data rules (e.g., boundaries, types) using PyYAML.

Under-the-Hood Math: Custom pure Python implementations of statistical primitives (mean, median, variance) backed by pytest.

Visual Diagnostics: Generates distribution histograms via matplotlib.

Automated Reporting: Compiles validation errors and plots into a standalone HTML dashboard.

Audit Logging: Configuration-driven logging separates system diagnostics from the final report.

Tech Stack
Python, Pandas, Matplotlib, PyYAML, Pytest, Ruff.