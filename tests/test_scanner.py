from backend.scanners.unsafe_function_detector import detect_unsafe_functions

def test_eval():

    result = detect_unsafe_functions("eval(input())")

    assert result