from flask import Flask, request, jsonify
from app.dag_parser import validate_dag
from app.tasks import execute_task

app = Flask(__name__)

@app.route("/")
def home():
    return "API Running"

@app.route("/submit_dag", methods=["POST"])
def submit_dag():
    data = request.json
    tasks = data["tasks"]

    if not validate_dag(tasks):
        return jsonify({"error": "Cycle detected"}), 400

    return jsonify({"message": "DAG stored"})

@app.route("/trigger_dag/<dag_id>", methods=["POST"])
def trigger_dag(dag_id):
    execute_task.delay("A")
    execute_task.delay("B")
    execute_task.delay("C")
    return jsonify({"message": "DAG triggered"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)