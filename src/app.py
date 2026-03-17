from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')   # Fix for MacOS thread issue
import matplotlib.pyplot as plt
from pandas.errors import EmptyDataError
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():

    # Check if file was uploaded
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']

    # Check if filename is empty
    if file.filename == '':
        return "No file selected"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        df = pd.read_csv(filepath)
    except EmptyDataError:
        return "Error: Uploaded CSV file is empty"

    # Check if required column exists
    if 'response_time' not in df.columns:
        return "Error: CSV must contain a 'response_time' column"

    avg_response = df['response_time'].mean()
    max_response = df['response_time'].max()

    plt.figure()
    df['response_time'].plot(kind='line')
    plt.title("Response Time Graph")
    plt.xlabel("Request Number")
    plt.ylabel("Response Time")

    graph_path = "static/graph.png"
    plt.savefig(graph_path)
    plt.close()

    return render_template(
        "result.html",
        avg=avg_response,
        max=max_response,
        graph=graph_path
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)