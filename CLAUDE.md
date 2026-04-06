# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Repository Overview

This is a student submission repository for the [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) course. The owner enrolled on August 4, 2024. Each assignment lives in its own subdirectory and contains a single Python solution file.

## Repository Structure

```
cs50-python-submissions/
├── CLAUDE.md                        # This file
├── README.md                        # Project overview
├── hello.py                         # Root-level introductory example
└── functions, variables/            # Week/unit assignment group
    ├── einstein/
    │   └── einstein.py              # E=mc² energy calculation
    ├── faces/
    │   └── faces.py                 # Emoji/text conversion
    ├── indoor/
    │   └── indoor.py                # String case conversion
    ├── playback/
    │   └── playback.py              # String substitution
    └── tip/
        └── tip.py                   # Tip calculator
```

New assignment groups are added as top-level directories named after the CS50 week/unit (e.g., `loops/`, `exceptions/`, `libraries/`). Each problem gets its own subdirectory matching the problem name, containing one `.py` file with the same name.

## Code Conventions

### Entry Point Pattern

All programs use an explicit `main()` function called at the bottom of the file — not guarded by `if __name__ == "__main__"`:

```python
def main():
    # program logic here

def helper_function(arg):
    # helper logic

main()
```

### File Naming

- Directory name matches problem name (lowercase): `tip/tip.py`, `indoor/indoor.py`
- One `.py` file per problem directory — no supporting modules

### Input / Output

Programs use `input()` for prompts and `print()` for output. No external libraries are used; all solutions rely solely on the Python standard library.

### Helper Functions

Logic is extracted into named helper functions rather than placed inline in `main()`. Example from `tip/tip.py`:

```python
def dollars_to_float(d):
    return float(d[1:])

def percent_to_float(p):
    return float(p[:-1]) / 100
```

### What Is (Intentionally) Absent

- No type hints or docstrings (beginner-level course work)
- No input validation or error handling (not required by CS50 problem specs)
- No external dependencies (`requirements.txt` not needed)
- No unit tests (CS50 uses its own `check50` grading tool, not pytest)
- No `.gitignore` (no generated files to ignore)

## Development Workflow

### Adding a New Assignment

1. Create the problem directory inside the relevant unit folder:
   ```
   mkdir -p "functions, variables/new_problem"
   ```
2. Create the solution file with the same name as the directory:
   ```
   touch "functions, variables/new_problem/new_problem.py"
   ```
3. Write the solution following the entry-point pattern above.
4. Commit with a descriptive message referencing the problem name.

### Running Solutions

Each file is a standalone script:

```bash
python "functions, variables/tip/tip.py"
```

No installation, virtual environment, or build step is required.

### Testing

CS50 assignments are graded via the `check50` and `style50` CLI tools provided by the course. There is no local test suite in this repository. To run the official checks (requires the CS50 tools to be installed):

```bash
check50 cs50/problems/2022/python/tip
style50 tip.py
```

## Git Conventions

- The default branch is `main`.
- Feature/documentation branches follow the pattern `claude/<description>-<id>`.
- Commit messages are short, plain-English descriptions of what was added (e.g., `"functions, variables"`, `"Create README.md"`).
- One commit per assignment group or logical unit of work.

## Notes for AI Assistants

- Do not add type hints, docstrings, or error handling unless the user explicitly requests it — this is course work intentionally written at a beginner level.
- Do not restructure or rename existing files; CS50's grader expects specific filenames.
- Do not introduce external dependencies.
- When adding new solutions, mirror the existing directory/file naming pattern exactly.
- The typo `sqared` in `einstein/einstein.py` is pre-existing; only fix it if the user asks.
