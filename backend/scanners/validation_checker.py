def detect_validation_issues(code):

    issues = []

    if "input(" in code:

        issues.append({
            "type": "unvalidated input",
            "severity": "LOW"
        })

    return issues