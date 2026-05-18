# E-Commerce Selenium Automation Suite

This is an enterprise-level test automation framework built for E-Commerce web applications using Python, Selenium WebDriver, Pytest, and the Requests library. It demonstrates modern industry standards and Page Object Model (POM) architecture.

## Target Applications
* Web UI: [SauceDemo](https://www.saucedemo.com/)
* API: [FakeStoreAPI](https://fakestoreapi.com/)

## Features
* **Page Object Model (POM) Design** - Clean separation of logic and locators.
* **Data-Driven Testing** - Parameterized testing with Pytest.
* **Cross-Browser Support** - Tests run seamlessly on Chrome, Firefox, and Edge.
* **HTML Reporting** - Auto-generated test execution reports with Pytest HTML.
* **Automatic Screenshot Capture** - Captures screenshots on test failure.
* **Explicit Waits** - Robust synchronization avoiding hardcoded sleeps.
* **WebDriver Manager** - Automatic driver binaries management.
* **API Testing Integration** - Includes REST API tests using the `requests` library.

## Project Structure
```
ecommerce-selenium-suite/
├── pages/                  # Page Object classes
│   ├── login_page.py
│   ├── home_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── menu_page.py
├── tests/                  # Test scripts
│   ├── test_login.py
│   ├── test_search.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_logout.py
│   └── test_api.py
├── utils/                  # Reusable utilities and configuration
│   ├── config.py           # Test configurations (URLs, credentials)
│   ├── driver_factory.py   # Cross-browser initialization
│   ├── logger.py           # Custom logging configuration
│   ├── wait_utils.py       # Explicit wait helpers
│   └── screenshot.py       # Screenshot utility
├── reports/                # Generated HTML test reports
├── screenshots/            # Screenshots of failed tests
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
├── conftest.py             # Pytest fixtures and hooks
└── README.md               # Project documentation
```

## Setup Guide

### 1. Prerequisites
* Python 3.8 or higher installed
* IDE like PyCharm or VS Code
* Git installed

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/ecommerce-selenium-suite.git
cd ecommerce-selenium-suite
```

### 3. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Tests

### Basic Execution (Default Chrome)
```bash
pytest
```

### Run Tests on Specific Browser
```bash
pytest --browser=firefox
pytest --browser=edge
```

### Run Tests in Parallel
```bash
pytest -n 3
```

### Generate HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

## GitHub Upload Steps

1. Initialize git in your project directory:
   ```bash
   git init
   ```
2. Create a `.gitignore` file and add `venv/`, `__pycache__/`, `reports/`, `screenshots/`, `.pytest_cache/`.
3. Add all files:
   ```bash
   git add .
   ```
4. Commit your changes:
   ```bash
   git commit -m "Initial commit: E-Commerce Automation Framework"
   ```
5. Go to GitHub, create a new repository named `ecommerce-selenium-suite`.
6. Link local repository to GitHub:
   ```bash
   git branch -M main
   git remote add origin https://github.com/yourusername/ecommerce-selenium-suite.git
   git push -u origin main
   ```

**Q5: How do you run tests on different browsers?**
*Answer:* I implemented a `DriverFactory` class utilizing `webdriver-manager` to automatically download and setup the correct binaries. In Pytest, I added a custom command-line option `--browser`. The `setup` fixture in `conftest.py` reads this option and calls the `DriverFactory` to initialize Chrome, Firefox, or Edge accordingly, allowing me to switch browsers dynamically from the command line like `pytest --browser=firefox`.
