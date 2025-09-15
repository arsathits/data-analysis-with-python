import os
import sys
import pandas as pd
from pathlib import Path

# Add the project's root directory to the Python path
# This allows the script to find the 'config' and other project modules.
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from config import DATA_PATH

def load_data():
    """Loads the raw training data from the specified path."""
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded raw data: {df.shape[0]} rows, {df.shape[1]} columns")
    return df