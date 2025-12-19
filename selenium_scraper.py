from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_reviews(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)

    wait = WebDriverWait(driver, 15)

    # 🔽 Scroll to trigger lazy loading
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2)

    reviews = []

    try:
        # ⚠️ Shiksha review text blocks (may change)
        elements = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class,'review')]")
            )
        )

        for el in elements[:5]:  # limit to avoid blocking
            text = el.text.strip()
            if text:
                reviews.append(text)

    except Exception as e:
        print("Could not fetch reviews:", e)

    driver.quit()
    return reviews
