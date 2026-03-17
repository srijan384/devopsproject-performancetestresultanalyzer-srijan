import pandas as pd

def calculate_average_response_time(df):
    return df["response_time"].mean()

def test_average_response_time():

    data = {
        "response_time": [100, 200, 300]
    }

    df = pd.DataFrame(data)

    avg = calculate_average_response_time(df)

    assert avg == 200