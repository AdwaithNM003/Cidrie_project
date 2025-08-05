import os
import pandas as pd
dir = 'sample path'#where is location of excel files
tar=  ['ColA', 'ColB']# Define the columns you want to read specifically

for filename in os.listdir(dir):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        fname = os.path.join(dir, filename)
        try:
            df = pd.read_excel(fname)
            available = [col for col in tar if col in df.columns]#this now contains columns we want
            missing = [col for col in tar if col not in df.columns]#this now contains columns we dont want

            if available:
                avail_df = df[available]
                print(f"{filename} - Successfully read: {available}")
            else:
                print(f"{filename} - Missing all target columns!")

            if missing:
                print(f"{filename} - Missing columns: {missing_cols}")

        except Exception as e:
            print(f"Error reading {filename}: {e}")