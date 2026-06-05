# Calculator

**Goal:** Test the Github workflow with a basic example!

A simple Python calculator library with basic arithmetic operations, tested with [pytest](https://docs.pytest.org/) and continuously integrated using GitHub Actions.

![Python](https://img.shields.io/badge/python-3.13-blue)

## Features

- `add(a, b)`: returns the sum of two numbers
- `subtract(a, b)`: returns the difference of two numbers
- `divide(a, b)`: returns the quotient, and raises `ValueError` when dividing by zero

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/soheilgholami/example-devops-project.git
cd example-devops-project
pip install -r requirements.txt
```

## Usage

```python
from calculator import add, subtract, divide

add(2, 3)      # 5
subtract(5, 2) # 3
divide(10, 2)  # 5.0

divide(1, 0)   # raises ValueError: Cannot divide by zero
```

## Running Tests

Run the full test with:

```bash
python -m pytest -v
```

The `-v` flag enables verbose output so you can see each test name as it runs.

## Continuous Integration

This project uses [GitHub Actions](https://docs.github.com/en/actions) to automatically run the test suite (whole collection of tests). 
Tests execute on every **push** and **pull request** targeting the `main` branch.

The workflow:

1. Checks out the repository
2. Sets up Python 3.13 with pip caching
3. Installs dependencies from `requirements.txt`
4. Runs the tests with `pytest`

## Understanding the Workflow File

The CI workflow lives in `.github/workflows/tests.yml`. Here's what each part does:

### `name`

```yaml
name: Run Tests
```

The display name of the workflow. This is what shows up in the **Actions** tab of your repository.

### `on`

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

The `on` key defines **what events trigger the workflow**. Here it runs in two cases:

- `push`: whenever commits are pushed to the `main` branch
- `pull_request`: whenever a pull request targets `main`

The `branches: [ main ]` filter limits it to the `main` branch only, so pushes to other branches won't trigger a run.

### `jobs`

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
```

A workflow is made of one or more **jobs**, which run in parallel by default. Here there's a single job with the ID `test`.

- `runs-on` specifies the **virtual machine** the job runs on. `ubuntu-latest` is a fresh Linux machine that GitHub spins up for you.

### `steps`

```yaml
    steps:
      - uses: actions/checkout@v6
```

Each job is a sequence of **steps** that run in order. A step either *uses* a pre-built action or *runs* a shell command.

- `uses` pulls in a reusable action. `actions/checkout@v6` is GitHub's official action that **copies your repository's code onto the machine** — without it, the runner would have nothing to test. The `@v6` pins it to major version 6.

### `with`

```yaml
      - uses: actions/setup-python@v6
        with:
          python-version: '3.13'
          cache: 'pip'
```

The `with` key passes **inputs (parameters)** into an action.

- `actions/setup-python@v6` installs Python on the runner.
- `python-version: '3.13'` tells it which version to install.
- `cache: 'pip'` caches your installed packages between runs, so future runs are faster.

### `run`

```yaml
      - run: pip install -r requirements.txt
      - run: pytest -v
```

The `run` key executes a **shell command** directly on the machine.

- The first installs your dependencies from `requirements.txt`.
- The second runs the test suite. `-v` (verbose) prints each test name as it runs.

> **Note:** Because the CI step uses `pip install -r requirements.txt`, make sure `pytest` is listed in that file — otherwise the `pytest -v` step will fail in CI.

### Quick reference

| Key | Purpose |
|-----|---------|
| `name` | Display name of the workflow |
| `on` | Events that trigger the workflow |
| `jobs` | The jobs to run |
| `runs-on` | The virtual machine to use |
| `steps` | Ordered list of actions/commands |
| `uses` | Run a pre-built, reusable action |
| `with` | Inputs passed to an action |
| `run` | Run a shell command |

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── tests.yml        # CI workflow
├── calculator.py            # Core functions
├── test_calculator.py       # Test suite
├── requirements.txt         # Dependencies
└── README.md
```