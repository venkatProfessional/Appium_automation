import os

tests = [
    "tests/test_regression_flow.py::test_login_negative_cases",
    "tests/test_regression_flow.py::test_login_valid",
    "tests/test_regression_flow.py::test_attendance_flow"
]

for test in tests:
    print(f"➡ Running {test}")
    os.system(f"pytest {test} --alluredir=allure-results")

# Generate final report
os.system("allure generate allure-results --clean -o reports/allure-report")
os.system("allure open reports/allure-report")
