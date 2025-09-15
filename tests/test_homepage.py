"""
Test cho trang chủ
"""


class TestHomepage:
    """Class chứa các test case cho trang chủ"""
    
    def test_homepage_title(self, driver):
        """Test kiểm tra tiêu đề trang chủ"""
        # Mở trang chủ
        driver.get("https://the-internet.herokuapp.com/")
        
        # Kiểm tra tiêu đề
        title = driver.title
        assert "The Internet" in title, f"Tiêu đề không đúng: {title}"
        
        print(f"✅ Tiêu đề trang chủ: {title}")
    
    def test_login_link(self, driver):
        """Test kiểm tra link Login có tồn tại"""
        # Mở trang chủ
        driver.get("https://the-internet.herokuapp.com/")
        
        # Tìm link Login
        login_link = driver.find_element("link text", "Form Authentication")
        assert login_link.is_displayed(), "Link Login không hiển thị"
        
        print("✅ Link Login đã tồn tại")
