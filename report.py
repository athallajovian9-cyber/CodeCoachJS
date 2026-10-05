"""Reporting engine for CodeCoach JS. Kid-friendly by default."""
from __future__ import annotations

from coach import Issue, analyze_js


def format_report(code: str, for_parents: bool = False) -> str:
    issues = analyze_js(code)
    if not issues:
        if for_parents:
            return "SUCCESS: Zero syntax or static linting warnings found in JavaScript file."
        return (
            "============================================================\n"
            "   🌟 ALL GOOD! YOUR JAVASCRIPT LOOKS CLEAN AND READY! 🌟  \n"
            "============================================================\n"
            "No bugs, loops, or tricky pitfalls spotted. Keep building! 🚀\n"
        )

    out = []
    if for_parents:
        out.append(f"CodeCoach JS Diagnostic Report: {len(issues)} issue(s) detected.\n")
        for i in issues:
            out.append(f"Line {i.line} [{i.kind}] {i.title}: {i.message} (Solution: {i.fix_hint})")
    else:
        out.append("============================================================")
        out.append("             🚀 CODECOACH JAVASCRIPT REVIEW               ")
        out.append("============================================================\n")
        for idx, i in enumerate(issues, start=1):
            out.append(f"👉 Problem #{idx} (Line {i.line}) - [{i.kind}]")
            out.append(f"   ⚠️  {i.title}")
            out.append(f"   💡 {i.message}")
            out.append(f"   🛠️  TRY THIS: {i.fix_hint}\n")
        out.append("You're doing great! Small fixes make you a master developer! 💻✨")

    return "\n".join(out)
