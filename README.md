# Dự án Automation Test với Selenium

Dự án automation test đơn giản sử dụng Selenium + pytest cho việc test chức năng login.

## 📁 Cấu trúc dự án

```
AUTOTEST_VIMON/
├── requirements.txt          # Các thư viện cần cài
├── conftest.py              # Cấu hình pytest và fixtures
├── run_test.py              # Script chạy test
├── tests/                   # Thư mục chứa test cases
│   ├── __init__.py
│   └── test_login.py        # Test cases cho login
├── drivers/                 # Thư mục chứa ChromeDriver
│   └── chromedriver         # ChromeDriver executable
└── README.md                # Hướng dẫn này
```

## 🚀 Cách sử dụng

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 2. Chạy test
```bash
# Chạy tất cả test
python run_test.py

# Hoặc chạy trực tiếp với pytest
python -m pytest tests/ -v

# Chạy 1 test cụ thể
python -m pytest tests/test_login.py::TestLogin::test_login_success -v
```

### 3. Các lệnh pytest hữu ích
```bash
# Chạy test với output chi tiết
python -m pytest tests/ -v -s

# Chạy test và dừng khi gặp lỗi đầu tiên
python -m pytest tests/ -x

# Chạy test và hiển thị browser (không headless)
python -m pytest tests/ -v -s
```

## 📝 Giải thích các file

### `conftest.py`
- **Chứa fixtures**: `driver`, `test_data`
- **Tự động khởi tạo**: ChromeDriver với các options
- **Tự động cleanup**: Đóng browser sau mỗi test
- **Cấu hình**: Chrome options (window size, no-sandbox, etc.)

### `tests/test_login.py`
- **Chứa test cases** cho chức năng login
- **3 test cases**:
  - `test_login_success`: Test login thành công
  - `test_login_fail`: Test login thất bại  
  - `test_login_empty_username`: Test login với username trống
- **Sử dụng fixtures** từ `conftest.py`

### `run_test.py`
- **Script đơn giản** để chạy test
- **Tự động chạy** tất cả test trong thư mục `tests/`
- **Hiển thị kết quả** test

### `drivers/chromedriver`
- **ChromeDriver executable** được đặt trong dự án
- **Tự động sử dụng** khi chạy test
- **Không cần cài đặt** ChromeDriver system-wide

## 🎯 Test Cases hiện tại

1. **test_login_success**: 
   - Mở trang login
   - Nhập username/password đúng
   - Click login
   - Kiểm tra URL sau login

2. **test_login_fail**:
   - Mở trang login  
   - Nhập username/password sai
   - Click login
   - Kiểm tra thông báo lỗi

3. **test_login_empty_username**:
   - Mở trang login
   - Để trống username
   - Nhập password
   - Click login
   - Kiểm tra không login được

## 🔧 Cấu hình

### Thay đổi URL test
Sửa URL trong file `tests/test_login.py`:
```python
driver.get("http://your-website.com/login")
```

### Thay đổi credentials
Sửa trong file `conftest.py`:
```python
@pytest.fixture
def test_data():
    return {
        "valid_username": "your_username",
        "valid_password": "your_password",
        # ...
    }
```

### Thay đổi Chrome options
Sửa trong file `conftest.py`:
```python
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Bỏ comment để chạy ẩn
options.add_argument('--window-size=1920,1080')
```

## 🐛 Troubleshooting

### Lỗi "pytest: command not found"
```bash
# Sử dụng python -m pytest thay vì pytest
python -m pytest tests/ -v
```

### Lỗi ChromeDriver
- ChromeDriver đã được đặt trong `drivers/` folder
- Nếu vẫn lỗi, kiểm tra Chrome browser version
- Có thể cần download ChromeDriver mới

### Test bị treo
- Kiểm tra network connection
- Kiểm tra URL có đúng không
- Thử chạy với `--headless` mode

## 📚 Học thêm

- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

## 🤝 Đóng góp

1. Fork dự án
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Tạo Pull Request