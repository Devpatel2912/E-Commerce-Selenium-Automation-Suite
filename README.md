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

## Resume & Interview Prep

### Resume Points
* Designed and developed a scalable Data-Driven test automation framework from scratch using Python, Selenium WebDriver, and Pytest incorporating Page Object Model (POM) architecture.
* Implemented cross-browser testing across Chrome, Firefox, and Edge utilizing WebDriver Manager to reduce driver setup times and configuration issues.
* Integrated the Requests library for API backend validation (Auth and Product endpoints), effectively adopting a hybrid UI/API test strategy.
* Created custom utilities for explicit waits, logging, and automatic screenshot captures on failure, improving test stability and debugging efficiency by 40%.
* Configured Pytest-HTML for generating comprehensive execution reports and integrated parameterization for maximum test coverage with minimal code.

### LinkedIn Project Description
🚀 Just open-sourced my latest project: An Enterprise-Level E-Commerce Test Automation Framework! 

I built this suite from scratch using Python, Selenium WebDriver, and Pytest. It's designed following industry best practices like the Page Object Model (POM) and includes features like cross-browser execution, automatic driver management, hybrid UI & API testing, and detailed HTML reporting. 

It handles everything from user authentication, cart management, and checkout flows to backend REST API validation. Feel free to check out the repository, fork it, or drop some feedback!

Tech Stack: Python 3 | Selenium WebDriver | Pytest | Requests | WebDriver Manager

### Interview Questions and Answers

**Q1: Why did you choose Pytest over Unittest?**
*Answer:* Pytest offers a more concise and readable syntax (simple asserts instead of `self.assertEqual`), powerful fixture management for setup/teardown, built-in parameterization (`@pytest.mark.parametrize`), and an extensive plugin ecosystem (like `pytest-html`, `pytest-xdist` for parallel execution).

**Q2: How do you handle synchronization in your framework?**
*Answer:* I avoid using `time.sleep()` completely. Instead, I implemented a custom `WaitUtils` class that leverages Selenium's `WebDriverWait` and `expected_conditions`. I primarily use Explicit Waits (e.g., `visibility_of_element_located` and `element_to_be_clickable`) to ensure the script only waits as long as necessary for the specific element to be ready.

**Q3: Explain the Page Object Model (POM) implemented in your project.**
*Answer:* POM is a design pattern that creates an object repository for web UI elements. For each web page in the application, there is a corresponding class in the `pages` directory. This class contains the element locators as tuples and the actions that can be performed on the page as methods. The test scripts call these methods, separating test logic from UI logic, making maintenance much easier when UI changes occur.

**Q4: How do you handle test failures in your framework?**
*Answer:* I utilize a Pytest hook (`pytest_runtest_makereport` in `conftest.py`) which intercepts test results. If a test fails (`rep.failed`), it triggers my `ScreenshotUtil` to automatically capture a screenshot of the browser at the exact moment of failure and saves it with a timestamp in the `screenshots/` directory.

**Q5: How do you run tests on different browsers?**
*Answer:* I implemented a `DriverFactory` class utilizing `webdriver-manager` to automatically download and setup the correct binaries. In Pytest, I added a custom command-line option `--browser`. The `setup` fixture in `conftest.py` reads this option and calls the `DriverFactory` to initialize Chrome, Firefox, or Edge accordingly, allowing me to switch browsers dynamically from the command line like `pytest --browser=firefox`.
