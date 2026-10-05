"""Random quiz and reward system for CodeCoach JS."""
from __future__ import annotations

import random

QUESTIONS = [
    {
        "q": "Which keyword is best for a variable whose value never changes?",
        "options": ["A) var", "B) let", "C) const", "D) fix"],
        "answer": "C",
        "hint": "Think of the word 'constant'!"
    },
    {
        "q": "Which operator checks both value AND data type strictly in JavaScript?",
        "options": ["A) =", "B) ==", "C) ===", "D) !=="],
        "answer": "C",
        "hint": "Three equals are stricter than two!"
    },
    {
        "q": "How do you correctly print something to the browser console?",
        "options": ["A) print('Hi')", "B) console.log('Hi')", "C) echo('Hi')", "D) write('Hi')"],
        "answer": "B",
        "hint": "It starts with 'console.'"
    },
    {
        "q": "What is the result of 'typeof 42' in JavaScript?",
        "options": ["A) 'number'", "B) 'integer'", "C) 'float'", "D) 'digit'"],
        "answer": "A",
        "hint": "JavaScript lumps all numbers into one type name."
    }
]

REWARDS = [
    "🏆 JavaScript Code Ninja Badge!",
    "⭐ Web Wizard Star of Honor!",
    "🚀 Frontend Explorer Trophy!",
    "💎 Diamond JS Master Token!"
]

def run_quiz():
    q = random.choice(QUESTIONS)
    print("\n" + "=" * 55)
    print("       🎯 CODECOACH JS: CHALLENGE QUESTION!       ")
    print("=" * 55)
    print(f"\n{q['q']}\n")
    for opt in q["options"]:
        print(f"  {opt}")
    print()

    ans = input("Your Answer (A, B, C, or D): ").strip().upper()
    if ans == q["answer"]:
        reward = random.choice(REWARDS)
        print("\n🎉 CORRECT! AMAZING JOB!")
        print(f"🎁 REWARD UNLOCKED: {reward}\n")
    else:
        print(f"\n❌ Not quite! The correct answer was {q['answer']}.")
        print(f"💡 Hint: {q['hint']}\n")

if __name__ == "__main__":
    run_quiz()
