from utils.logger_utils import get_logger
from utils.selenium_utils import SeleniumUtils
from configs import elements
from utils.driver_utils import driver
from utils.reporter_utils import HTMLReporter
from utils.excel_utils import ExcelUtils
from utils.screencapture_utils import ScreenCaptureUtils

log = get_logger()


class SanityWorkflow:

    def __init__(html):
        log.info("Inside SanityWorkflow")

        # To get the data from Excel
        excel_data = ExcelUtils.read_from_excel()

        # Work-around to directly use excel_data[0][0],[1][0]...[4][0] as a Test Case Numbers
        testcase_numbers = []
        for data in excel_data:
            testcase_numbers.append(data[0])

        # Workflow Execution
        SanityWorkflow.mac_click()
        results = []
        log.info("Mac Home Page Title is : " + driver.title)
        if driver.title == "Mac - Apple":
            results.append("PASS")
        else:
            results.append("FAIL")
            ScreenCaptureUtils.take_screenshot(testcase_numbers[0])
        SanityWorkflow.click_apple()
        log.info("Apple Home Page Title is : " + driver.title)
        if driver.title == "Apple":
            results.append("PASS")
        else:
            results.append("FAIL")
            ScreenCaptureUtils.take_screenshot(testcase_numbers[1])
        SanityWorkflow.iPad_click()
        log.info("iPad Home Page Title is : " + driver.title)
        if driver.title == "iPad - Apple":
            results.append("PASS")
        else:
            results.append("FAIL")
            ScreenCaptureUtils.take_screenshot(testcase_numbers[2])
        SanityWorkflow.iPhone_click()
        log.info("iPhone Home Page Title is : " + driver.title)
        if driver.title == "iPhone - Apple":
            results.append("PASS")
        else:
            results.append("FAIL")
            ScreenCaptureUtils.take_screenshot(testcase_numbers[3])
        SanityWorkflow.iphone_click_learn_more()
        log.info("iPhone Learn More Page Title : " + driver.title)
        if driver.title == "Apple Card - Monthly Installments -Apple":
            results.append("PASS")
        else:
            results.append("FAIL")
            ScreenCaptureUtils.take_screenshot(testcase_numbers[4])

        # Compiling Results
        i = 0
        for data in excel_data:
            html = HTMLReporter.create_test_data(html, data[0], data[1], results[i])
            i += 1
        return html

    def mac_click():
        SeleniumUtils.click(SeleniumUtils.getElement(elements.elementType, elements.mac))

    def click_apple():
        SeleniumUtils.click(SeleniumUtils.getElement(elements.elementType, elements.apple))

    def iPhone_click():
        SeleniumUtils.click(SeleniumUtils.getElement(elements.elementType, elements.iPhone))

    def iPad_click():
        SeleniumUtils.click(SeleniumUtils.getElement(elements.elementType, elements.iPad))

    def iphone_click_learn_more():
        SeleniumUtils.click(SeleniumUtils.getElement(elements.elementType, elements.iPhone_learnMoreLink))
