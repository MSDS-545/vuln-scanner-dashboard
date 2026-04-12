def detect_owasp(code):

    issues = []

    if "pickle.loads" in code:

        issues.append({
            "type": "insecure deserialization",
            "severity": "HIGH"
        })

    return issues