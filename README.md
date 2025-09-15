# Dự án Automation Test Cơ Bản

Dự án automation test đơn giản sử dụng Selenium + pytest + Allure cho người mới học.

## 📁 Cấu trúc dự án

```
AUTOTEST_VIMON/
├── requirements.txt          # Các thư viện cần cài
├── conftest.py              # Cấu hình pytest
├── login_page.py            # Page Object cho trang login
├── test_login.py            # Test cases
├── run_test.py              # Script chạy test
└── README.md                # Hướng dẫn này
```

## 🚀 Cách sử dụng

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 2. Chạy test
```bash
python run_test.py
```

Hoặc chạy trực tiếp:
```bash
pytest test_login.py -v --alluredir=allure-results
```

### 3. Xem báo cáo Allure
```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## 📝 Giải thích các file

### `conftest.py`
- Chứa các fixture (driver, test_data)
- Chạy trước mỗi test case
- Tự động mở/đóng browser

### `login_page.py`
- Page Object Pattern
- Chứa các element và method của trang login
- Dễ bảo trì và tái sử dụng

### `test_login.py`
- Chứa các test case
- Sử dụng Allure để tạo báo cáo đẹp
- 3 test case cơ bản:
  - Login thành công
  - Login thất bại
  - Login với username trống

### `run_test.py`
- Script đơn giản để chạy test
- Tự động tạo và mở báo cáo Allure

## 🎯 Test Cases

1. **test_login_success**: Test login với thông tin đúng
2. **test_login_fail**: Test login với thông tin sai
3. **test_login_empty_username**: Test login với username trống

## 📊 Báo cáo

Sau khi chạy test, báo cáo Allure sẽ hiển thị:
- Kết quả test (Pass/Fail)
- Screenshot khi test fail
- Thời gian chạy test
- Chi tiết từng bước test

## 🔧 Tùy chỉnh

Để test trên website khác, chỉ cần:
1. Sửa URL trong `login_page.py`
2. Sửa các locator (ID, class) cho phù hợp
3. Sửa dữ liệu test trong `conftest.py`

## 📚 Học thêm

- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Documentation](https://docs.qameta.io/allure/)
