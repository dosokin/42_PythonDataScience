import pandas as pd


def load(path: str) -> pd.DataFrame or None:

    """load and return csv"""

    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(e)
        return None

    print(f"Loading dataset of dimensions {df.shape}")

    return df
