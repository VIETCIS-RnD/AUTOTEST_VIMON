"""
File cấu hình pytest - chạy trước mỗi test
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """Tạo browser driver cho mỗi test"""
    # Tạo Chrome options
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Chạy ẩn browser để nhanh hơn
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    try:
        # Sử dụng ChromeDriver trong dự án
        import os
        chromedriver_path = os.path.join(os.path.dirname(__file__), "drivers", "chromedriver")
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)
        print("✅ Chrome driver khởi tạo thành công!")
    except Exception as e:
        print(f"❌ Lỗi khởi tạo Chrome driver: {e}")
        raise
    
    # Chạy test
    yield driver
    
    # Đóng browser sau khi test xong
    driver.quit()
    print("✅ Đã đóng browser!")


@pytest.fixture
def test_data():
    """Dữ liệu test"""
    return {
        "valid_username": "tomsmith",
        "valid_password": "SuperSecretPassword!",
        "invalid_username": "wrong_user",
        "invalid_password": "wrong_pass"
    }


