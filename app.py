from flask import Flask, request, jsonify
from google.cloud import bigquery

app = Flask(__name__)
client = bigquery.Client()

@app.route('/persona', methods=['POST'])
def save_persona():
    data = request.json
    table_id = "project-web-dev-416401.ds_company.tbl_persona"

    errors = client.insert_rows_json(table_id, [data])  # Make sure your data keys match the BigQuery table schema

    if errors == []:
        return jsonify({"success": True}), 200
    return jsonify({"success": False, "errors": errors}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
