# Vulnerability Scanner & Code Safety Dashboard

A web-based security scanning application for analyzing Python code and reviewing detected vulnerabilities alongside CICIDS dataset-based security data.

The project combines rule-based static analysis with a dashboard workflow for reviewing security findings. It includes a FastAPI service, an optional Flask worker, PostgreSQL storage, and a Streamlit dashboard.

## Overview

The scanner checks uploaded Python files for common security issues such as:

- Unsafe functions including `eval()` and `exec()`
- SQL injection patterns
- Hardcoded secrets
- Insecure deserialization
- Unvalidated user input
- Other OWASP-inspired rule violations

The application also works with the CICIDS dataset for security analysis and testing. CICIDS data can be used to support traffic-based security experiments, attack-category analysis, visualization, and validation of the broader security workflow.

## Features

- Python static vulnerability scanning
- File-type validation for uploaded `.py` files
- Rule-based security checks
- CICIDS dataset support
- PostgreSQL scan history
- Streamlit dashboard
- Plotly-based visualization
- JSON and PDF reporting
- Unit and API tests
- Docker-based sandbox components

## Architecture

```text
Streamlit Dashboard
        |
        v
FastAPI Service
        |
        v
Scanner Service
        |
        +--------------------+
        |                    |
        v                    v
Rule-Based Scanners     Flask Worker
        |                    |
        +---------+----------+
                  |
                  v
             PostgreSQL
                  |
                  v
          Reports / Dashboard
```

The Flask worker is an optional execution layer. Core scanning logic is handled through the scanner service and security rule modules.

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── docker-compose.yml
├── .env
├── .gitignore
│
├── backend/
│   ├── fastapi_app/
│   │   ├── main.py
│   │   ├── routers/
│   │   ├── services/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── config/
│   │
│   ├── flask_worker/
│   │   ├── worker.py
│   │   ├── sandbox_executor.py
│   │   └── rule_engine.py
│   │
│   └── scanners/
│       ├── unsafe_function_detector.py
│       ├── injection_detector.py
│       ├── validation_checker.py
│       └── owasp_rules.py
│
├── dashboard/
│   ├── app.py
│   ├── pages/
│   └── utils/
│
├── database/
│   ├── schema.sql
│   └── seed_data.sql
│
├── sandbox/
│   ├── Dockerfile
│   ├── sandbox_runner.py
│   └── resource_limits.py
│
├── logging/
│   ├── audit_logger.py
│   └── security_logs.py
│
├── reports/
│   ├── pdf_report.py
│   └── json_report.py
│
├── tests/
│   ├── test_scanner.py
│   ├── test_api.py
│   └── test_rules.py
│
└── docs/
    ├── architecture.md
    ├── threat_model.md
    └── usage.md
```

## CICIDS Dataset

This project uses CICIDS data as part of its cybersecurity analysis workflow.

Depending on the experiment, CICIDS records can be used to:

- Analyze benign and malicious network traffic
- Compare attack categories
- Test detection and classification workflows
- Generate dashboard summaries and visualizations
- Evaluate security-processing components against labeled network traffic

Place the CICIDS dataset in the location expected by the application or update the configured dataset path.

A recommended local structure is:

```text
data/
└── cicids/
    ├── <dataset-file-1>.csv
    ├── <dataset-file-2>.csv
    └── ...
```

Do not commit large CICIDS dataset files to the repository unless the repository is specifically configured to store them.

## Scanner Components

### FastAPI Service

`backend/fastapi_app/main.py` is the FastAPI entry point.

The API routes include components for:

- File scanning
- Scan reports
- Authentication placeholders
- Scanner service integration

### Scanner Service

`backend/fastapi_app/services/scanner_service.py` coordinates the scanning workflow and calls the individual rule modules.

### File Validation

`file_validator.py` checks uploaded files before they are sent through the scanner.

The current workflow is intended for Python source files.

### Rule-Based Scanners

The scanner modules include checks for:

```text
eval()
exec()
pickle.loads()
SQL query construction
unvalidated input
other OWASP-inspired patterns
```

These rules are static checks. They identify patterns that may require security review; they do not prove that a vulnerability is exploitable.

## Flask Worker

The optional Flask worker runs separately from the FastAPI service:

```text
backend/flask_worker/worker.py
```

It can be used as an additional processing layer for scanner tasks and sandbox-related functionality.

## Dashboard

The Streamlit dashboard is located in:

```text
dashboard/
```

The dashboard provides:

- Scan submission
- Vulnerability summaries
- Detailed findings
- Severity visualization
- CICIDS-related security visualizations where configured
- Remediation information

## Database

PostgreSQL is used for scan-history and application data.

Database initialization files are stored under:

```text
database/
```

Environment-specific database credentials should be placed in `.env` and should not be committed to source control.

## Setup

Clone the repository:

```bash
git clone <repo-url>
cd vuln-scanner-dashboard
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on macOS or Linux:

```bash
source venv/bin/activate
```

On Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file if one is not already present.

Use the configuration values required by the application, such as database connection information and dataset paths.

Example:

```env
DATABASE_URL=<database-connection-string>
CICIDS_DATA_PATH=/absolute/path/to/data/cicids
```

Use the variable names expected by the project configuration files if they differ from this example.

## Run the Application

### Start FastAPI

```bash
uvicorn backend.fastapi_app.main:app --reload
```

### Start the Flask Worker

Open another terminal, activate the environment, and run:

```bash
python backend/flask_worker/worker.py
```

### Start the Streamlit Dashboard

Open another terminal, activate the environment, and run:

```bash
streamlit run dashboard/app.py
```

Then open:

```text
http://localhost:8501
```

## Running Tests

Run the test suite from the repository root:

```bash
pytest
```

For verbose output:

```bash
pytest -v
```

The tests cover scanner behavior, API routes, and security rules.

## Reports

The reporting modules support structured scan output.

Available report components include:

```text
reports/pdf_report.py
reports/json_report.py
```

Reports can include detected issue type, severity, and remediation guidance.

## Security Notes

Uploaded files should be treated as untrusted input.

The project includes validation and sandbox-related components, but local development configurations should not be treated as production-grade isolation without additional hardening.

Recommended production controls include:

- Strict upload limits
- File-content validation
- Authentication and authorization
- Restricted execution privileges
- Container isolation
- CPU and memory limits
- Centralized audit logging
- Secret management
- Database access controls

## Development Notes

This repository is intended for cybersecurity and software-security experimentation. The CICIDS dataset provides network-security data, while the scanner components evaluate source-code patterns. These are separate analysis inputs within the same security application and should not be interpreted as equivalent detection methods.
