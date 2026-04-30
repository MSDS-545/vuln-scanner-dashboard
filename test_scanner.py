import unittest

# Copy of your scanning logic to test against
def scan_code(source_code):
    import re
    issues = []
    lines = source_code.splitlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if re.search(r'\beval\s*\(', stripped):
            issues.append({"line": i, "type": "Unsafe function", "severity": "HIGH"})
        if re.search(r'\bexec\s*\(', stripped):
            issues.append({"line": i, "type": "Unsafe function", "severity": "HIGH"})
        if re.search(r'(password|api_key|secret)\s*=\s*["\'].+["\']', stripped, re.IGNORECASE):
            issues.append({"line": i, "type": "Hardcoded secret", "severity": "CRITICAL"})
        if re.search(r'\binput\s*\(', stripped):
            issues.append({"line": i, "type": "Unvalidated input", "severity": "MEDIUM"})
        if re.search(r'pickle\.loads?\s*\(', stripped):
            issues.append({"line": i, "type": "Insecure deserialization", "severity": "HIGH"})
    return issues


class TestScanner(unittest.TestCase):

    def test_detects_eval(self):
        code = "eval('print(hello)')"
        results = scan_code(code)
        types = [r["type"] for r in results]
        self.assertIn("Unsafe function", types)

    def test_detects_exec(self):
        code = "exec('x = 1')"
        results = scan_code(code)
        types = [r["type"] for r in results]
        self.assertIn("Unsafe function", types)

    def test_detects_hardcoded_secret(self):
        code = "password = 'supersecret123'"
        results = scan_code(code)
        types = [r["type"] for r in results]
        self.assertIn("Hardcoded secret", types)

    def test_detects_unvalidated_input(self):
        code = "user_input = input('Enter: ')"
        results = scan_code(code)
        types = [r["type"] for r in results]
        self.assertIn("Unvalidated input", types)

    def test_detects_pickle(self):
        code = "pickle.loads(data)"
        results = scan_code(code)
        types = [r["type"] for r in results]
        self.assertIn("Insecure deserialization", types)

    def test_clean_code_returns_no_issues(self):
        code = "x = 1 + 1\nprint(x)"
        results = scan_code(code)
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()