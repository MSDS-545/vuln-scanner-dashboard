import sys
from pathlib import Path

# Add the project root to sys.path before importing backend
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from flask import Flask
from backend.flask_worker.rule_engine import run_rules

app = Flask(__name__)

@app.route("/scan")
def scan():
    code = "example code"
    result = run_rules(code)
    return {"result": result}

if __name__ == "__main__":
    app.run(port=5001)