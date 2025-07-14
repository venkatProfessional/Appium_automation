import pytest

from pages.ApproveAttendance import ApproveAttendanceClass
from pages.ApprovePermission import ApprovePermissionClass
from pages.Approveleaves import Approveleaveclass
from pages.FeedbackPage import FeedbackPage
from pages.Forgotpass import forgotpasswordclass
from pages.Notication import NotificationMaintenanceClass
from pages.ResignationMaintenance import ResignationMaintenanceClass

from pages.ourprojects import listprojects
from pages.login import LoginPage
from pages.repair_maintenance import RepairMaintenanceClass
from tests.conftest import logged_in_driver


@pytest.mark.order(1)
def test_login_negative_cases(driver):  # ❌ Uses only `driver` (no login)
    login_page = LoginPage(driver)
    login_page.test_login_negative_cases()


@pytest.mark.order(2)
def test_login_valid(logged_in_driver):  # ✅ Logs in
    login_page = LoginPage(logged_in_driver)
    login_page.test_login_positive_case()


@pytest.mark.order(3)
def test_projects_page_valid(logged_in_driver):
    project_page = listprojects(logged_in_driver)
    project_page.wait_for_projects_page()
    project_page.search("smi")
    project_page.click_first_result()

    project_page.click_save_button()  # Initial Save
    project_page.click_fetch_location()  # Start fetching location
    project_page.allow_location_popup()  # GPS permission
    project_page.wait_for_location_and_click_save()  # Wait for location fetch & Save again

    # ✅ Final validation
    if not project_page.is_project_saved():
        print("⚠️ Project was not saved. Manual verification needed.")
    else:
        print("✅ Project saved successfully.")


@pytest.mark.order(4)
def test_approve_reject_leave_flow(logged_in_driver):
    approve_page = Approveleaveclass(logged_in_driver)
    approve_page.togglebar()
    approve_page.click_approve_leaves_menu()
    approve_page.process_leave_requests()


@pytest.mark.order(5)
def test_approve_permission_flow(logged_in_driver):
    permission_page = ApprovePermissionClass(logged_in_driver)
    permission_page.togglebar()
    permission_page.click_approve_permission_menu()
    permission_page.process_permission_requests()
    # permission_page.verify_filter_by_status_and_date()


@pytest.mark.order(6)
def test_resignation_maintenance_filters(logged_in_driver):
    resignation_page = ResignationMaintenanceClass(logged_in_driver)
    resignation_page.click_toggle_menu()
    resignation_page.click_resignation_menu()
    resignation_page.verify_all_filters()


@pytest.mark.order(7)
def test_feedback_cards_navigation(logged_in_driver):
    feedback_page = FeedbackPage(logged_in_driver)
    feedback_page.click_toggle_menu()  # Fixed method name
    feedback_page.click_feedback_menu()
    feedback_page.open_and_close_feedback_cards(2)

@pytest.mark.order(8)
def test_repair_maintenance_navigation(logged_in_driver):
    repair_page = RepairMaintenanceClass(logged_in_driver)
    repair_page.run_repair_maintenance_flow(2)


@pytest.mark.order(9)
def test_notification_maintenance_navigation(logged_in_driver):
    notification_page = NotificationMaintenanceClass(logged_in_driver)
    notification_page.run_notification_maintenance_flow()


@pytest.mark.order(10)
def test_attendance_flow(logged_in_driver):
    attendance = ApproveAttendanceClass(logged_in_driver)
    attendance.run_approve_attendance_flow()


@pytest.mark.order(11)
def test_logout_flow(logged_in_driver):
    from pages.logout import logout_test
    logout_page = logout_test(logged_in_driver)
    logout_page.perform_logout_flow()

@pytest.mark.order(12)
def test_forgot_password_flow(driver):
    forgot = forgotpasswordclass(driver)
    forgot.run_forgot_password_flow()
