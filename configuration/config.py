import os
class Datatest:
    URL = "http://localhost:4723/wd/hub"
    IMPLICIT_WAIT = 10
    EMULADOR_ID = "emulator-5554"
    # Device define: si es Dispositivo fisico o si es emulador, debe escribirse los comandos = (emulador , fisico)
    DEVICE = "emulador"
    # Env define: el entorno de pruebas si es produccion, pre-produccion o QA, debe escribirse los comandos = (pro, pre, qa)
    ENV = "qa"

    # Package y Activity de la aplicacion a testear
    if ENV.upper() == "QA":
        PACKAGE_MYAC = "com.assistcard.assistcard.qa"
    elif ENV.upper() == "PRE":
        PACKAGE_MYAC = "com.assistcard.assistcard.pre"
    else:
        PACKAGE_MYAC = "com.assistcard.assistcard"

    ACTIVITY_MYAC = "com.assistcard.assistcard.preapp.AtvSplash"
    # Rutas para acceder a la BD
    PATH_BD = os.path.abspath("resources/BD.xlsx")

    # Ruta para apk de navegador
    PATH_APK_BROWSER = os.path.abspath("resources/browser.apk")

    # Ruta para apk Assist Card
    PATH_APK_MYAC = os.path.abspath("resources/app.apk")

    # Ruta para acceder a imagenes y archivos PDF
    PATH_IMG_PDF = os.path.abspath("resources/")

    # URL de proveedor de correos temporales
    MAIL_PROVIDER = "https://yopmail.com/es/"

    ##################### CONFIGURACION DE CAPABILITIES ########################################


    # Configuración para ejecutar pruebas en dispositivos fisico Android
    ANDROID_CONFIG_LOCAL = {
        "platformName": "Android",
        "appium:platformVersion": "12",
        "appium:deviceName": "lancelot",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": f"{PACKAGE_MYAC}",
        "appium:appActivity": f"{ACTIVITY_MYAC}",
        "app": f"{PATH_APK_MYAC}",
        "appium:grantPermissions": "true",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "resetKeyboard": True
    }
    # Configuración para ejecutar pruebas en dispositivos emulados Android
    ANDROID_CONFIG_EMU = {
        "platformName": "Android",
        "appium:platformVersion": "12",
        "appium:deviceName": "emulator64_x86_64_arm64",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": f"{PACKAGE_MYAC}",
        "appium:appActivity": f"{ACTIVITY_MYAC}",
        "app": f"{PATH_APK_MYAC}",
        "appium:grantPermissions": "true",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "resetKeyboard": True
    }
















































































