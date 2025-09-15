"""
Login page - chứa các element và method của trang login
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Class chứa các element và method của trang login"""
    
    # Định nghĩa các element trên trang
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button.radius")
    error_message = (By.CLASS_NAME, "error")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_login_page(self, url="https://the-internet.herokuapp.com/login"):
        """Mở trang login"""
        self.driver.get(url)
    
    def enter_username(self, username):
        """Nhập username"""
        username_field = self.wait.until(EC.presence_of_element_located(self.username_input))
        username_field.clear()
        username_field.send_keys(username)
    
    def enter_password(self, password):
        """Nhập password"""
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)
    
    def click_login_button(self):
        """Click nút login"""
        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()
    
    def login(self, username, password):
        """Thực hiện login hoàn chỉnh"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        """Lấy thông báo lỗi"""
        try:
            error = self.driver.find_element(*self.error_message)
            return error.text
        except Exception:
            return ""
    
    def is_login_successful(self):
        """Kiểm tra login có thành công không"""
        # Kiểm tra URL có chứa "secure" không (trang sau khi login thành công)
        current_url = self.driver.current_url
        return "secure" in current_url
