"""
Base Page - chứa các method và element chung cho tất cả trang
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    """Class cơ sở chứa các method chung cho tất cả trang"""
    
    def __init__(self, driver=None):
        """
        Khởi tạo BasePage
        Args:
            driver: WebDriver instance (nếu None sẽ tạo mới)
        """
        if driver is None:
            self.driver = self._create_driver()
        else:
            self.driver = driver
        
        # Khởi tạo WebDriverWait
        self.wait = WebDriverWait(self.driver, 10)
    
    def _create_driver(self):
        """Tạo Chrome driver với các options"""
        # Tạo Chrome options
        options = Options()
        # options.add_argument('--headless')  # Bỏ comment để chạy ẩn browser
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        
        try:
            # Sử dụng ChromeDriver đã cài đặt
            service = Service("/usr/local/bin/chromedriver")
            driver = webdriver.Chrome(service=service, options=options)
            driver.maximize_window()
            print("✅ Chrome driver khởi tạo thành công!")
            return driver
        except Exception as e:
            print(f"❌ Lỗi khởi tạo Chrome driver: {e}")
            raise
    
    def open_url(self, url):
        """Mở URL"""
        self.driver.get(url)
        print(f"✅ Đã mở URL: {url}")
    
    def find_element(self, by, value, timeout=10):
        """Tìm element với wait"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"❌ Không tìm thấy element: {by}={value}")
            raise
    
    def find_elements(self, by, value, timeout=10):
        """Tìm nhiều elements với wait"""
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            return elements
        except Exception as e:
            print(f"❌ Không tìm thấy elements: {by}={value}")
            raise
    
    def click_element(self, by, value, timeout=10):
        """Click element với wait"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            print(f"✅ Đã click element: {by}={value}")
        except Exception as e:
            print(f"❌ Không thể click element: {by}={value}")
            raise
    
    def send_keys_to_element(self, by, value, text, timeout=10):
        """Nhập text vào element với wait"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            element.clear()
            element.send_keys(text)
            print(f"✅ Đã nhập text '{text}' vào element: {by}={value}")
        except Exception as e:
            print(f"❌ Không thể nhập text vào element: {by}={value}")
            raise
    
    def get_element_text(self, by, value, timeout=10):
        """Lấy text của element với wait"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            text = element.text
            print(f"✅ Lấy được text: '{text}' từ element: {by}={value}")
            return text
        except Exception as e:
            print(f"❌ Không thể lấy text từ element: {by}={value}")
            raise
    
    def is_element_displayed(self, by, value, timeout=10):
        """Kiểm tra element có hiển thị không"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            is_displayed = element.is_displayed()
            print(f"✅ Element {by}={value} hiển thị: {is_displayed}")
            return is_displayed
        except Exception as e:
            print(f"❌ Không thể kiểm tra element: {by}={value}")
            return False
    
    def wait_for_url_contains(self, url_part, timeout=10):
        """Chờ URL chứa text cụ thể"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(url_part)
            )
            print(f"✅ URL đã chứa: {url_part}")
            return True
        except Exception as e:
            print(f"❌ URL không chứa: {url_part}")
            return False
    
    def get_current_url(self):
        """Lấy URL hiện tại"""
        url = self.driver.current_url
        print(f"✅ URL hiện tại: {url}")
        return url
    
    def get_page_title(self):
        """Lấy tiêu đề trang"""
        title = self.driver.title
        print(f"✅ Tiêu đề trang: {title}")
        return title
    
    def close_driver(self):
        """Đóng driver"""
        if self.driver:
            self.driver.quit()
            print("✅ Đã đóng browser!")
    
    def __del__(self):
        """Destructor - tự động đóng driver khi object bị xóa"""
        self.close_driver()
