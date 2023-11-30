

from support.GeneralLocators import LocatorsInitialStepPage as lisp

from support.BaseActions import BaseActions

# Variable de tiempo
t = 0.5


class InitialStepsPage(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    """
    TODOS DE GESTOS Y ACCIONES
    """

    def ClickOnButtonContinueSetupPage(self):


        BaseActions.clickOnElementBySelector(self, lisp.locatorButtonInitPage[0], lisp.locatorButtonInitPage[1], t)

    def ClickOnButtonContinueOfModal(self):
        BaseActions.clickOnElementBySelector(self, lisp.locatorButtonContinueModalNotificacionGPS[0],
                                             lisp.locatorButtonContinueModalNotificacionGPS[1], t)

    def ClickOnButtonAccepPermission(self):
        BaseActions.clickOnElementBySelector(self, lisp.locatorButtonPermission[0], lisp.locatorButtonPermission[1], t)

    def ClickOnButtonLoginWithCredential(self):
        BaseActions.clickOnElementByText(self, lisp.textLocatorButtonLogin, t)

    def ClickOnButtonRegisterUser(self):
        BaseActions.clickOnElementByText(self, lisp.textLocatorButtonRegister, t)

    def ClickOnLinkPrivacyPolicy(self):
        BaseActions.clickOnElementByText(self, lisp.textLocatorLinkPrivacyPolicy, t)

    def ClickOnIconDonwloadProvacyPolicy(self):
        BaseActions.clickOnElementBySelector(self, lisp.locatorIconDownloadPolicy[0], lisp.locatorIconDownloadPolicy[1], t)

    def ClickOnBtnContinueInModalPermissionPrivacyPolicy(self):
        BaseActions.clickOnElementBySelector(self, lisp.locatorBtnContinuePermissionPrivacyPolicy[0],
                                             lisp.locatorBtnContinuePermissionPrivacyPolicy[1], t)

    def ClickBtnAllowPermissionNative(self):
        BaseActions.clickOnElementBySelector(self, lisp.locatorBtnAllowPermissionNative[0], lisp.locatorBtnAllowPermissionNative[1], t)

    """
    VALIDACIONES
    """

    def ValidatePageLoginInitialSteps(self):
        val = BaseActions.findElementIsVisibleByText(self, lisp.textValidateInitialStepsLogin)
        if val is True:
            BaseActions.screenshot(self, "Pagina de login mostrada exitosamente")
        else:
            assert False, "La pagina de login no se mostró"
    def ValidateMessageOfPageInitial(self):
        val = BaseActions.findElementIsVisibleByText(self, lisp.textValidateWelcome)
        if val is True:
            BaseActions.screenshot(self, "Mensaje de bienvenida confirmada")
        else:
            assert False, "No se mostró mensaje de bienvenida"
    def ValidateAlertOfPermission(self):
        val = BaseActions.findElementIsVisibleByText(self, lisp.textAlertPermission)
        if val is True:
            BaseActions.screenshot(self, "modal permisos de ubicación")
        else:
            assert False, "No se mostró la modal de permisos de ubicacion"
    def ValidateModalNotificationAndGPS(self):
        val = BaseActions.findElementIsVisibleByText(self, lisp.textModalNotificacionGPS)
        if val is True:
            BaseActions.screenshot(self, "Modal de permisos para notificaciones y GPS")
        else:
            assert False, "No se mostró modal de permisos de notificación y GPS"
    def ValidatePageRegister(self):
        val = BaseActions.findElementIsVisibleByText(self, lisp.textValidatePageRegister)
        if val is True:
            BaseActions.screenshot(self, "Redireccción a Pagina de registro confirmada")
        else:
            assert False, "No se redireccionó a la pagina de registro"
    def ValidatePageLogin(self):
        val = BaseActions.findElementIsVisibleByText(self, lisp.textValidatePageLogin)
        if val is True:
            BaseActions.screenshot(self, "Redireccion a Pagina de login confirmada")
        else:
            assert False, "No se redirecciono a la pagina de login"
    def ValidatePageOfPrivacyPolicy(self):

        val = BaseActions.findElementIsVisibleBySelector(self, lisp.locatorIconDownloadPolicy[0], lisp.locatorIconDownloadPolicy[1])
        val2 = BaseActions.findElementIsVisibleBySelector(self, lisp.locatorTextPolicyPrivacy[0], lisp.locatorTextPolicyPrivacy[1])
        if val and val2:
            BaseActions.screenshot(self, "Se mostro pagina de politicas de privacidad correctamente")
        else:
            assert False, "No se mostro contenido de politicas de privacidad"

    def ValidateModalOfPermissionPrinvacyPolicy(self):
        val = BaseActions.findElementIsVisibleByText(self, lisp.textValidateModalOfPermission)
        if val:
            BaseActions.screenshot(self, "Modal de permisos de almacenamiento")
        else:
            assert False, "Error la modal de permiso de almacenamiento no se mostro"

    def ValidateModalPermissionNativePrivacyPolicy(self):
        val = BaseActions.findElementIsVisibleByText(self, lisp.textValidateNativeModalPermission)
        if val:
            BaseActions.screenshot(self, "Modal nativa de permisos de almacenamiento")
        else:
            assert False, "Error no se mostro la segunda modal de permisos nativos para almacenamiento"

    def ValidateToastMessageDownloadPrivacyPolicy(self, textValidateToast):
        val = BaseActions.validateToastWithTextVisible(self, textValidateToast)
        if val is True:
            BaseActions.screenshot(self, f"Validado el toast con el mensaje: {textValidateToast}")
        else:
            assert False, f"No se mostro el Toast con el mensaje {textValidateToast}"