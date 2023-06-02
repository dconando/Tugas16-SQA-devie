from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='E:\aplikasi\chrome\chromedriver.exe')

# Test Case 1: Membuka halaman Google
driver.get('https://www.google.com')
assert "Google" in driver.title, "Test Case 1 Failed: Halaman Google tidak terbuka"

# Test Case 2: Mencari kata kunci di Google
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Selenium')
search_box.submit()
assert "Hasil Pencarian" in driver.title, "Test Case 2 Failed: Halaman hasil pencarian tidak terbuka"

# Test Case 3: Mengklik tautan pertama di hasil pencarian
first_link = driver.find_element(By.CSS_SELECTOR, '#search .g a')
first_link.click()
assert "Selenium" in driver.title, "Test Case 3 Failed: Halaman tautan pertama tidak terbuka"

# Test Case 4: Mengisi formulir login di halaman Facebook
driver.get('https://www.facebook.com')
email_input = driver.find_element(By.ID, 'email')
email_input.send_keys('email@example.com')

password_input = driver.find_element(By.ID, 'pass')
password_input.send_keys('password123')

login_button = driver.find_element(By.NAME, 'login')
login_button.click()

assert "Beranda" in driver.title, "Test Case 4 Failed: Halaman beranda tidak terbuka setelah login"

# Jika semua test case berhasil
print("Semua test case berhasil")

# Menutup browser
driver.quit()
