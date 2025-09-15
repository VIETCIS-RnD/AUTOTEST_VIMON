#!/usr/bin/env python3
"""
Script đơn giản để chạy test
"""
import subprocess
import sys


def run_tests():
    """Chạy tất cả test cases"""
    print("🚀 Bắt đầu chạy test...")
    
    # Chạy pytest - chạy tất cả test từ thư mục tests (tạm thời disable Allure)
    cmd = "python -m pytest tests/ -v"
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("✅ Test chạy thành công!")
        
    except subprocess.CalledProcessError:
        print("❌ Test thất bại!")
        sys.exit(1)


if __name__ == "__main__":
    run_tests()
