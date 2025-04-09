# src/utils/data_merge.py

import pandas as pd


def merge_and_sample(mat_path, por_path, output_path, sample_size=100):
    df_mat = pd.read_csv(mat_path, sep=';')
    df_por = pd.read_csv(por_path, sep=';')

    merge_cols = ["school", "sex", "age", "address", "famsize", "Pstatus",
                  "Medu", "Fedu", "Mjob", "Fjob", "reason", "nursery", "internet"]

    df_merged = pd.merge(df_mat, df_por, on=merge_cols,
                         suffixes=('_mat', '_por'))

    df_sample = df_merged.sample(sample_size, random_state=42)
    df_sample.to_csv(output_path, index=False)

    print(f"✅ Muestra guardada en: {output_path}")
    return df_sample
