from flask import Flask, request, jsonify
from langflow import load_flow_from_json, run_flow

app = Flask(__name__)
flow = load_flow_from_json("Auto-loan v1.json")

@app.route("/run", methods= )
def run():
    file = request.files['file']
    result = run_flow(flow, inputs={"file": file})
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
