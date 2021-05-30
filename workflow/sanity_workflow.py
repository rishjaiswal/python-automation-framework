from utils.logger_utils import get_logger
from utils.selenium_utils import SeleniumUtils
from configs import elements
from utils.driver_utils import driver
from utils.reporter_utils import HTMLReporter
import time

log = get_logger()


class SanityWorkflow:

    def __init__(html):
        log.info("Inside SanityWorkflow")
        SanityWorkflow.mac_click()
        log.info("Mac Home Page Title is : " + driver.title)
        i = 1;
        if driver.title == "Mac - Apple":
            html = HTMLReporter.create_test_data(html, "Sanity_TC_01", "Verify Mac Home Page Title ", "PASS")
        else:
            html = HTMLReporter.create_test_data(html, "Sanity_TC_01", "Verify Mac Home Page Title ", "FAIL")
        SanityWorkflow.click_apple()
        log.info("Apple Home Page Title is : " + driver.title)
        if driver.title == "Apple":
            html = HTMLReporter.create_test_data(html, "Sanity_TC_02", "Verify Apple Home Page Title ", "PASS")
        else:
            html = HTMLReporter.create_test_data(html, "Sanity_TC_02", "Verify Apple Home Page Title ", "FAIL")
        SanityWorkflow.iPad_click()
        log.info("iPad Home Page Title is : " + driver.title)
        if driver.title == "iPad - Apple":
            html = HTMLReporter.create_test_data(html, "Sanity_TC_03", "Verify iPad Home Page Title ", "PASS")
        else:
            html = HTMLReporter.create_test_data(html, "Sanity_TC_03", "Verify iPad Home Page Title ", "FAIL")
        SanityWorkflow.iPhone_click()
        log.info("iPhone Home Page Title is : " + driver.title)
        if driver.title == "iPhone - Apple":
            html = HTMLReporter.create_test_data(html, "Sanity_TC_04", "Verify iPhone Home Page Title ", "PASS")
        else:
            html = HTMLReporter.create_test_data(html, "Sanity_TC_04", "Verify iPhonne Home Page Title ", "FAIL")
        SanityWorkflow.iphone_click_learn_more()
        log.info("iPhone Learn More Page Title : " + driver.title)
        if driver.title == "Apple Card - Monthly Installments -Apple":
            html = HTMLReporter.create_test_data(html, "Sanity_TC_05", "Verify iPhone Learn More Page Title ", "PASS")
        else:
            html = HTMLReporter.create_test_data(html, "Sanity_TC_05", "Verify iPhone Learn More Page Title ", "FAIL")
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
