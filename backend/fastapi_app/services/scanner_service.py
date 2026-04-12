from ...scanners.unsafe_function_detector import detect_unsafe_functions
from ...scanners.injection_detector import detect_injection
from ...scanners.validation_checker import detect_validation_issues
from ...scanners.owasp_rules import detect_owasp

def run_scan(code):

    issues = []

    issues += detect_unsafe_functions(code)
    issues += detect_injection(code)
    issues += detect_validation_issues(code)
    issues += detect_owasp(code)

    return issues