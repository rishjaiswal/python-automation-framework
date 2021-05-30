from utils.logger_utils import get_logger
from utils.reporter_utils import HTMLReporter
from utils.driver_utils import DriverUtils
from workflow.sanity_workflow import SanityWorkflow
from configs import config
import os, subprocess, sys

log = get_logger()

if __name__ == '__main__':
    log.info("Workflow Started")
    html = HTMLReporter.create_html()
    workflow_type = None

    try:
        # Set-up
        log.info("Started setting up packages through requirements.txt")
        subprocess.check_call(["pip3", "install", "-r", config.PIP_REQUIREMENTS_PATH])
        log.info("Completed setting up packages through requirements.txt")
        html = HTMLReporter.create_test_folder(html)
        DriverUtils.initialize_driver()
        if len(sys.argv) > 1:
            workflow_type = sys.argv[1]

        # Execution Steps
        log.info("Workflow Execution In Progress")
        if workflow_type == "SanityWorkflow":
            log.info("Sanity Workflow Execution")
            html = SanityWorkflow.__init__(html)
        elif workflow_type == "PerformanceWorkflow":
            log.info("Performance Workflow Execution")
        else:
            log.trace("No Workflow Matching with Workflowtype for Execution")

        # Clean-up
        DriverUtils.quit_driver()

    except Exception as e:
        log.fatal("Exception occured", exc_info=True)
        log.fatal(e)

    finally:
        os.chdir(os.path.join(config.PROJECT_PATH, config.RESULTS_PATH))
        HTMLReporter.complete_html(html)
        log.info("Workflow Completed")
