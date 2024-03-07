from flask import Flask, request, jsonify
from google.cloud import bigquery

app = Flask(__name__)

# BigQuery client initialization
client = bigquery.Client()

# Endpoint to receive and save data
@app.route('/persona', methods=['POST'])
def save_persona():
    data = request.json
    table_id = "your-project-id.your-dataset.persona_table"

    # Ensure data contains all required fields
    if not all(key in data for key in ('doc_identidad', 'nombre', 'apellido')):
        return jsonify({"error": "Missing data fields"}), 400

    # Construct a BigQuery row
    rows_to_insert = [data]

    # Insert data into BigQuery
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if not errors:
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False, "errors": errors}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
