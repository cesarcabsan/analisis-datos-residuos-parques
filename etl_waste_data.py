import pandas as pd
import numpy as np

def extract_data(file_route):
    df = pd.read_csv(file_route, header=1)
    print("Extracting data from csv.")
    return df

def clean_data(df):
    remove_cols = [col for col in df.columns if 'Unnamed' in col]
    df = df.drop(columns=remove_cols)

    df['Tipo de residuo'] = df['Tipo de residuo'].str.lower()
    df['Tipo de residuo'] = df['Tipo de residuo'].str.replace('á', 'a').str.replace('é', 'e').str.replace('í', 'i').str.replace('ó', 'o').str.replace('ú', 'u')
    df['Tipo de residuo'] = df['Tipo de residuo'].str.title()

    print("Cleaning up data")
    return df

def transform_data(df):
    df['Cantidad estimada (kg)'] = pd.to_numeric(df['Cantidad estimada (kg)'], errors='coerce').astype(np.float64)
    
    df['Fecha de registro'] = pd.to_datetime(df['Fecha de registro'], format='%d-%m-%Y', errors='coerce')
    
    df['Mes'] = df['Fecha de registro'].dt.month
    df['Año'] = df['Fecha de registro'].dt.year
    
    print("Transforming data and generate temporal metrics")
    return df

def load_data(df, exit_route):
    df.to_csv(exit_route, index=False, encoding="utf-8")
    print(f"Loading data.")

def exec_etl_pipeline():
    file_input = 'DatosResiduos.csv'
    file_output = 'DatosResiduos_Procesados.csv'
    
    print("--- Iniciating ETL Pipeline ---")
    raw_df = extract_data(file_input)
    clean_df = clean_data(raw_df)
    transformed_df = transform_data(clean_df)
    load_data(transformed_df, file_output)
    print("--- ETL Pipeline finished ---")
    
    return transformed_df

if __name__ == "__main__":
    df_final = exec_etl_pipeline()
    print("\nProccesed data preview:")
    print(df_final.head())
    print("\nColumn information (Data types):")
    print(df_final.dtypes)