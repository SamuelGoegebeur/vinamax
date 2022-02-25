import pandas as pd

def get_all_data(file,delimiter='\s+',skiprows=0,printtf=False):
    data = pd.read_csv(file,delimiter=delimiter,skiprows=skiprows)
    df = pd.DataFrame(data)
    if printtf:
        print(df)
    return df