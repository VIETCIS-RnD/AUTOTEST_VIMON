from selenium.webdriver.support.ui import WebDriverWait


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
        print(f"Nhập username: {username_field.get_attribute('value')}")
        
        # Nhập password
        password_field = driver.find_element("id", "password")
        password_field.send_keys("root123456")
        print(f"Nhập password: {password_field.get_attribute('value')}")
        # Click login
        login_button = driver.find_element(
            "xpath", "/html/body/div/div/div[2]/div/form/div[2]/button"
        )
        login_button.click()
        print(f"Click login: {login_button.get_attribute('value')}")
        # Chờ trang chuyển sang màn hình overview
        wait = WebDriverWait(driver, 10)
        
        # Chờ URL chứa "/apps/overview"
        wait.until(lambda driver: "/apps/overview" in driver.current_url)
        print(f"Chờ URL chứa '/apps/overview': {driver.current_url}")
        # check lại url hiện tại
        current_url = driver.current_url
        print(f"URL hiện tại: {current_url}")
        
        assert "/apps/overview" in current_url, "Không nằm trong trang overview"