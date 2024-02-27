import pathlib

import pytest

from sge_functions.sge_functions2 import sge_functions2
from py.xml import html
import os
from pathlib import Path

_SCREENSHOT_PATH = os.path.join(pathlib.Path(__file__).parent, "screenshots")
_TMP_FILE_PATH = os.path.join(pathlib.Path(__file__).parent, "tmp_file")

def pytest_configure(config):
    # to remove environment section
    config._metadata = None
    #para uso con archivos csv
    #sge_fun = SgeFunctions()
    sge_fun = sge_functions2()
    report_directory = sge_fun.create_report_directory()
    if not os.path.exists(report_directory):
        os.makedirs(report_directory)
    if not os.path.exists(os.path.join(_SCREENSHOT_PATH)):
        os.makedirs(_SCREENSHOT_PATH)


    config.option.htmlpath = f"{report_directory}SGE_Carga_de_datos_Test_Report.html"
    config.option.imagepath = report_directory


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    print(str(item))
    sge_fun = sge_functions2()
    html_path = str(item.config.option.imagepath)

    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    #sge_fun.terminate_sge_session()

    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        # always add url to images_report
        xfail = hasattr(report, "wasxfail")
        # if (images_report.skipped and xfail) or (images_report.failed and not xfail):
        # only add additional html on failure
        message = "_Error" if report.failed else "_Successful"
        # img_name = sge_fun.obtener_fecha() + message + ".png"
        img_name = item.name + message + ".png"

        new_path_img = sge_fun.move_to_report_dir(img_name, html_path)
        main_dir = str(Path(new_path_img).resolve().parents[1])
        extra.append(pytest_html.extras.html("additional html" + f"{main_dir}/{new_path_img}"))
        insert_img = str(
            f'<div class="image"><a class="image" href="{img_name}" target="_blank"><img src="{img_name}"></a></div>')
        extra.append(pytest_html.extras.html(insert_img))
        report.extra = extra


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(
        [html.img(src="../../image_files/logo_oreilly.png", style="right:8%; height:240px; top:0; position:fixed;")])


# con set
def pytest_html_report_title(report):
    test_files = set()
    for result in report.results:
        """
        Get file from test result information: https://github.com/pytest-dev/pytest-html/blob/master/src/pytest_html/result.py
        """
        tmp = result.test_id.split("::") if result else "MISSING TEST ID"
        test_files.add(tuple(tmp))
        #usando el set
    #test_files_list = str(test_files).split(",")
    """
    test_files_list[0] : contains the python file name exucuted i.e. test_create_invoice_credit_massive_order_csv.py
    test_files_list[1] : contains the class name of the py file executed i.e SgeUnittest
    test_files_list[2] : contains the test name of py file executed i.e test_create_invoice_mostrador_simple_order
    """
    test_files_list = str(test_files).split(",")
    #print("Len de test_files_list")
    #print(str(len(test_files_list)))
    titulo = test_files_list[0].replace("{(", "").replace("'", "").replace(")}", "").replace("_", " ")
    report.title = f"SGE Purchase Order Report: {titulo}"
