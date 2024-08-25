from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Login_Page:
    def __init__(self, driver):
        self.driver = driver

    def boot(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

    def forgot_password(self, username):
        forgot_your_password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')))
        forgot_your_password.click()

        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@class='oxd-input oxd-input--active'][@placeholder='Username']")))
        username_field.send_keys(username)

        reset_password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        reset_password.click()

        reset_password_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']")))
        text_msg = reset_password_link.text
        print(text_msg)

        self.driver.back()
        self.driver.back()

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        password_input.send_keys(password)

        login_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")))
        login_input.click()

    def title_validation(self):
        title = self.driver.title
        return title == "OrangeHRM"

    def admin(self):
        admin = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Admin']")))
        admin.click()

    def user_management_validation(self):
        user_management = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item'][text()='User Management ']")))
        return user_management.is_displayed()

    def job_validation(self):
        job = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item'][text()='Job ']")))
        return job.is_displayed()

    def organization_validation(self):
        organization = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item'][text()='Organization ']")))
        return organization.is_displayed()

    def qualification_validation(self):
        qualification = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item'][text()='Qualifications ']")))
        return qualification.is_displayed()

    def nationalities_validation(self):
        nationalities = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//span[@class='oxd-topbar-body-nav-tab-item'])[5]")))
        return nationalities.is_displayed()

    def corporate_branding_validation(self):
        corporate_branding = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item'][text()='Corporate Branding']")))
        return corporate_branding.is_displayed()

    def configuration_validation(self):
        configuration = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//span[@class='oxd-topbar-body-nav-tab-item'])[5]")))
        return configuration.is_displayed()

    def admin_validation(self):
        admin = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Admin']")))
        return admin.is_displayed()

    def pim_validation(self):
        pim_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='PIM']")))
        return pim_menu.is_displayed()

    def leave_validation(self):
        leave_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Leave']")))
        return leave_menu.is_displayed()

    def time_validation(self):
        time_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Time']")))
        return time_menu.is_displayed()

    def recruitment_validation(self):
        recruitment_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Recruitment']")))
        return recruitment_menu.is_displayed()

    def myinfo_validation(self):
        myinfo_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='My Info']")))
        return myinfo_menu.is_displayed()

    def performance_validation(self):
        performance_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Performance']")))
        return performance_menu.is_displayed()

    def dashboard_validation(self):
        dashboard_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Dashboard']")))
        return dashboard_menu.is_displayed()

    def directory_validation(self):
        directory_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Directory']")))
        return directory_menu.is_displayed()

    def maintenance_validation(self):
        maintenance_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Maintenance']")))
        return maintenance_menu.is_displayed()

    def buzz_validation(self):
        buzz_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='Buzz']")))
        return buzz_menu.is_displayed()
