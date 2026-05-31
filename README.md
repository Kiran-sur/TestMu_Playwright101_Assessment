# TestMu AI Selenium Playground Automation

This project contains a suite of automated end-to-end tests for the [TestMu AI Selenium Playground](https://www.testmuai.com/selenium-playground/) using Playwright and Python.

## Project Overview

The automation suite covers three primary test scenarios:
1. **Simple Form Demo**: Validating basic text input and display logic.
2. **Drag & Drop Sliders**: Handling complex mouse interactions to precisely move sliders to target values.
3. **Input Form Submit**: Testing comprehensive form validation, dropdown selection, and successful submission messages.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository** to your local machine.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Install Playwright browsers**:
   ```bash
   playwright install
   ```

## Running the Tests

You can execute each scenario individually using Python:

```bash
python test/test_testScnario1.py
python test/test_testScnario2.py
python test/test_testScnario3.py
```

## Project Structure

- `test/`: Contains the `.py` test scripts for each scenario.
- `requirements.txt`: Lists necessary Python libraries (`playwright`, `pytest-playwright`).
- `.gitignore`: Configured to exclude virtual environments, cache, and Playwright reports.
