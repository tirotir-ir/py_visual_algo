# Contributing to `py_visual_algo`

We welcome contributions to the `py_visual_algo` library! Whether it's bug fixes, new features, documentation improvements, or testing, your help is greatly appreciated.

## Getting Started

1. **Fork the Repository**: Start by forking the `py_visual_algo` repository on GitHub.
2. **Clone the Repository**: Clone your fork to your local machine.
```bash
   git clone https://github.com/<your-username>/py_visual_algo.git
   cd py_visual_algo
```

3. **Set Up the Environment**:

    Install dependencies:
```bash
    pip install -r requirements-dev.txt
```
## Development Guidelines

1.  Coding Standards:
        Use Black for code formatting.
```bash
    black .
```
    Follow PEP 8 guidelines for Python code.

2.  Testing:

    Write tests for any new features in the tests directory.
    Run tests using pytest.

```bash
        pytest
```

3.  Documenting:
    Add docstrings to all new functions and classes.
    Update api_reference.md if new functionality is added.

## Submitting Changes

1.  Create a Branch:

```bash
git checkout -b feature/<your-feature-name>
```
2.  Commit Your Changes:

    Write clear and concise commit messages.

```bash
git commit -m "Add <feature>"
```
3.  Push and Submit a Pull Request:
```bash
    git push origin feature/<your-feature-name>
```
    Open a pull request on the original repository.

Thank you for contributing!