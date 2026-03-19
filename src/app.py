from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
import os

# Import analyzer logic
from analyzer import analyze_file

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, '..'))

# Flask app setup
app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, 'templates'),
    static_folder=os.path.join(project_root, 'static'),
    static_url_path='/static'
)

print("STATIC PATH:", app.static_folder)

# Prometheus Monitoring
metrics = PrometheusMetrics(app, path="/metrics")
metrics.info('app_info', 'Application info', version='1.0')

@app.route('/metrics')
def metrics_endpoint():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# Upload folder setup
UPLOAD_FOLDER = os.path.join(base_dir, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']

    if file.filename == '':
        return "No file selected"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Call analyzer
    result = analyze_file(filepath, os.path.join(project_root, "static"))

    if "error" in result:
        return result["error"]

    return render_template(
        "result.html",
        avg=result["avg"],
        max=result["max"],
        graph=result["graph"]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)