from utils.logger_utils import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_utils import driver, DriverUtils
from configs import config

log = get_logger()
driver = DriverUtils.initialize_driver()


class SeleniumUtils:
    def getElementBy(type, path):
        if type == "class":
            return driver.find_element_by_class_name(path)
        elif type == "css":
            return driver.find_element_by_css_selector(path)
        elif type == "id":
            return driver.find_element_by_id(path)
        elif type == "link":
            return driver.find_element_by_link_text(path)
        elif type == "xpath":
            return driver.find_element_by_xpath(path)
        else:
            print("Invalid Selector Type")
            return None
        return None

    def getElement(type, path):
        return SeleniumUtils.getElementBy(type, path)

    def click(element):
        element.click()

    def sendkeys(element, text):
        element.sendKeys(text)

    def isVisible(element):
        flag = False
        driver.implicitly_wait(config.IMPLICITTWAIT_TIME)
        try:
            if element.isDisplayed():
                flag = True
        except Exception as e:
            log.fatal("Exception occured", exc_info=True)
        return flag

    def waitUntilElementVisible(element):
        wait = WebDriverWait(driver, config.EXPLICITWAIT_TIME)
        return wait.until(EC.visibilityOf(element))
