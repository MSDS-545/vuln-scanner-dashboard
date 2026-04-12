from backend.scanners.owasp_rules import detect_owasp


def run_rules(code):

    return detect_owasp(code)