from flask import Flask, Response
import json
import os

app = Flask(__name__)

# Define the JSON file path inside the Docker container
JSON_PATH = "/data/data.json"

# Ensure JSON file exists before starting
if not os.path.exists(JSON_PATH):
    print(f"âŒ Error: JSON file '{JSON_PATH}' not found. Make sure it's mounted correctly.")
    exit(1)

def parse_scoutsuite_json():
    try:
        with open(JSON_PATH, "r") as file:
            data = json.load(file)

        # Extract service summary from last run
        services_summary = data.get("last_run", {}).get("summary", {})

        metrics = []
        for service, details in services_summary.items():
            checked_items = details.get("checked_items", 0)
            flagged_items = details.get("flagged_items", 0)
            max_level = details.get("max_level", "warning")

            metrics.append(f'scoutsuite_checked_items{{service="{service}"}} {checked_items}')
            metrics.append(f'scoutsuite_flagged_items{{service="{service}"}} {flagged_items}')
            metrics.append(f'scoutsuite_risk_level{{service="{service}",level="{max_level}"}} 1')

        return "\n".join(metrics) if metrics else "scoutsuite_checked_items{} 0"
    
    except json.JSONDecodeError as e:
        print(f"âŒ JSON Parsing Error: {e}")
        return "scoutsuite_checked_items{} 0"

@app.route("/metrics")
def metrics():
    metric_data = parse_scoutsuite_json()
    return Response(metric_data, mimetype="text/plain")

if __name__ == "__main__":
    print("âœ… JSON Exporter is running on http://0.0.0.0:8000/metrics")
    app.run(host="0.0.0.0", port=8000, debug=True)
