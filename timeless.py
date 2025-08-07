from keep_alive import keep_alive
keep_alive()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# === CONFIG ===
CHROME_PROFILE_PATH = "/app/.config/google-chrome"  # For Replit container
TIMEBUCKS_URL = "https://timebucks.com/dashboard"

# === SETUP CHROMEDRIVER ===
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.binary_location = "/usr/bin/google-chrome"  # Render's location

driver = webdriver.Chrome(options=chrome_options)

# === LOGIN ===
driver.get(TIMEBUCKS_URL)
time.sleep(10)
print("✅ Logged in successfully!")

# === AUTOMATION LOOP ===
while True:
    try:
        # === SLIDESHOWS ===
        print("▶ Slideshows")
        driver.get("https://timebucks.com/tasks2/slideshow")
        time.sleep(5)
        try:
            while True:
                next_btn = driver.find_element(By.ID, "next-slide")
                next_btn.click()
                time.sleep(3)
        except:
            print("✅ Slideshow done")

        # === ARTICLES ===
        print("▶ Articles")
        driver.get("https://timebucks.com/tasks2/articles")
        time.sleep(5)
        try:
            read_btn = driver.find_element(By.CLASS_NAME, "start_reading_btn")
            read_btn.click()
            time.sleep(25)
            driver.back()
        except:
            print("✅ No articles available")

        # === POLLS ===
        print("▶ Polls")
        driver.get("https://timebucks.com/tasks2/polls")
        time.sleep(5)
        try:
            options_list = driver.find_elements(By.NAME, "answer")
            if options_list:
                options_list[0].click()
                submit = driver.find_element(By.ID, "poll_submit_btn")
                submit.click()
                time.sleep(2)
        except:
            print("✅ No polls or error")

        # === CAPTCHA ===
        print("▶ Captchas")
        driver.get("https://timebucks.com/tasks2/captcha")
        time.sleep(5)
        try:
            start_btn = driver.find_element(By.ID, "captcha_start")
            start_btn.click()
            time.sleep(15)
        except:
            print("✅ No captchas now")

        # === FAUCET ===
        print("▶ Faucet")
        driver.get("https://timebucks.com/faucet")
        time.sleep(5)
        try:
            roll = driver.find_element(By.ID, "roll")
            roll.click()
            time.sleep(10)
        except:
            print("✅ Faucet already claimed")

        print("⏳ Sleeping 15 mins before next cycle...")
        time.sleep(900)

    except Exception as e:
        print("❌ ERROR:", e)
    time.sleep(60)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"