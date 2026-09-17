# Coding Test Practice

Python coding test practice repository for job preparation.

## Study Rule

- Solve with `.py` files first.
- Use Jupyter Notebook only for concept experiments or visual notes.
- For each problem, record the approach, complexity, and mistakes.
- Push solved problems and notes through GitHub PRs.

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── coding-test-roadmap.md
│   └── wrong-answer-note-template.md
├── problems/
│   ├── baekjoon/
│   ├── programmers/
│   ├── leetcode/
│   └── softeer/
└── .github/
    └── pull_request_template.md
```

## File Naming

```text
problems/baekjoon/01000_a_plus_b.py
problems/programmers/lv1_incomplete_runner.py
problems/leetcode/0242_valid_anagram.py
problems/softeer/lv2_obstacle_recognition.py
```

## Basic Solution Template

```python
import sys


def solve():
    input = sys.stdin.readline


if __name__ == "__main__":
    solve()
```

## PR Routine

1. Create or update solution files under `problems/`.
2. Add explanation and wrong-answer notes to the PR body.
3. Include time complexity and space complexity.
4. Mention whether the problem should be solved again.
