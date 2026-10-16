# LAB1 - MLOps (IE-7374)

## Overview

This lab introduces foundational MLOps practices through a Python calculator project. The main objectives are to:

- Create and use a Python virtual environment.
- Organize a project in a GitHub repository.
- Implement arithmetic functions in `src/calculator.py`.
- Write unit tests with `pytest` and Python's built-in `unittest`.
- Automate test execution with GitHub Actions.

## Project Structure

My repository structure is:

```text
.
├── .github/
│   └── workflows/
│       ├── pytest_action.yml
│       └── unittest_action.yml
├── data/
├── src/
│   └── calculator.py
├── test/
│   ├── test_pytest.py
│   └── test_unittest.py
├── .gitignore
├── README.md
└── requirements.txt
```

Keep `.github/workflows/` at the **root of the GitHub repository** so GitHub can discover and run the workflow files.

## 1. Set Up a Virtual Environment

From the project directory, create a virtual environment:

```bash
python3 -m venv lab_01
```

Activate it on macOS or Linux:

```bash
source lab_01/bin/activate
```

On Windows Command Prompt:

```bat
lab_01\Scripts\activate
```

On Windows PowerShell:

```powershell
.\lab_01\Scripts\Activate.ps1
```

When the environment is active, its name should appear in your terminal prompt.

## 2. Install Dependencies

With the virtual environment activated, install `pytest`:

```bash
python -m pip install pytest
```

If your project uses a `requirements.txt` file, install all listed dependencies with:

```bash
python -m pip install -r requirements.txt
```

For this lab, `pytest` is the main third-party testing dependency. `unittest` is included with Python.

## 3. Calculator Implementation

The calculator source code is stored in `src/calculator.py`. The lab's original functions cover basic arithmetic operations:

- `fun1(x, y)`: adds two numbers.
- `fun2(x, y)`: subtracts `y` from `x`.
- `fun3(x, y)`: multiplies two numbers.
- `fun4(x, y, z)`: adds three numbers.

I added functions for division and power.


## 4. Run Tests Locally

### Pytest

Run all tests in the `test` directory from the repository root:

```bash
python -m pytest test/
```

To run a particular test file:

```bash
python -m pytest test/test_pytest.py
```

Pytest discovers test functions whose names start with `test_`. Assertions are used to check expected results.

### Unittest

Run the unittest suite from the repository root:

```bash
python -m unittest test.test_unittest
```

Alternatively, if the test file is configured to call `unittest.main()`, run:

```bash
python test/test_unittest.py
```

Unittest test cases are generally methods beginning with `test_` inside classes that inherit from `unittest.TestCase`.

## 5. GitHub Actions

For this part, I added two YAML workflow files so GitHub can run the tests automatically when I push changes to the `main` branch.

Both files need to be saved in the `.github/workflows/` folder at the **root of the repository**:

```text
.github/
└── workflows/
    ├── pytest_action.yml
    └── unittest_action.yml
```

The `pytest_action.yml` file runs the Pytest tests, and `unittest_action.yml` runs the Unittest tests. After pushing changes, I can go to the **Actions** tab on GitHub to check whether the workflows ran successfully.

