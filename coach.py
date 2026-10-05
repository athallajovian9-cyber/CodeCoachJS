"""CodeCoach JavaScript (JS) - Kid-Friendly AST & Pattern Linter Engine.
Detects common beginner bugs, endless loops, DOM pitfalls, variable scope traps,
and provides approachable hints with clear solutions.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List


@dataclass
class Issue:
    kind: str
    line: int
    title: str
    message: str
    fix_hint: str


def analyze_js(code: str) -> List[Issue]:
    issues: List[Issue] = []
    lines = code.splitlines()

    for idx, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()

        # Skip comment lines
        if line.startswith("//") or line.startswith("/*"):
            continue

        # 1. Assignment inside if condition: if (x = 5)
        if re.search(r'\bif\s*\([^=!<>\n]*=[^=!<>\n]*\)', line):
            if not re.search(r'===|==|<=|>=|!=', line):
                issues.append(Issue(
                    kind="QUIET BUG",
                    line=idx,
                    title="ACCIDENTAL VALUE ASSIGNMENT!",
                    message="You used a single '=' inside an 'if' statement! Single '=' sets a value instead of checking it.",
                    fix_hint="Use '===' to test if two values are equal: e.g. if (score === 10)"
                ))

        # 2. Loose equality check: == instead of ===
        if re.search(r'[^=!<>]={2}[^=]', line) and "===" not in line:
            issues.append(Issue(
                kind="TRICKY PITFALL",
                line=idx,
                title="LOOSE EQUALITY CAN TRICK YOU!",
                message="Double '==' converts types silently (like '5' == 5 is true).",
                fix_hint="Use strict triple '===' so types must match exactly!"
            ))

        # 3. Endless loop pattern: while(true) without break
        if re.search(r'\bwhile\s*\(\s*true\s*\)', line):
            issues.append(Issue(
                kind="LOOP NEVER STOPS!",
                line=idx,
                title="RUNAWAY WHILE LOOP!",
                message="This loop condition is always true and may freeze the web browser!",
                fix_hint="Add an end condition or 'break;' inside the loop to let it stop."
            ))

        # 4. Old var keyword: var x = 10
        if re.search(r'\bvar\s+[a-zA-Z_$][a-zA-Z0-9_$]*\s*=', line):
            issues.append(Issue(
                kind="OUTDATED HABIT",
                line=idx,
                title="OLD 'var' KEYWORD DETECTED!",
                message="'var' has confusing scope rules that cause mysterious bugs.",
                fix_hint="Use 'let' (for values that change) or 'const' (for values that stay same) instead!"
            ))

        # 5. Missing parentheses on console.log
        if "console.log" in line and not re.search(r'console\.log\s*\(', line):
            issues.append(Issue(
                kind="SYNTAX ERROR",
                line=idx,
                title="MISSING PARENTHESES ON CONSOLE.LOG!",
                message="console.log needs round brackets () to print your message.",
                fix_hint="Wrap your message like: console.log(\"Hello world!\");"
            ))

        # 6. NaN check bug: x === NaN
        if "=== NaN" in line or "== NaN" in line:
            issues.append(Issue(
                kind="QUIET BUG",
                line=idx,
                title="CANNOT CHECK NaN WITH EQUALITY!",
                message="In JavaScript, NaN === NaN is always false! It will never match.",
                fix_hint="Use Number.isNaN(value) to check if something is Not a Number."
            ))

        # 7. Unclosed string quotes check
        single_quotes = line.count("'") - line.count(r"\'")
        double_quotes = line.count('"') - line.count(r'\"')
        if (single_quotes % 2 != 0) and (double_quotes % 2 != 0):
            issues.append(Issue(
                kind="SYNTAX ERROR",
                line=idx,
                title="UNCLOSED TEXT QUOTE!",
                message="A sentence or word has a missing quotation mark at the end.",
                fix_hint="Make sure opening quotes have matching closing quotes: \"text\" or 'text'"
            ))

    return issues
