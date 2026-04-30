def detect_unsafe_functions(code):
    issues = []

    if "eval(" in code:
        issues.append({
            "type": "Unsafe function: eval()",
            "severity": "HIGH",
            "remediation": "Never use eval() on user input. Use ast.literal_eval() instead."
        })

    if "exec(" in code:
        issues.append({
            "type": "Unsafe function: exec()",
            "severity": "HIGH",
            "remediation": "Avoid exec(). It allows arbitrary code execution."
        })

    if "input(" in code:
        issues.append({
            "type": "Unvalidated user input: input()",
            "severity": "MEDIUM",
            "remediation": "Always validate and sanitize user input before using it."
        })

    if 'password = "' in code or "password = '" in code:
        issues.append({
            "type": "Hardcoded secret: password",
            "severity": "CRITICAL",
            "remediation": "Never hardcode passwords. Use environment variables instead."
        })

    if 'api_key = "' in code or "api_key = '" in code:
        issues.append({
            "type": "Hardcoded secret: API key",
            "severity": "CRITICAL",
            "remediation": "Never hardcode API keys. Store them in a .env file."
        })

    if 'secret = "' in code or "secret = '" in code:
        issues.append({
            "type": "Hardcoded secret: secret key",
            "severity": "CRITICAL",
            "remediation": "Never hardcode secret keys. Use environment variables."
        })

    return issues
