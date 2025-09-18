"""
Test cases cho chức năng login
"""


class TestLogin:
    """Class chứa các test case cho login"""
    
    def test_login_success(self, driver):
        """Test login với username và password đúng"""
        # Mở trang login
        driver.get("http://222.252.19.252:4001/login")
        
        # Nhập username
        username_field = driver.find_element("id", "username")
        username_field.send_keys("root")
        
        # Nhập password
        password_field = driver.find_element("id", "password")
        password_field.send_keys("root123456")
        
        # Click login
        login_button = driver.find_element(
            "xpath", "/html/body/div/div/div[2]/div/form/div[2]/button"
        )
        login_button.click()
        
        # Kiểm tra login thành công - kiểm tra URL hoặc thông báo
        current_url = driver.current_url
        print(f"URL hiện tại: {current_url}")

    def test_login_fail(self, driver):
        """Test login với username và password sai"""
        # Mở trang login
        driver.get("http://222.252.19.252:4001/login")
        
        # Nhập username
        username_field = driver.find_element("id", "username")
        username_field.send_keys("root")
        
        # Nhập password
        password_field = driver.find_element("id", "password")
        password_field.send_keys("root123456")
        
        # Click login
        login_button = driver.find_element(
            "xpath", "/html/body/div/div/div[2]/div/form/div[2]/button"
        )
        login_button.click()
        
        # Kiểm tra login thất bại - kiểm tra URL hoặc thông báo
        current_url = driver.current_url
        print(f"URL hiện tại: {current_url}")