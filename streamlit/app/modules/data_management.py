import pandas as pd

def load_data(file_name: str) -> pd.DataFrame:
    return pd.read_csv(file_name)

def save_data(data: pd.DataFrame, file_name: str) -> None:
    data.to_csv(file_name, index=False)

def add_row_to_data(data: pd.DataFrame, row: dict) -> pd.DataFrame:
    return data.append(row, ignore_index=True)

def update_row_in_data(data: pd.DataFrame, row_id: int, updated_row: dict) -> pd.DataFrame:
    data.loc[row_id] = updated_row
    return data

def delete_row_from_data(data: pd.DataFrame, row_id: int) -> pd.DataFrame:
    return data.drop(index=row_id).reset_index(drop=True)