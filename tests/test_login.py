"""
Test cases cho chức năng login
"""


class TestLogin:
    """Class chứa các test case cho login"""
    
    def test_login_success(self, driver, test_data):
        """Test login với username và password đúng"""
        # Mở trang login
        driver.get("https://the-internet.herokuapp.com/login")
        
        # Nhập username
        username_field = driver.find_element("id", "username")
        username_field.send_keys(test_data["valid_username"])
        
        # Nhập password
        password_field = driver.find_element("id", "password")
        password_field.send_keys(test_data["valid_password"])
        
        # Click login
        login_button = driver.find_element("css selector", "button.radius")
        login_button.click()
        
        # Kiểm tra login thành công
        assert "secure" in driver.current_url, "Login should be successful"
        print("✅ Login thành công!")
    
    def test_login_fail(self, driver, test_data):
        """Test login với username và password sai"""
        # Mở trang login
        driver.get("https://the-internet.herokuapp.com/login")
        
        # Nhập username sai
        username_field = driver.find_element("id", "username")
        username_field.send_keys(test_data["invalid_username"])
        
        # Nhập password sai
        password_field = driver.find_element("id", "password")
        password_field.send_keys(test_data["invalid_password"])
        
        # Click login
        login_button = driver.find_element("css selector", "button.radius")
        login_button.click()
        
        # Kiểm tra có thông báo lỗi
        error_message = driver.find_element("class name", "error")
        assert error_message.is_displayed(), "Should show error message"
        print("✅ Hiển thị thông báo lỗi!")
    
    def test_login_empty_username(self, driver, test_data):
        """Test login với username trống"""
        # Mở trang login
        driver.get("https://the-internet.herokuapp.com/login")
        
        # Để trống username
        username_field = driver.find_element("id", "username")
        username_field.send_keys("")
        
        # Nhập password
        password_field = driver.find_element("id", "password")
        password_field.send_keys(test_data["valid_password"])
        
        # Click login
        login_button = driver.find_element("css selector", "button.radius")
        login_button.click()
        
        # Kiểm tra không login được
        assert "secure" not in driver.current_url, "Login should fail with empty username"
        print("✅ Login thất bại với username trống!")
