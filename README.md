# Sauce Demo - Automated Testing Project

Automated end-to-end testing of an e-commerce website (saucedemo.com) using Python and Playwright.

## Features Tested
- Valid login
- Invalid login (error message validation)
- Add to cart functionality
- Complete checkout flow

## Tech Stack
- Python
- Playwright
- Pytest

## How to Run
pip install -r requirements.txt
playwright install
pytest tests/ --headed

## Test Results
All 4 test cases passing ✅

## Manual Test Cases
Manual test cases are documented in `manual_test_cases.xlsx`, covering login, cart, and checkout scenarios with expected vs actual results.

## API Testing
API testing done using Postman on JSONPlaceholder API, covering:
- Valid user data retrieval (status code + response validation)
- Invalid user handling (404 error check)

Postman collection exported as `api_tests_postman_collection.json`.