import pickle
import time
import undetected_chromedriver as uc

options = uc.ChromeOptions()
options.user_data_dir = "C:/Users/hp/AppData/Local/Google/Chrome/User Data"
options.add_argument("profile-directory=Default")
options.add_argument("--start-maximized")

driver = uc.Chrome(options=options)

try:
    driver.get("https://timebucks.com")
    print("✅ Logged-in Chrome opened. Please wait 60 seconds...")

    time.sleep(60)  # Let you verify it's logged in before saving cookies

    with open("timebucks_cookies.pkl", "wb") as f:
        pickle.dump(driver.get_cookies(), f)

    print("✅ Cookies saved to timebucks_cookies.pkl")

except Exception as e:
    print(f"❌ ERROR: {e}")

finally:
 driver.quit()