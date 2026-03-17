import pandas as pd

def test_empty_dataframe():

    df = pd.DataFrame()

    assert df.empty