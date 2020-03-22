from selenium import webdriver

if __name__ == "__main__":   
    test_drive = webdriver.Chrome()
    test_drive.get('https://www.google.com')