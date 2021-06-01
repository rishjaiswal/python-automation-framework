from utils.logger_utils import get_logger
from utils.driver_utils import driver, DriverUtils
from configs import config
import os

log = get_logger()
driver = DriverUtils.initialize_driver()


class ScreenCaptureUtils:
    log.info("Implementation of ScreenCaptureUtils")

    def take_screenshot(test_case):
        # Python’s PIL library which lets us perform image operations= from PIL import Image
        log.info("Inside method take_screenshot() for capturing screenshots")
        driver.save_screenshot(os.path.join(config.SCREENSHOT_PATH, test_case + ".png"))
        log.info("Finished method take_screenshot()")
