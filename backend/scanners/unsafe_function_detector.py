def detect_unsafe_functions(code):

    issues = []

    if "eval(" in code:

        issues.append({
            "type": "unsafe function",
            "severity": "HIGH"
        })

    if "exec(" in code:

        issues.append({
            "type": "exec usage",
            "severity": "HIGH"
        })

    return issues