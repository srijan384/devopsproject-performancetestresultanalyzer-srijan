import pandas as pd
import os

def test_load_performance_data():
    
    file_path = "performance-data/sample_data.csv"
    
    assert os.path.exists(file_path)

    df = pd.read_csv(file_path)

    assert not df.empty