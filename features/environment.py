import time
import warnings

import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options

from app.application import Application
from configuration.config import Datatest


def before_scenario(context, scenario):
    print("################")
    print("[ CONFIGURACION ] - Inicializando la configuracion del controlador")
    print("################")
    caps = None
    if Datatest.DEVICE.upper() == "FISICO":
        caps = Datatest.ANDROID_CONFIG_LOCAL
    else:
        caps = Datatest.ANDROID_CONFIG_EMU
    if caps is None:
        assert False, f"Error no hay data en los capabilities, el valor es: {caps}"

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        capabilities_options = UiAutomator2Options().load_capabilities(caps)
        context.driver = webdriver.Remote(command_executor=Datatest.URL, options=capabilities_options)
        context.driver.implicitly_wait(Datatest.IMPLICIT_WAIT)
        context.application = Application(context.driver)
    print("################")
    print("[ SCENARIO ] - " + scenario.name)
    print("################")


def after_scenario(context, scenario):

    if scenario.status == "failed":
        failed_step_name = None
        scenario_name = scenario.name
        for step in scenario.steps:
            if step.status == "failed":
                failed_step_name = step.name
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
        screenshot_name = f"{scenario_name}_{failed_step_name}_{current_time}.png"
        allure.attach(context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)
        context.driver.terminate_app("com.assistcard.assistcard.qa")
        print("################")
        print(f"[  DRIVER STATUS  ] - Limpiando y cerrando instancia del controlador debido a un error del scenario {scenario_name}")
        print("################")
        print("____________________________________________________________________________")
    elif scenario.status == "passed":
        print("----------------------")
        print(f"[  SCENARIO STATUS  ] - Prueba Exitosa (PASS): {scenario.name}")
        print("----------------------")
        context.driver.terminate_app("com.assistcard.assistcard.qa")
    context.driver.quit()

