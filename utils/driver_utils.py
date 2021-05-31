from utils.logger_utils import get_logger
from selenium import webdriver
from configs import config
import os

log = get_logger()
driver = None


class DriverUtils:
    def initialize_driver():
        global driver
        if driver == None:
            log.info("Inside initialize_driver() method")
            if config.BROWSER == "chrome":
                if os.name == "nt":
                    driver = webdriver.Chrome(executable_path=os.path.join(config.DRIVER_PATH, "chromedriver.exe"))
                else:
                    driver = webdriver.Chrome(executable_path=os.path.join(config.DRIVER_PATH, "chromedriver"))
            elif config.BROWSER == "safari":
                driver = webdriver.Safari()
            else:
                if os.name == "nt":
                    driver = webdriver.Chrome(executable_path=os.path.join(config.DRIVER_PATH, "geckodriver.exe"))
                else:
                    driver = webdriver.Chrome(executable_path=os.path.join(config.DRIVER_PATH, "geckodriver"))
            log.info("Initializing the Base URL " + config.BASE_URL)
            driver.maximize_window()
            driver.implicitly_wait(config.IMPLICITWAIT_TIME)
            driver.set_page_load_timeout(config.IMPLICITWAIT_TIME)
            driver.get(config.BASE_URL)
            log.info("Finish initialize_driver() method")
            return driver
        return driver

    def quit_driver():
        global driver
        log.info("Inside quit_driver() method")
        driver.quit()
        log.info("Finish quit_driver() method")
