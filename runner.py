from utils.logger_utils import get_logger

log = get_logger()

if __name__ == '__main__':
    log.info("Workflow Started")
    try:
        log.info("Workflow Execution In Progress")

    except Exception as e:
        log.fatal("Exception occured", exc_info=True)
        log.fatal(e)

    finally:
        log.info("Workflow Completed")
