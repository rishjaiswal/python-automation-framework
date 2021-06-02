from configs import constants
import os

RESULTS_PATH = constants.Results.RESULTS_LOCATION
LOGS_PATH = constants.Results.LOGS_LOCATION

# ProjectConfigurations
PROJECT_PATH = os.getcwd()
RESOURCES_PATH = os.path.join(PROJECT_PATH, constants.Resources.RESOURCES_LOCATION)
DRIVER_PATH = os.path.join(RESOURCES_PATH, constants.Resources.DRIVER_LOCATION)
TESTDATA_PATH = os.path.join(RESOURCES_PATH, constants.Resources.TESTDATA_PATH , constants.Resources.TESTDATA_LOCATION)
SCREENSHOT_PATH = os.path.join(RESOURCES_PATH, constants.Resources.SCREENSHOT_LOCATION)
PIP_REQUIREMENTS_PATH = os.path.join(PROJECT_PATH, constants.Resources.PIP_LOCATION)
IMPLICITWAIT_TIME = constants.Wait.IMPLICITWAIT
EXPLICITWAIT_TIME = constants.Wait.EXPLICITWAIT

# Sanity Test Configurations
BASE_URL = constants.SanityTest.BASE_URL_LOCATION
BROWSER = constants.SanityTest.BROWSER_NAME

# Performance Test Configurations
PERFORMANCE_ITERATION = 2
