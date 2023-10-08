from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_leaderboard_load():
    opts = Options()
    opts.headless = True
    driver = Firefox(options=opts)
    driver.get('https://hacknight5leaderboard.vercel.app/')

    try:
        leaderboard = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'leaderboard-background'))
        )
        assert leaderboard


    finally:
        driver.quit()
