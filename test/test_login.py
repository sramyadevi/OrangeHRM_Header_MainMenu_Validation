import pytest
from pages.login_page import Login_Page


# Forgot Password Link Validation
@pytest.mark.parametrize("username", ["Admin"])
def test_forgot_password_validation(driver, username):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.forgot_password(username)


# Header Validation on Admin Page
@pytest.mark.parametrize("username, password, expected_result", [
    ("Admin", "admin123", True)
])
def test_header_validation(driver, username, password, expected_result):
    login_page = Login_Page(driver)
    login_page.login(username, password)

    login_page.admin()

    result = login_page.title_validation()

    if result == expected_result:
        print("\nTitle of the page is validated.")

    # Validated below options are displayed on Admin Page
    user_management_displayed = login_page.user_management_validation()
    if user_management_displayed:
        print("\nUser Management option is displayed on admin page.")
    assert user_management_displayed, "User Management is not displayed."

    job_displayed = login_page.job_validation()
    if job_displayed:
        print("Job option is displayed on admin page.")
    assert job_displayed, "Job option is not displayed."

    organization_displayed = login_page.organization_validation()
    if organization_displayed:
        print("Organization option is displayed on admin page.")
    assert organization_displayed, "Organization option is not displayed."

    qualification_displayed = login_page.qualification_validation()
    if qualification_displayed:
        print("Qualification option is displayed on admin page.")
    assert qualification_displayed, "Qualification option is not displayed."

    nationalities_displayed = login_page.nationalities_validation()
    if nationalities_displayed:
        print("Nationalities option is displayed on admin page.")
    assert nationalities_displayed, "Nationalities option is not displayed."

    corporate_branding_displayed = login_page.corporate_branding_validation()
    if corporate_branding_displayed:
        print("Corporate Branding option is displayed on admin page.")
    assert corporate_branding_displayed, "Corporate Branding option is not displayed."

    configuration_displayed = login_page.configuration_validation()
    if configuration_displayed:
        print("Configuration option is displayed on admin page.")
    assert configuration_displayed, "Configuration option is not displayed."


# Main Menu Validation on Admin Page
def test_main_menu_validation(driver):
    login_page = Login_Page(driver)

    admin_menu_displayed = login_page.admin_validation()
    if admin_menu_displayed:
        print("\nFollowing MENU Options are displayed on the Admin Page:")
        print("Admin Menu option is displayed on Admin Page.")
    assert admin_menu_displayed, "Admin Menu option is not displayed."

    pim_menu_displayed = login_page.pim_validation()
    if pim_menu_displayed:
        print("PIM Menu option is displayed on Admin Page.")
    assert pim_menu_displayed, "PIM Menu option is not displayed."

    leave_menu_displayed = login_page.leave_validation()
    if leave_menu_displayed:
        print("Leave Menu option is displayed on Admin Page.")
    assert leave_menu_displayed, "Leave Menu option is not displayed."

    time_menu_displayed = login_page.time_validation()
    if time_menu_displayed:
        print("Time Menu option is displayed on Admin Page.")
    assert time_menu_displayed, "Time Menu option is not displayed."

    recruitment_menu_displayed = login_page.recruitment_validation()
    if recruitment_menu_displayed:
        print("Recruitment Menu option is displayed on Admin Page.")
    assert recruitment_menu_displayed, "Recruitment Menu option is not displayed."

    myinfo_menu_displayed = login_page.myinfo_validation()
    if myinfo_menu_displayed:
        print("My Info Menu option is displayed on Admin Page.")
    assert myinfo_menu_displayed, "My Info Menu option is not displayed."

    performance_menu_displayed = login_page.performance_validation()
    if performance_menu_displayed:
        print("Performance Menu option is displayed on Admin Page.")
    assert performance_menu_displayed, "Performance Menu option is not displayed."

    dashboard_menu_displayed = login_page.dashboard_validation()
    if dashboard_menu_displayed:
        print("Dashboard Menu option is displayed on Admin Page.")
    assert dashboard_menu_displayed, "Dashboard Menu option is not displayed."

    directory_menu_displayed = login_page.directory_validation()
    if directory_menu_displayed:
        print("Directory Menu option is displayed on Admin Page.")
    assert directory_menu_displayed, "Directory Menu option is not displayed."

    maintenance_menu_displayed = login_page.maintenance_validation()
    if maintenance_menu_displayed:
        print("Maintenance Menu option is displayed on Admin Page.")
    assert maintenance_menu_displayed, "Maintenance Menu option is not displayed."

    buzz_menu_displayed = login_page.buzz_validation()
    if buzz_menu_displayed:
        print("Buzz Menu option is displayed on Admin Page.")
    assert buzz_menu_displayed, "Buzz Menu option is not displayed."
