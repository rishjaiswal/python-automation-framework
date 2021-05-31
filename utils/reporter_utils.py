from utils.logger_utils import get_logger

log = get_logger()


class HTMLReporter():

    def create_css():
        log.info("Inside create_css() method")
        css = '<style>'
        css += 'body{background - color: dark-grey;}'
        css += 'h1{border -width : 4px;}'
        css += 'p{font-size:20px;}'
        css += '</style>'
        log.info("Finish create_css() method")
        return css;

    def create_html():
        log.info("Inside create_html() method")
        html = '<html<head>' + '<head><body><h1> Automation Test Run Results</h1>'
        html += HTMLReporter.create_css()
        log.info("Complete create_html() method")
        return html

    def complete_html(html):
        log.info("Inside complete_html() method")
        html += "</tr><body></table>"
        html_path = open("automation_report.html", "w")
        html_path.write(html)
        log.info("Complete complete_html() method")
        html_path.close()

    def create_test_data(html, test_case_number, test_case_description, status):
        log.info("Inside create_test_data() method")
        if status == "PASS":
            html += '<tr><td>' + test_case_number + '</td><td>' + test_case_description + '</td><td><p style="color:blue">' + status + '</td></tr>'
        elif status == "FAIL":
            html += '<tr><td>' + test_case_number + '</td><td>' + test_case_description + '</td><td><p style="color:red">' + status + '</td></tr>'
        else:
            html += '<tr><td>' + test_case_number + '</td><td>' + test_case_description + '</td><td>' + status + '</td></tr>'
        log.info("Complete create_test_data() method")
        return html;

    def create_test_folder(html):
        log.info("Inside create_test_folder() method")
        html += '<table border ="1" style="width:50% ">'
        html += '<tr><th class ="grey" style="width:20px;">S.No</th><th class ="grey" style="width:100px;">Test Case Description</th><th class ="grey" style="width:60px;">Test Result</th></tr>'
        log.info("Complete create_test_folder() method")
        return html;
