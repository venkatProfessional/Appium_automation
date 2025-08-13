# regression_suite.py
import pytest

from tests.test_workflow import (
    test_login_negative_cases,
    test_login_valid,
    test_projects_page_valid,
    test_approve_reject_leave_flow,
    test_approve_permission_flow,
    test_resignation_maintenance_filters,
    test_feedback_cards_navigation,
    test_repair_maintenance_navigation,
    test_notification_maintenance_navigation,
    test_attendance_flow,
    test_logout_flow,
    test_forgot_password_flow,
)


@pytest.mark.order(1)
def test_run_login_negative(driver):
    test_login_negative_cases(driver)


@pytest.mark.order(2)
def test_run_login_valid(logged_in_driver):
    test_login_valid(logged_in_driver)


@pytest.mark.order(3)
def test_run_projects(logged_in_driver):
    test_projects_page_valid(logged_in_driver)


@pytest.mark.order(4)
def test_run_approve_reject_leave(logged_in_driver):
    test_approve_reject_leave_flow(logged_in_driver)


@pytest.mark.order(5)
def test_run_approve_permission(logged_in_driver):
    test_approve_permission_flow(logged_in_driver)


@pytest.mark.order(6)
def test_run_resignation_filters(logged_in_driver):
    test_resignation_maintenance_filters(logged_in_driver)


@pytest.mark.order(7)
def test_run_feedback_navigation(logged_in_driver):
    test_feedback_cards_navigation(logged_in_driver)


@pytest.mark.order(8)
def test_run_repair_maintenance(logged_in_driver):
    test_repair_maintenance_navigation(logged_in_driver)


@pytest.mark.order(9)
def test_run_notification_maintenance(logged_in_driver):
    test_notification_maintenance_navigation(logged_in_driver)


@pytest.mark.order(10)
def test_run_attendance(logged_in_driver):
    test_attendance_flow(logged_in_driver)


@pytest.mark.order(11)
def test_run_logout(logged_in_driver):
    test_logout_flow(logged_in_driver)


@pytest.mark.order(12)
def test_run_forgot_password(driver):
    test_forgot_password_flow(driver)
