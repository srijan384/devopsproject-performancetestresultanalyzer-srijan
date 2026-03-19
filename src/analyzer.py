import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pandas.errors import EmptyDataError
import os


def analyze_file(filepath, static_folder):
    try:
        df = pd.read_csv(filepath)
    except EmptyDataError:
        return {"error": "Uploaded CSV file is empty"}

    if 'response_time' not in df.columns:
        return {"error": "CSV must contain a 'response_time' column"}

    avg_response = df['response_time'].mean()
    max_response = df['response_time'].max()

    # Generate graph
    plt.figure()
    df['response_time'].plot(kind='line')
    plt.title("Response Time Graph")
    plt.xlabel("Request Number")
    plt.ylabel("Response Time")

    graph_filename = "graph.png"
    graph_path = os.path.join(static_folder, graph_filename)

    plt.savefig(graph_path)
    plt.close()

    return {
        "avg": avg_response,
        "max": max_response,
        "graph": graph_filename
    }