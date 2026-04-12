def detect_injection(code):

    issues = []

    if "SELECT * FROM" in code and "+" in code:

        issues.append({
            "type": "SQL injection risk",
            "severity": "CRITICAL"
        })

    return issues