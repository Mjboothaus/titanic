from functools import cache
import pandas as pd
import pandas_profiling

CSV_URL_EXAMPLE = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"

@cache 
def get_data_pandas_example(datasource=CSV_URL_EXAMPLE, sep=",", header=0):
    try:
        return pd.read_csv(datasource, sep=sep, header=header)
    except Exception as e:
        raise(e)

@cache
def load_data():
    data_url = "https://raw.githubusercontent.com/Mjboothaus/titanic/main/data"
    titanic_train = pd.read_csv(f"{data_url}/train.csv")
    titanic_test= pd.read_csv(f"{data_url}/test.csv")
    return titanic_train, titanic_test


#@cache(hash_funcs={pandas_profiling.report.presentation.core.container.Container: lambda _: None})
def create_data_profile(df):
    return df.profile_report(minimal=True)