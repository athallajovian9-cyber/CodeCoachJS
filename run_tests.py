"""Unit test suite for CodeCoach JS."""
import unittest
from coach import analyze_js

class TestCodeCoachJS(unittest.TestCase):
    def test_clean_code(self):
        code = "const score = 100;\nconsole.log(score);"
        issues = analyze_js(code)
        self.assertEqual(len(issues), 0)

    def test_single_equals_in_if(self):
        code = "if (x = 5) { doSomething(); }"
        issues = analyze_js(code)
        self.assertTrue(any(i.kind == "QUIET BUG" for i in issues))

    def test_while_true_loop(self):
        code = "while (true) { console.log('spam'); }"
        issues = analyze_js(code)
        self.assertTrue(any(i.kind == "LOOP NEVER STOPS!" for i in issues))

    def test_old_var_keyword(self):
        code = "var myName = 'Alex';"
        issues = analyze_js(code)
        self.assertTrue(any(i.kind == "OUTDATED HABIT" for i in issues))

    def test_nan_equality(self):
        code = "if (score === NaN) { score = 0; }"
        issues = analyze_js(code)
        self.assertTrue(any("NaN" in i.title for i in issues))

if __name__ == "__main__":
    unittest.main()
