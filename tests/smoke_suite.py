# tests/smoke_suite.py

import pytest

from tests.test_workflow import (
    test_login_valid,
    test_logout_flow,
)

@pytest.mark.order(1)
def test_smoke_login_valid(logged_in_driver):
    test_login_valid(logged_in_driver)



@pytest.mark.order(3)
def test_smoke_logout(logged_in_driver):
    test_logout_flow(logged_in_driver)
