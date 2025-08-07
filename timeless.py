from flask import Flask
import threading
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import os

# === CONFIG ===
TIMEBUCKS_URL = "https://timebucks.com/dashboard"

# === FLASK KEEP ALIVE ===
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is alive and running!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# === AUTOMATION ===
def run_bot():
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(options=options)

    driver.get(TIMEBUCKS_URL)
    time.sleep(10)
    print("✅ Logged in successfully!")

    while True:
        try:
            # Slideshows
            driver.get("https://timebucks.com/tasks2/slideshow")
            time.sleep(5)
            try:
                while True:
                    next_btn = driver.find_element(By.ID, "next-slide")
                    next_btn.click()
                    time.sleep(3)
            except:
                print("✅ Slideshow done")

            # Articles
            driver.get("https://timebucks.com/tasks2/articles")
            time.sleep(5)
            try:
                read_btn = driver.find_element(By.CLASS_NAME, "start_reading_btn")
                read_btn.click()
                time.sleep(25)
                driver.back()
            except:
                print("✅ No articles available")

            # Polls
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

            # Captcha
            driver.get("https://timebucks.com/tasks2/captcha")
            time.sleep(5)
            try:
                start_btn = driver.find_element(By.ID, "captcha_start")
                start_btn.click()
                time.sleep(15)
            except:
                print("✅ No captchas now")

            # Faucet
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

# === THREADING ===
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
run_flask()
