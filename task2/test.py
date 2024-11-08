from interpreter import Interpreter, Lexer, Parser


def run_tests():
    test_cases = [
        ("2 + 3", 5),
        ("2 - 3", -1),
        ("2 * 3", 6),
        ("6 / 3", 2),
        ("7 + 3 * 2", 13),
        ("(2 + 3) * 4", 20),
        ("7 + (3 - 1) * 5", 17),
        ("10 - (2 + 3) * 2", 0),
        ("(10 - 3) * (2 + 2)", 28),
        ("((2 + 3) * 2) + 1", 11)
    ]

    for expression, expected in test_cases:
        lexer = Lexer(expression)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        assert result == expected, f"Test failed for '{
            expression}': expected {expected}, got {result}"
        print(f"Test passed for '{expression}': {result}")


if __name__ == "__main__":
    run_tests()
