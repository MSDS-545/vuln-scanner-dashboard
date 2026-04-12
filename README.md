# Vulnerability Scanner & Code Safety Dashboard

A secure code scanning platform that detects common vulnerabilities in Python code using OWASP-inspired rules.

The system analyzes uploaded Python code using rule-based static analysis, detects security vulnerabilities aligned with OWASP risks, and presents results through a web dashboard with actionable remediation insights.

This project simulates real-world DevSecOps tools, similar to:

Static analyzers (Bandit)
Code scanners (SonarQube)
Security platforms (Snyk)

It demonstrates:

Secure software development
Automated vulnerability detection
Cybersecurity + software engineering integration

How Scanning Works

1. User uploads a Python file
2. File is validated (.py only)
3. Code is scanned using rule-based detectors:
   - Unsafe functions (eval, exec)
   - SQL injection patterns
   - Hardcoded secrets
   - Insecure deserialization
4. Results are returned with:
   - vulnerability type
   - severity
   - remediation suggestion
5. Dashboard visualizes results



Features:
- Static vulnerability detection
- Secure file validation
- Sandboxed scanning
- PostgreSQL scan history
- Streamlit dashboard visualization
- Automated vulnerability reporting

Architecture:
FastAPI API → Flask scanning worker → PostgreSQL → Streamlit Dashboard

User Upload (Streamlit)
        ↓
FastAPI Backend (API)
        ↓
Scanner Service
        ↓
Flask Worker (optional processing layer)
        ↓
Rule-Based Scanners
        ↓
Results → Dashboard + Reports

Root Files


README.md
Explains the project
Contains setup + run instructions

requirements.txt
Lists all Python dependencies:
FastAPI → backend API
Flask → worker
Streamlit → dashboard
SQLAlchemy → database
Plotly/Pandas → visualization


docker-compose.yml
Defines multi-service environment
Spins up:
API
Worker
Dashboard
PostgreSQL


.env
Stores environment variables (DB credentials)

.gitignore
Prevents committing:
venv
logs
uploads


Backend (Core Logic)

backend/fastapi_app/
main.py
Entry point for FastAPI
Registers all API routes
Starts the backend service

routers/ (API Endpoints)
scan_router.py
Handles file upload (/scan)
Calls scanner service
Returns vulnerabilities

auth_router.py
Handles authentication (placeholder)
Returns token (demo)

report_router.py
Provides scan reports (/report)
Connects to reporting service


services/ (Business Logic)

scanner_service.py
Core orchestrator
Calls all scanner modules:
unsafe functions
injection detection
validation checks
OWASP rules

file_validator.py
Ensures only .py files are uploaded
Prevents malicious file types

report_service.py
Generates scan summaries
Returns structured output (JSON)

models/ (Database Models)
scan_model.py
Defines scan table structure
Stores vulnerability results

user_model.py
Defines user table
Used for authentication

schemas/ (Data Validation)
scan_schema.py
Defines API response format for scans
auth_schema.py
Defines login request structure

config/
database.py
Sets up database connection (SQLAlchemy)

settings.py
Loads environment variables from .env


Flask Worker (Execution Layer)
backend/flask_worker/
worker.py
Runs Flask server (port 5001)
Acts as background scanner service
Can simulate async processing

sandbox_executor.py
Placeholder for secure execution
Intended to run code safely in isolation
rule_engine.py
Calls scanner rules (OWASP detection)
Connects worker to scanning logic

Scanners (Security Detection Engine)

backend/scanners/
unsafe_function_detector.py
Detects:
eval()
exec()
Flags unsafe execution

injection_detector.py
Detects:
SQL injection patterns
Looks for string concatenation in queries
validation_checker.py
Detects:
unvalidated user input (input())
owasp_rules.py
Detects OWASP-style issues:
insecure deserialization (pickle.loads)
unsafe operations
These files collectively form the static analysis engine

Dashboard (Frontend UI)
dashboard/
app.py
Main Streamlit app
Uploads file
Calls API
Stores results in session

pages/
overview.py
Displays:
total vulnerabilities
severity distribution

scan_results.py
Shows detailed table of vulnerabilities
vulnerability_map.py
Visualizes vulnerabilities (charts)
remediation_guide.py
Provides fixes and recommendations

utils/
api_client.py
Handles API calls from dashboard
visualization.py
Creates charts (Plotly)

Database
database/
schema.sql
Defines database tables
seed_data.sql
Inserts sample data

Sandbox (Security Layer)
sandbox/
Dockerfile
Creates isolated container for safe execution
sandbox_runner.py
Runs code inside sandbox
resource_limits.py
Defines CPU/memory restrictions
Prevents malicious code execution

Logging
logging/
audit_logger.py
Logs system events (scans, uploads)
security_logs.py
Logs detected vulnerabilities

Reports
reports/
pdf_report.py
Generates PDF vulnerability reports
json_report.py
Generates JSON reports

Tests
tests/
test_scanner.py
Tests detection logic
test_api.py
Tests API endpoints
test_rules.py
Tests rule engine

Docs
docs/
architecture.md
Describes system architecture
threat_model.md
Lists potential security threats
usage.md
Explains how to use the system


steps: 

Run to get repo:
git clone <repo-url>
cd vuln-scanner-dashboard


Run code in terminal: 
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

uvicorn backend.fastapi_app.main:app --reload

In another terminal run: 
source venv/bin/activate   # Windows: venv\Scripts\activate
Worker
python backend/flask_worker/worker.py


In another terminal run: 

source venv/bin/activate   # Windows: venv\Scripts\activate
streamlit run dashboard/app.py

Open:
http://localhost:8501





