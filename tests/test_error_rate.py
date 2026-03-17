import pandas as pd

def calculate_error_rate(df):
    
    total = len(df)
    errors = len(df[df["status"] >= 400])
    
    return errors / total

def test_error_rate():

    data = {
        "status": [200, 200, 500, 404]
    }

    df = pd.DataFrame(data)

    error_rate = calculate_error_rate(df)

    assert error_rate == 0.5