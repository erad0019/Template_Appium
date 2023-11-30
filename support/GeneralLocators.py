from selenium.webdriver.common.by import By

from configuration.config import Datatest


class LocatorsInitialStepPage:
    # Localizadores por ruta HTML
    locatorButtonInitPage = (By.ID, f"{Datatest.PACKAGE_MYAC}:id/tv_onboarding__btncontinue")
    locatorButtonContinueModalNotificacionGPS = (By.ID, f"{Datatest.PACKAGE_MYAC}:id/dialog_btnAccept")
    locatorButtonPermission = (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    locatorIconDownloadPolicy = (By.XPATH, "//android.widget.Image[@resource-id='new-ac-logo']")
    locatorBtnContinuePermissionPrivacyPolicy = (By.ID, f"{Datatest.PACKAGE_MYAC}:id/dialog_btnAccept")
    locatorBtnAllowPermissionNative = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    locatorTextPolicyPrivacy = (By.XPATH, "//android.view.View[contains(@text, '1. Consideraciones generales')]")
    # Textos Para validar alertas o visualizaciones de resultados
    textValidateWelcome = "Te damos la bienvenida"
    textAlertPermission = "¿Quieres permitir que Assist Card-QA acceda a la ubicación de este dispositivo?"
    textValidateInitialStepsLogin = "Inicia sesión"
    textModalNotificacionGPS = "Permite que Assist Card envíe notificaciones y acceda a tu ubicación."
    textLocatorButtonLogin = "INICIAR CON USUARIO Y CONTRASEÑA"
    textValidatePageRegister = "Completa tus datos para poder avanzar."
    textValidatePageLogin = "Ingresa con correo y contraseña"
    textLocatorButtonRegister = "REGISTRARSE CON USUARIO Y CONTRASEÑA"
    textLocatorLinkPrivacyPolicy = "Presione aquí para ver nuestras políticas de privacidad"
    textValidateModalOfPermission = "Permite que Assist Card acceda a los archivos de tu dispositivo."
    textValidateNativeModalPermission = "¿Quieres permitir que Assist Card-QA acceda a las fotos y el contenido " \
                                        "multimedia del dispositivo?"

