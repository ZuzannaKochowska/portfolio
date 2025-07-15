import pandas as pd
import os
import glob

folder_path = './'
file_paths = glob.glob(os.path.join(folder_path, '*_clean.csv'))

#Lista
dfs = []

for path in file_paths:
    file_name = os.path.basename(path)
    df = pd.read_csv(path)
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)

df_all.to_csv('all_companies.csv', index=False)

print("Plik 'all_companies.csv' został zapisany.")
