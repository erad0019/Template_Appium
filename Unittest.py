import subprocess
import time
import unittest
import warnings
from datetime import datetime

from appium.options.android import UiAutomator2Options

from support.GeneralLocators import LocatorsMyAccountPage as lap
import numpy
from selenium.webdriver.common.by import By
from appium import webdriver

from app.application import Application
from configuration.config import Datatest

from support.BaseActions import BaseActions


t = 1


class MyTestChats(unittest.TestCase):
    def setUp(self):
        # Inicializacion de Manejador Appium
        caps = Datatest.ANDROID_CONFIG_EMU

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            capabilities_options = UiAutomator2Options().load_capabilities(caps)
            self.driver = webdriver.Remote(command_executor=Datatest.URL, options=capabilities_options)
            # self.driver = webdriver.Remote(Datatest.URL, caps)
            self.driver.implicitly_wait(Datatest.IMPLICIT_WAIT)

    def test_act01(self):
        # Omitir 3 veces una misma actividad. en la cuarta iteracion debera mostrar una
        # alerta indicando que se llego al limite de omisiones por dia

        Email = "epidata1@yopmail.com"
        Password = "Tester23."
        Name = "UNA ASISTENCIA"
        LastName = "USER"
        DayAssitence = "26"
        MonthAssistence = "Septiembre"
        YearAssistence = "2023"
        Description = "Esto es una descripcion"


        locatorAddDocumentID = (By.ID, "com.assistcard.assistcard.qa:id/inputfiles_add_button")
        locatorObligatoryInput = (By.ID, "com.assistcard.assistcard.qa:id/inputfiles_text_mandatory")
        locatorIconGallery = (By.ID, "com.assistcard.assistcard.qa:id/dialog_inputfile_btn_galeria")
        locatorIconCamera = (By.ID, "com.assistcard.assistcard.qa:id/dialog_inputfile_btn_camera")
        locatorIconPDF = (By.ID, "com.assistcard.assistcard.qa:id/dialog_inputfile_btn_document")
        locatorPermissionLocalStorage = (By.ID, "com.assistcard.assistcard.qa:id/dialog_btnAccept")
        locatorSecondPermissionLocalStorage = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
        locatorSearchDownloads = (By.XPATH, "//android.widget.ImageButton[@content-desc='Mostrar raíces']")
        textLocatorButtonDownloads = (
            By.XPATH, "//android.widget.TextView[@resource-id='android:id/title' and @text='Descargas']")
        locatorIMGGallery = (By.XPATH, "//android.widget.LinearLayout[@content-desc='IMG_20230906_153453.jpg, 1.78 MB, "
                                       "27 sep.']/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget"
                                       ".ImageView[1]")
        # "com.google.android.documentsui:id/icon_thumb"   Localizador por ID para imagen
        locatorAddSuccessDocument = (By.ID, "com.assistcard.assistcard.qa:id/inputfiles_adjuntos")
        locatorPermissionCameraAccess = (
            By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        locatorCapturePhoto = (By.ID, "com.android.camera2:id/shutter_button")
        locatorButtonSaveCaputePhoto = (By.ID, "com.android.camera2:id/done_button")
        locatorDocumentOfFile = (
            By.XPATH, "//android.widget.TextView[@resource-id='android:id/title' and @text='Documento.pdf']")

        # Localizadores por clase android.widget.TextView
        locator_Element_MyAccount = (By.CLASS_NAME, "android.widget.TextView")

        # Textos Para validar alertas o visualizaciones de resultados
        txtValidatePagMyAccount = ["Datos personales", "Grupo de viaje", "Mi historial"]
        textValidatePageChangePassword = "Cambiar contraseña"
        textToScrollDownInMyAccount = "BORRAR CUENTA"
        textValidatePageAssistance = "Elige la asistencia por la\nque solicitas el reintegro"
        textValidatePageSelectTypeReimbursement = "Debes presentar una solicitud por\ncada tipo de reintegro."

        # Cargar documentos local storage
        uri_destino = "/storage/emulated/0/Download"
        path_local_one = Datatest.PATH_IMG_PDF + "\Documento.pdf"
        path_local_two = Datatest.PATH_IMG_PDF + "\IMG_20230906_153453.jpg"

        # packageAndActivity = ("org.mozilla.firefox", "org.mozilla.firefox.App")

        second_app_package = 'org.mozilla.firefox'  # Paquete de la segunda aplicación
        second_app_activity = 'org.mozilla.firefox.App'  # Actividad principal de la segunda aplicación



        fa = BaseActions(self.driver)
        app = Application(self.driver)
        app.InitialStepsPage.ValidateMessageOfPageInitial()
        app.InitialStepsPage.ClickOnButtonContinueSetupPage()
        app.InitialStepsPage.ValidateModalNotificationAndGPS()
        app.InitialStepsPage.ClickOnButtonContinueOfModal()
        app.InitialStepsPage.ValidateAlertOfPermission()
        app.InitialStepsPage.ClickOnButtonAccepPermission()
        app.InitialStepsPage.ValidatePageLoginInitialSteps()
        fa.installApk(Datatest.PATH_APK_BROWSER)
        # fa.switchApp(packageAndActivity[0], packageAndActivity[1])
        # Reiniciar app de fabrica borrando data cache
        subprocess.run(['adb', 'shell', 'pm', 'clear', second_app_package])
        print("Se reinicio la aplicacion correctamente")
        # Configura las nuevas capacidades para la aplicación objetivo
        desired_caps = {
            'appPackage': second_app_package,
            'appActivity': second_app_activity
        }

        self.driver.execute_script('mobile: startActivity', {'package': second_app_package, 'activity': second_app_activity})

        #
        # # Usa la extensión "mobile: startActivity" para iniciar la aplicación B
        # self.driver.execute_script('mobile: startActivity', desired_caps_B)
        # # Cambia a la aplicación objetiva utilizando start_activity
        # # self.driver.execute_script('mobile: startActivity', {'appium:appPackage': 'org.mozilla.firefox', 'appium:appActivity': 'org.mozilla.firefox.App'})
        # self.driver.start_activity(packageAndActivity[0], packageAndActivity[1])
        # print(f"Se cambio a la aplicacion: {packageAndActivity[0]}, de forma correcta")
        # self.driver.execute_script()
        # self.driver.switch_to.context()
        # self.driver.st

        # app.InitialStepsPage.ClickOnButtonLoginWithCredential()
        # app.LoginPage.InsertEmailCredential(Email)
        # app.LoginPage.InsertPasswordCredential(Password)
        # app.LoginPage.ClickButtonStartLogin()
        #
        # app.HomePage.ClickOnModuleMyAccount()
        # app.MyAccountPage.ClickOnMyHistory()
        # app.MyAccountPage.ValidatePageMyHistory()
        # app.MyAccountPage.ClickBtnAssitance()
        # app.MyAccountPage.ValidatePageAssistaceByUserTitular(Name, LastName)
        #
        # status_ongoing = fa.findListOfElementsBySelector(lap.locatorStatusAssistance[0],
        #                                                           lap.locatorStatusAssistance[1])
        # btn_see_detail = fa.findListOfElementsBySelector(lap.locatorBtnSeeDetailsOfAssistance[0],
        #                                                           lap.locatorBtnSeeDetailsOfAssistance[1])
        # # Extraer el texto de cada elemento y guardarlos en una lista
        # text_list = [cant.text for cant in status_ongoing]
        # print(text_list)
        # # Buscar la posición del elemento que contiene el texto "En curso"
        # position_of_ongoing = None
        # for index, text in enumerate(text_list):
        #     if 'En curso' in text:
        #         position_of_ongoing = index
        #         break  # Si lo encontramos, podemos salir del bucle
        # if position_of_ongoing is not None:
        #     print(f'La asistencia "En curso" se encuentra en la posición {position_of_ongoing}')
        # else:
        #     assert False, "No hay asistencias en curso"
        # # Hacer click en el boton ver detalle donde se visualizo el status en curso
        # btn_see_detail[position_of_ongoing].click()
        # time.sleep(10)

    # def AddDocumentIdentity(self):
    #     try:
    #         obligatory = BaseActions.findListOfElementsBySelector(self, locatorObligatoryInput[0], locatorObligatoryInput[1])
    #         btn_add_document = BaseActions.findListOfElementsBySelector(self, locatorAddDocumentID[0], locatorAddDocumentID[1])
    #         number_doc_obli = len(obligatory)
    #         for doc in range(0, number_doc_obli):
    #             for i in range(0, 3):
    #                 if i < 1:
    #                     for a in range(0, 2):
    #                         btn_add_document[doc].click()
    #                     BaseActions.Tiempo(t)
    #                     # Hacer click en opcion galeria
    #                     BaseActions.clickOnElementBySelector(self, locatorIconGallery[0], locatorIconGallery[1], t)
    #                     is_visible = BaseActions.findElementIsDisplayed(self, locatorPermissionLocalStorage[0],
    #                                                                     locatorPermissionLocalStorage[1])
    #                     if is_visible:
    #                         # Conceder permisos por primera vez hacia local storage
    #                         BaseActions.clickOnElementBySelector(self, locatorPermissionLocalStorage[0],
    #                                                              locatorPermissionLocalStorage[1], t)
    #                         BaseActions.clickOnElementBySelector(self, locatorSecondPermissionLocalStorage[0],
    #                                                              locatorSecondPermissionLocalStorage[1], t)
    #                     # Acceder a descargas en local storage
    #                     BaseActions.clickOnElementBySelector(self, locatorSearchDownloads[0], locatorSearchDownloads[1],
    #                                                          t)
    #                     BaseActions.clickOnElementBySelector(self, textLocatorButtonDownloads[0],
    #                                                          textLocatorButtonDownloads[1], t)
    #                     # Seleccionar IMG de Descargas
    #                     BaseActions.clickOnElementBySelector(self, locatorIMGGallery[0], locatorIMGGallery[1], t)
    #                     # Verificar si se muestra archivo cargado
    #                     adjunto = BaseActions.findListOfElementsBySelector(self, locatorAddSuccessDocument[0],
    #                                                                        locatorAddSuccessDocument[1])
    #                     # Extraer el texto de cada elemento y guardarlos en una lista
    #                     text_list = [cant.text for cant in adjunto]
    #                     # Validar que se cargaron la cantidad de documentos correctamente
    #                     if text_list[doc] == "1 Adjuntos":
    #                         BaseActions.screenshot(self,
    #                             f"Archivo numero {i}, se adjunto correctamente para opcion Galeria")
    #                     else:
    #                         assert False, f"Error no se cargo el archivo adjunto numero {i} para la opcion galeria"
    #                 elif i == 1:
    #                     btn_add_document[doc].click()
    #                     BaseActions.Tiempo(t)
    #                     # Hacer click en opcion Camara
    #                     BaseActions.clickOnElementBySelector(self, locatorIconCamera[0], locatorIconCamera[1], t)
    #                     # Conceder permisos por primera vez hacia local storage
    #                     is_visible = BaseActions.findElementIsDisplayed(self, locatorPermissionLocalStorage[0],
    #                                                                     locatorPermissionLocalStorage[1])
    #                     if is_visible:
    #                         # Conceder permisos por primera vez hacia local storage
    #                         BaseActions.clickOnElementBySelector(self, locatorPermissionLocalStorage[0],
    #                                                              locatorPermissionLocalStorage[1], t)
    #                         BaseActions.clickOnElementBySelector(self, locatorPermissionCameraAccess[0],
    #                                                              locatorPermissionCameraAccess[1], t)
    #
    #                     # Acceder a camara y capturar foto
    #                     BaseActions.clickOnElementBySelector(self, locatorCapturePhoto[0], locatorCapturePhoto[1],
    #                                                          t)
    #                     # Guardar imagen capturada por camara
    #                     BaseActions.clickOnElementBySelector(self, locatorButtonSaveCaputePhoto[0],
    #                                                          locatorButtonSaveCaputePhoto[1],
    #                                                          t)
    #                     # Verificar si se muestra archivo cargado
    #                     adjunto = BaseActions.findListOfElementsBySelector(self, locatorAddSuccessDocument[0],
    #                                                                        locatorAddSuccessDocument[1])
    #                     # Extraer el texto de cada elemento y guardarlos en una lista
    #                     text_list = [cant.text for cant in adjunto]
    #                     # Validar que se cargo el segundo documento correctamente
    #                     if text_list[doc] == "2 Adjuntos":
    #                         BaseActions.screenshot(self,
    #                             f"Archivo numero {i}, se adjunto correctamente para opcion Galeria")
    #                     else:
    #                         assert False, f"Error no se cargo el archivo adjunto numero {i} para la opcion galeria"
    #                 else:
    #                     btn_add_document[doc].click()
    #                     BaseActions.Tiempo(t)
    #                     # Hacer click en opcion Camara
    #                     BaseActions.clickOnElementBySelector(self, locatorIconPDF[0], locatorIconPDF[1], t)
    #                     # Conceder permisos por primera vez hacia local storage
    #                     is_visible = BaseActions.findElementIsDisplayed(self, locatorPermissionLocalStorage[0],
    #                                                                     locatorPermissionLocalStorage[1])
    #                     if is_visible:
    #                         # Conceder permisos por primera vez hacia local storage
    #                         BaseActions.clickOnElementBySelector(self, locatorPermissionLocalStorage[0],
    #                                                              locatorPermissionLocalStorage[1], t)
    #                         BaseActions.clickOnElementBySelector(self, locatorSecondPermissionLocalStorage[0],
    #                                                              locatorSecondPermissionLocalStorage[1], t)
    #
    #                     # Seleccionar Documento pdf
    #                     BaseActions.clickOnElementBySelector(self, locatorDocumentOfFile[0], locatorDocumentOfFile[1], t)
    #                     # Verificar si se muestra archivo cargado
    #                     adjunto = BaseActions.findListOfElementsBySelector(self, locatorAddSuccessDocument[0],
    #                                                                        locatorAddSuccessDocument[1])
    #                     # Extraer el texto de cada elemento y guardarlos en una lista
    #                     text_list = [cant.text for cant in adjunto]
    #                     # Validar que se cargo el segundo documento correctamente
    #                     if text_list[doc] == "3 Adjuntos":
    #                         BaseActions.screenshot(self,
    #                             f"Archivo numero {i}, se adjunto correctamente para opcion Galeria")
    #                     else:
    #                         assert False, f"Error no se cargo el archivo adjunto numero {i} para la opcion galeria"
    #     except Exception:
    #         print(" NO HAY CAMPOS OBLIGATORIOS")
    #         btn_add_document = BaseActions.findListOfElementsBySelector(self, locatorAddDocumentID[0],
    #                                                                     locatorAddDocumentID[1])
    #         for i in range(0, 3):
    #             if i < 1:
    #                 for a in range(0, 2):
    #                     btn_add_document[0].click()
    #                 BaseActions.Tiempo(t)
    #                 # Hacer click en opcion galeria
    #                 BaseActions.clickOnElementBySelector(self, locatorIconGallery[0], locatorIconGallery[1], t)
    #                 is_visible = BaseActions.findElementIsDisplayed(self, locatorPermissionLocalStorage[0],
    #                                                                 locatorPermissionLocalStorage[1])
    #                 if is_visible:
    #                     # Conceder permisos por primera vez hacia local storage
    #                     BaseActions.clickOnElementBySelector(self, locatorPermissionLocalStorage[0],
    #                                                          locatorPermissionLocalStorage[1], t)
    #                     BaseActions.clickOnElementBySelector(self, locatorSecondPermissionLocalStorage[0],
    #                                                          locatorSecondPermissionLocalStorage[1], t)
    #                 # Acceder a descargas en local storage
    #                 BaseActions.clickOnElementBySelector(self, locatorSearchDownloads[0], locatorSearchDownloads[1],
    #                                                      t)
    #                 BaseActions.clickOnElementBySelector(self, textLocatorButtonDownloads[0], textLocatorButtonDownloads[1],
    #                                                      t)
    #                 # Seleccionar IMG de Descargas
    #                 BaseActions.clickOnElementBySelector(self, locatorIMGGallery[0], locatorIMGGallery[1], t)
    #                 # Verificar si se muestra archivo cargado
    #                 adjunto = BaseActions.findListOfElementsBySelector(self, locatorAddSuccessDocument[0],
    #                                                                    locatorAddSuccessDocument[1])
    #                 # Extraer el texto de cada elemento y guardarlos en una lista
    #                 text_list = [cant.text for cant in adjunto]
    #                 # Validar que se cargaron la cantidad de documentos correctamente
    #                 if text_list[0] == "1 Adjuntos":
    #                     BaseActions.screenshot(self,
    #                         f"Archivo numero {i}, se adjunto correctamente para opcion Galeria")
    #                 else:
    #                     assert False, f"Error no se cargo el archivo adjunto numero {i} para la opcion galeria"
    #             elif i == 1:
    #                 btn_add_document[0].click()
    #                 BaseActions.Tiempo(t)
    #                 # Hacer click en opcion Camara
    #                 BaseActions.clickOnElementBySelector(self, locatorIconCamera[0], locatorIconCamera[1], t)
    #                 # Conceder permisos por primera vez hacia local storage
    #                 is_visible = BaseActions.findElementIsDisplayed(self, locatorPermissionLocalStorage[0],
    #                                                        locatorPermissionLocalStorage[1])
    #                 if is_visible:
    #                     # Conceder permisos por primera vez hacia local storage
    #                     BaseActions.clickOnElementBySelector(self, locatorPermissionLocalStorage[0],
    #                                                          locatorPermissionLocalStorage[1], t)
    #                     BaseActions.clickOnElementBySelector(self, locatorPermissionCameraAccess[0],
    #                                                          locatorPermissionCameraAccess[1], t)
    #
    #                 # Acceder a camara y capturar foto
    #                 BaseActions.clickOnElementBySelector(self, locatorCapturePhoto[0], locatorCapturePhoto[1],
    #                                                      t)
    #                 # Guardar imagen capturada por camara
    #                 BaseActions.clickOnElementBySelector(self, locatorButtonSaveCaputePhoto[0],
    #                                                      locatorButtonSaveCaputePhoto[1],
    #                                                      t)
    #                 # Verificar si se muestra archivo cargado
    #                 adjunto = BaseActions.findListOfElementsBySelector(self, locatorAddSuccessDocument[0],
    #                                                                    locatorAddSuccessDocument[1])
    #                 # Extraer el texto de cada elemento y guardarlos en una lista
    #                 text_list = [cant.text for cant in adjunto]
    #                 # Validar que se cargo el segundo documento correctamente
    #                 if text_list[0] == "2 Adjuntos":
    #                     BaseActions.screenshot(self,
    #                         f"Archivo numero {i}, se adjunto correctamente para opcion Galeria")
    #                 else:
    #                     assert False, f"Error no se cargo el archivo adjunto numero {i} para la opcion galeria"
    #             else:
    #                 btn_add_document[0].click()
    #                 BaseActions.Tiempo(t)
    #                 # Hacer click en opcion Camara
    #                 BaseActions.clickOnElementBySelector(self, locatorIconPDF[0], locatorIconPDF[1], t)
    #                 # Conceder permisos por primera vez hacia local storage
    #                 is_visible = BaseActions.findElementIsDisplayed(self, locatorPermissionLocalStorage[0],
    #                                                                 locatorPermissionLocalStorage[1])
    #                 if is_visible:
    #                     # Conceder permisos por primera vez hacia local storage
    #                     BaseActions.clickOnElementBySelector(self, locatorPermissionLocalStorage[0],
    #                                                          locatorPermissionLocalStorage[1], t)
    #                     BaseActions.clickOnElementBySelector(self, locatorPermissionCameraAccess[0],
    #                                                          locatorPermissionCameraAccess[1], t)
    #
    #                 # Seleccionar Documento pdf
    #                 BaseActions.clickOnElementBySelector(self, locatorDocumentOfFile[0], locatorDocumentOfFile[1], t)
    #                 # Verificar si se muestra archivo cargado
    #                 adjunto = BaseActions.findListOfElementsBySelector(self, locatorAddSuccessDocument[0],
    #                                                                    locatorAddSuccessDocument[1])
    #                 # Extraer el texto de cada elemento y guardarlos en una lista
    #                 text_list = [cant.text for cant in adjunto]
    #                 # Validar que se cargo el segundo documento correctamente
    #                 if text_list[0] == "3 Adjuntos":
    #                     BaseActions.screenshot(self,
    #                         f"Archivo numero {i}, se adjunto correctamente para opcion Galeria")
    #                 else:
    #                     assert False, f"Error no se cargo el archivo adjunto numero {i} para la opcion galeria"
    # def test_act02(self):
    #     # Omitir 3 veces una misma actividad. en la cuarta iteracion debera mostrar una
    #     # alerta indicando que se llego al limite de omisiones por dia
    #     driver = self.driver
    #     fa = faApp(driver)
    #
    #
    #     headers = RequestMethod.header_auth()
    #     LoginFunctions.SetUpSecretDevMode(driver)
    #     time.sleep(1)
    #     app_package = "com.android.chrome"
    #     app_activity = "com.google.android.apps.chrome.Main"
    #     fa.switchApp(app_package, app_activity)
    #     fa.openHomeInChrome()
    #     fa.send_Text_In_Input_By_Selector(By.ID, "com.android.chrome:id/url_bar", "https://yopmail.com/es/", 5)
    #     driver.press_keycode(66)
    #     time.sleep(5)
    #     fa.send_Text_In_Input_By_Selector(By.XPATH, "//android.widget.EditText[@resource-id='login']", "datepicker@yopmail.com", 5)
    #     driver.press_keycode(66)
    #     fa.findEmailVerification()
    #
    #
    #     fa.scrollAndFindVisibleElementInClassicHomeByText('Ver Programas')   #By.XPATH, "//android.widget.TextView[contains(@text, 'Ver Programas')]")
    #     fa.clickOnElementByText("Ver Programas", 0.5)
    #     fa.findElementIsVisibleByText("Programas y desafíos")
    #     fa.clickOnInitProgram("Estres", 0.5)
    #     fa.findElementIsVisibleByText("Estres")
    #     fa.findElementIsVisibleByText("Descripción")
    #     fa.clickOnElementByText("Aceptar", 0.5)
    #     fa.findElementIsVisibleByText("Módulos")
    #     fa.findElementIsVisibleByText("Canaliza tu Estres")
    #     for i in range (1, 3):
    #         fa.backPage()
    #     fa.scrollAndFindVisibleElementInClassicHomeByText('Estres')
    #

    # def test_act03(self):
    #
    #     filesheet = Datatest.DEMO
    #
    #     # Cargar el archivo Excel
    #     archivo = openpyxl.load_workbook(filesheet)
    #
    #     # Obtener las hojas
    #     hoja1 = archivo['Hoja1'] # Quien envia
    #     hoja2 = archivo['Hoja2'] # Quien recibe
    #
    #     for o in range(2, 3):  # Itera por fila
    #         # Ingresa una fila vacía en la posicion 1 para el archivo que recibe la data
    #         hoja2.insert_rows(1)
    #         for j in range(1, 11):  # Itera por columnas
    #             # copia el dato de la iteracion de la columna indicada por J para
    #             # la fila indicada por O para el archivo que envia la data
    #             c = hoja1.cell(row=o, column=j)
    #             # Pega en la misma columna en el archivo que recibe la data,
    #             # la información que copio del archivo que envia la data
    #             hoja2.cell(row=o, column=j).value = c.value
    #
    #     # Eliminar los datos copiados de la hoja 1
    #     hoja1.delete_rows(2)
    #
    #     # Guardar los cambios en el archivo
    #     archivo.save(filesheet)
    #

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestChats)
    unittest.TextTestRunner(verbosity=2).run(suite)
