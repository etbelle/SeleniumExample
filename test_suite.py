from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
print("options object created")

opt.add_argument("--remote-debugging-port=9222")
opt.add_argument('--no-sandbox')
opt.add_argument('--headless')
opt.add_argument('--window-size=1420,1080')
opt.add_argument('--disable-extensions')
opt.add_argument('--disable-dev-shm-usage')
opt.add_experimental_option("prefs",{"download.default_directory":"/databricks/driver"})

driver = webdriver.Chrome(options=opt, executable_path=r'./chromedriver')

print("Driver has been set")

driver.get("http://google.com/")
print("Headless Chrome Initialized")

driver.quit()