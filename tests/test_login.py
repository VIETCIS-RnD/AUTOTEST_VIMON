"""
Test cases cho chức năng login
"""
import allure
import sys
import os

# Thêm thư mục gốc vào Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from login_page import LoginPage


@allure.feature("Login Tests")
class TestLogin:
    """Class chứa các test case cho login"""
    
    @allure.story("Test login thành công")
    @allure.title("Login với thông tin đúng")
    def test_login_success(self, driver, test_data):
        """Test login với username và password đúng"""
        # Tạo object LoginPage
        login_page = LoginPage(driver)
        
        # Mở trang login
        login_page.open_login_page()
        
        # Thực hiện login
        login_page.login(test_data["valid_username"], test_data["valid_password"])
        
        # Kiểm tra login thành công
        assert login_page.is_login_successful(), "Login should be successful"
    
    @allure.story("Test login thất bại")
    @allure.title("Login với thông tin sai")
    def test_login_fail(self, driver, test_data):
        """Test login với username và password sai"""
        # Tạo object LoginPage
        login_page = LoginPage(driver)
        
        # Mở trang login
        login_page.open_login_page()
        
        # Thực hiện login với thông tin sai
        login_page.login(test_data["invalid_username"], test_data["invalid_password"])
        
        # Kiểm tra có thông báo lỗi
        error_message = login_page.get_error_message()
        assert error_message != "", "Should show error message"
    
    @allure.story("Test login với username trống")
    @allure.title("Login với username trống")
    def test_login_empty_username(self, driver, test_data):
        """Test login với username trống"""
        # Tạo object LoginPage
        login_page = LoginPage(driver)
        
        # Mở trang login
        login_page.open_login_page()
        
        # Thực hiện login với username trống
        login_page.login("", test_data["valid_password"])
        
        # Kiểm tra không login được
        assert not login_page.is_login_successful(), "Login should fail with empty username"
