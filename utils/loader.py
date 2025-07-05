import pandas as pd
from io import BytesIO

def load_forecast_from_file(contents: bytes, filename: str) -> pd.DataFrame:
    if filename.endswith(".csv"):
        return pd.read_csv(BytesIO(contents))
    else:
        return pd.read_excel(BytesIO(contents))
