import datetime
import subprocess
import time

import allure
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
    WebDriverException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration.config import Datatest


class BaseActions:

    def __init__(self, driver):
        self.driver = driver
        global act
        act = ActionChains(driver)

    @staticmethod
    def Tiempo(tie):
        time.sleep(tie)

    ######################### ACTION CHAINS #######################################################################
    def clickAction(self, by_tipo: By, selector: str, tiempo: float):
        """
        Hacer click sobre un elemento con actions chains

        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta del elemento donde se desea ingresar el texto.
        :param tiempo: Tiempo de espera luego que termina la ejecucion de la funcion.
        :return: Accion donde se simula el click sobre un elemento con el mouse
        """

        try:
            val = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            act.click(val).perform()
            BaseActions.Tiempo(tiempo)
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def key_Up_Key_Down(self, by_tipo: By, selector: str, tecla: Keys, tiempo: float):
        """
        Hacer click sobre un elemento, luego de haber realizado focus
        en el elemento se procede a pulsar una tecla del keyboard

        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta del elemento donde se desea ingresar el texto.
        :param tiempo: Tiempo de espera luego que termina la ejecucion de la funcion.
        :param tecla: Valor de tipo Keys que simula el uso de una tecla del keyboard.
        :return: Accion que simula la interaccion de un usuario al marcar sobre un elemento y luego pulsar uan tecla.
        """

        try:
            val = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            act.click(val).perform()
            act.key_down(tecla).key_up(tecla).perform()
            BaseActions.Tiempo(tiempo)
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def drag_Drop_To_Element(self, by_tipo_Initial, selector_initial, by_tipo_final, selector_final):
        """
        Accion que permite mover un elemento hacia la posicion donde esta ubicado un segundo elemento

        :param selector_final: Ruta del elemento donde se desea mover el primer localizador.
        :param by_tipo_final: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector_initial: Ruta del elemento que se desea desplazar hacia otra posicion.
        :param by_tipo_Initial: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
       """
        try:
            val = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((by_tipo_Initial, selector_initial)))
            val2 = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((by_tipo_final, selector_final)))
            act.drag_and_drop(val, val2).perform()
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaban los " \
                          f"elementos\n{selector_initial} y {selector_final}\n El Error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontraron los elementos " \
                          f"{selector_initial} y {selector_final}\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con los elementos " \
                          f"{selector_initial} y {selector_final}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def drag_Drop_To_Position(self, by_tipo: By, selector: str, X, Y):
        """
        Metodo para poder mover un elemento hacia una posicion en el plano x, y.
        :param selector: Ruta del elemento donde se desea mover segun las coordenadas indicadas.
        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param X: posicion en el eje horizontal.
        :param Y: posicion en el eje vertical.

        """
        try:
            val = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            act.drag_and_drop_by_offset(val, X, Y).perform()
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    ################################# TAP AND GESTURES ON SCREEN #################################################

    def tap_Screen(self, x, y, durationMiliSeconds):
        """
        Funcion que permite realizar un tap sobre la pantalla en un plano X e Y por un periodo de tiempo determinado.
        :param x: Ubicación en el plano X.
        :param y: Ubicación en el plano Y.
        :param durationMiliSeconds: Colocar duracion milisegundos el cual durara en hacer click en pantalla.
        """
        try:

            self.driver.execute_script('mobile: longClickGesture', {'x': x, 'y': y, 'duration': durationMiliSeconds})
            print(f"Se hizo click en las coordenadas indicadas {x} y {y}")
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se hacia tap en las coordenadas " \
                          f": X: {x} ,  Y: {y}\n El Error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def backPage(self):
        """
        Funcion para realizar accion de volver a la pagina anterior
        """
        try:
            self.driver.back()
            print("Se hizo click al boton regresar correctamente")
        except Exception as ex:
            assert False, f"No se logro retroceder a la pantalla anterior\nError: {ex}"

    def restartApk(self):
        """
        Action que permite restablecer de fabrica una aplicacion
        """
        try:
            self.driver.reset()
            print("Se Reinicio el app correctamente")
        except Exception as ex:
            assert False, f"No se logro reiniciar el app\nError: {ex}"

    def installApk(self, Path_Apk):
        """
        Funcion qu epermite instalar una app
        :param Path_Apk: ruta de la apk para ser instalada
        """
        try:
            self.driver.install_app(Path_Apk)
            print("Se Instaló el app correctamente")
        except Exception as e:
            assert False, f"Se produjo un error durante la instalación de la aplicación:\n Error: {e}"

    def switchApp(self, app_package, app_activity):
        """
        Funcion que permite cambiar de una aplicacion a otra en el mismo flujo
        :param app_package: Package de la app a la que se desea cambiar
        :param app_activity: Activity de la aplicación a la que se desea cambiar
        :return: acción de cambio de aplicación
        """
        try:
            # Reiniciar app de fabrica borrando data cache
            subprocess.run(['adb', 'shell', 'pm', 'clear', app_package])
            print("Se reinicio la aplicacion correctamente")
            # Configura las nuevas capacidades para la aplicación objetivo
            desired_caps = {
                'appPackage': app_package,
                'appActivity': app_activity
            }

            # Cambia a la aplicación objetiva utilizando start_activity
            # self.driver.start_activity(app_package, app_activity) """ Metodo deprecado """
            # self.driver.execute_script('mobile: startActivity', {'appPackage': f'{app_package}','appActivity': f'{app_activity}'})
            self.driver.execute_script('mobile: startActivity', {
                'package': app_package,
                'activity': app_activity
            })
            print(f"Se cambio a la aplicacion: {app_package}, de forma correcta")
        except Exception as e:
            assert False, "Error al cambiar de aplicación: {}".format(str(e))

    def pressKey(self, code):
        """
        Funcion que permite hacer comandos en gestos del teclado del navegador
        :param code: codigo de teclado a utilizar
        :return:
        """
        try:
            self.driver.press_keycode(code)
        except WebDriverException as e:
            print(f"Error al presionar la tecla: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    ######################### SEARCH AND SEND, INPUTS; ELEMENTS; TEXT AND SELECTORS ################################

    def find_element(self, by_tipo: By, selector: str):
        try:
            val = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            return val
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def findListOfElementsBySelector(self, by_tipo: By, selector: str):
        """
        Funcion que retorna una lista de localizadores con el mismo tipo de selector y by_typo.
        :param by_tipo: Ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta de los elementos que se desean encontrar.
        :return: Listado de localizadores que contengan el mismo selector y by_tipo.
        """
        try:
            time.sleep(2)
            val = self.driver.find_elements(by_tipo, selector)
            return val
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el listado de " \
                          f"elementos\n selector usado: {selector} de tipo: {by_tipo}\n Log: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontro el listado de " \
                          f"elementos, selector usado: {selector} de tipo: {by_tipo}\n Log: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el selector proporsionado: {selector} de tipo: {by_tipo}\n Log: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido mientras se buscaba listado de elementos con selector:{selector}\n  Log: {ex}"

    def send_Numb_In_Input_By_Selector(self, by_tipo: By, selector: str, numb: float, tiempo: float):
        """
        Enviar número sobre un input de data numerica solamente

        :param selector: Ruta del elemento que se desea enviar un numero
        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param numb: Dato numerico para enviar en el input numerico.
        :param tiempo: valor numerico tipo float que determina el tiempo de espera.
        :return: Accion que envia solo valores numerico en un input
        """

        try:

            ele = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            # Limpiar campo y enviar texto
            ele.clear()
            ele.send_keys(numb)
            BaseActions.Tiempo(tiempo)
            print(f"Cargado el numero {numb} correctamente")
            allure.attach(f"Cargado el numero {numb} correctamente")
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def send_Text_In_Input_By_Selector(self, by_tipo: By, selector: str, texto: str, tiempo: float):
        """
        Enviar texto en un campo tipo input

        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta del elemento donde se desea ingresar el texto.
        :param texto: Cadena de texto que se enviara dentro del input seleccionado.
        :param tiempo: Valor numerico tipo float que determina el tiempo de espera.
        :return: Accion que envia una cadena de texto a un campo de tipo input
        """

        try:
            ele = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((by_tipo, selector)))
            # Limpiar campo y enviar texto
            ele.clear()
            ele.send_keys(texto)
            BaseActions.Tiempo(tiempo)
            print(f"Cargado el texto {texto} correctamente")
            allure.attach(f"Cargado el texto {texto} correctamente")
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n Log: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n Log: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n Log: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: Log {ex}"

    def scrollAndFindVisibleElementBySelector(self, by_tipo: By, selector: str):
        """
        Hacer scroll hacia un elemento específico en el home Clasico

        :param by_tipo: Ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta o path del elemento al cual se desea encontrar haciendo scroll
        :return: Accion que ejecuta un scroll hacia la ubicación del elemento seleccionado en selector.
        """

        try:
            while True:
                try:
                    self.driver.find_element(by_tipo, selector)
                    break
                except NoSuchElementException:
                    # Obtener tamaño de la pantalla
                    window_size = self.driver.get_window_size()
                    width = window_size['width']
                    height = window_size['height']

                    # Calcular coordenadas para desplazamiento
                    start_x = width // 2
                    start_y = int(height * 0.7)
                    end_y = int(height * 0.5)

                    # Realizar desplazamiento
                    self.driver.swipe(start_x, start_y, start_x, end_y)

                    # Validar si se ha llegado al final de la pantalla
                    if self.driver.find_element(by_tipo, selector).is_displayed():
                        break
        except NoSuchElementException:
            assert False, "No se pudo encontrar el elemento después de hacer scroll"
        except WebDriverException as e:
            assert False, "Ocurrió un error de WebDriver al intentar hacer scroll: " + str(e)
        except Exception as ex:
            assert False, f"No se pudo hacer scroll hasta encontrar el elemento :{selector}\n el Erro es: {ex}"

    def scrollUp(self, howManySwipeToUp):
        """
        Funcion que permite hacer swipe largo hacia arriba lo que deslizara
        el contenido de pantalla hacia arriba mostrando nuevo contenido desde abajo
        :param howManySwipeToUp: Cantidad de veces que se realizara swipe en pantalla.
        """
        try:
            for i in range(1, howManySwipeToUp + 1):
                # Obtener medida de pantalla
                window_size = self.driver.get_window_size()
                width = window_size['width']
                height = window_size['height']
                # Calcular coordenadas para desplazamiento
                start_x = width // 2
                start_y = int(height * 0.7)
                end_y = int(height * 0.3)
                # Realizar desplazamiento
                self.driver.swipe(start_x, start_y, start_x, end_y)
                BaseActions.Tiempo(0.5)
                print(f"Se realizo swipe Up {i} veces")
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se realizar el scroll" \
                          f"\n Log: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def scrollToFindElementByText(self, Find_Text):
        """
        Hacer scroll hasta encontrar un texto en específico

        :param Find_Text: Texto del elemento que se desea conseguir haciendo scroll
        :return: Accion que ejecuta un scroll hacia la ubicación del elemento con el texto indicado.
        """

        try:
            i = 0
            status = False
            ele_repe = ["null"]  # Inicializacion de listado de elementos repetidos
            while i < 1:
                search_text = None
                search_text = self.driver.find_elements(By.CLASS_NAME,
                                                        "android.widget.TextView")  # Hacer listado de elementos con la misma class name
                for sear in search_text:  # Iterar listado de elementos para buscar el texto de cada elemento de clase "android.widget.TextView"
                    if Find_Text in sear.text:  # Encontrar coincidencias del listado de elementos con el texto deseado
                        print(f"Elemento: {Find_Text} encontrado")
                        # sear.click()  # Click sobre el elemento con el texto buscado
                        i += 1
                        status = True
                        break
                    elif sear.text == search_text[-1].text and search_text[-1].text == ele_repe[-1]:
                        i += 1
                        print(f"No se encontró el elemento: {Find_Text}")
                        break
                    elif sear.text == search_text[
                        -1].text:  # Si el listado de elementos llego al texto limitador, debera generar scroll y repetir el ciclo de busqueda
                        # Obtener el texto del último elemento registrado
                        last_position = search_text[search_text.index(sear) - 1].text
                        # Agregar ese ultimo elemento a listado de elementos repetiros
                        ele_repe.append(last_position)
                        # Obtener medida de pantalla
                        window_size = self.driver.get_window_size()
                        width = window_size['width']
                        height = window_size['height']
                        # Calcular coordenadas para desplazamiento
                        start_x = width // 2
                        start_y = int(height * 0.7)
                        end_y = int(height * 0.5)
                        # Realizar desplazamiento
                        self.driver.swipe(start_x, start_y, start_x, end_y)
                        break
            return status
        except Exception as ex:
            assert False, f"No se pudo desplazar al elemento con el texto: {Find_Text}\n el Error es: {ex}"

    def getTextOnElement(self, by_tipo: By, selector: str):
        """
        Obtener el texto de un elemento, retornará el texto solamente

        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta o path del elemento al cual se le extraera el texto.
        :return: Retorna el texto del elemento sobre el cual se evaluó la funcion
        """

        try:
            val = None
            val = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            ele = str(val.text)
            return ele
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def findEmailVerification(self, Email):
        """
        Funcion que permite localizar el correo de confirmacion en yopmail
        """
        i = 0
        while i < 1:
            try:
                time.sleep(1)
                element = None
                # Hacer click en el primer correo recibido
                BaseActions.tap_Screen(self, 629, 796, 300)
                time.sleep(1)

                # Verificar si se muestra el texto de confirma tu registro
                element = self.driver.find_elements(By.CLASS_NAME, "android.view.View")
                for ele in element:
                    if ele.text == "¡Confirmá tu registro!":
                        print("Se hizo click sobre el card de correo assist card")
                        i += 1
                        break
                else:
                    print("No se muestra nada")
                    raise NoSuchElementException

            except NoSuchElementException:
                elements = None
                elements = self.driver.find_elements(By.CLASS_NAME, "android.view.View")
                email_lower = str(Email).lower()
                for ele in elements:
                    if ele.text == "":
                        print(
                            "El correo abierto no es el correo de confirmacion de AssistCard, se procedera a retroceder y refrescar navegador")
                        # Regresar a la pantalla anterior utilizando self.driver.back() en caso de encontrar el emoji de reloj
                        self.driver.back()
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='refresh']").click()
                        time.sleep(2)
                        break
                    elif ele.text == email_lower:
                        print(f"No se muestra ningún correo disponible, Se procedera a refrescar navegador")
                        # Si detecta el correo del usuario quiere decir que no hay correo para ingresar, por lo tanto, se deberá refrescar
                        self.driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='refresh']").click()
                        time.sleep(2)
                        break
                else:
                    # Si no se cumple ninguna de las condiciones anteriores, repetir el bucle desde el inicio
                    print("Se repetira el flujo")
                    continue

            except TimeoutException as ex:
                assert False, f"Error: Tiempo de espera agotado mientras se buscaba el correo de confirmación de assistcard\n El error es: {ex}"

            except ElementNotInteractableException as ex:
                assert False, f"Error: No se puede interactuar con el correo de confirmación de assistcard\n El error es: {ex}"

            except Exception as ex:
                assert False, f"Error desconocido al buscar el correo de confirmación de assistcard: {ex}"

    def clickCheckCapchat(self):
        try:
            result = False
            time.sleep(1)
            elements = None
            elements = self.driver.find_elements(By.CLASS_NAME,
                                                 "android.widget.CheckBox")  # Crear listado de elementos con la clase Checkbox
            for ele in elements:  # Se itera elemento por elemento hasta encontrar el que coincide con el texto del capchat
                if ele.text == "No soy un robot":
                    print(f"Se encontro el capchat")
                    elements[elements.index(ele)].click()  # Sí detecta el elemento esperado hara click sobre el
                    result = True
                    break
            if result is False:
                print("No hay capchat que validar")
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se" \
                          f"buscaba algun capchat en pantalla\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró ningun capchat en pantalla\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar ningun capchat en pantalla\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido al buscar algun capchat en pantalla: {ex}"

    def keyboard_Hide(self):
        """
        Funcion que permite ocultar el teclado
        """
        try:
            self.driver.hide_keyboard()
            print("Se realizó la acción de ocultar el teclado")
        except Exception as ex:
            assert False, f"Error desconocido al intentar ocultar el teclado: {ex}"

    #################################### CLICK ON ELELMENT WITH METHOD BY ###################################

    def clickOnElementByText(self, texto: str, tiempo: float):
        """
        Hacer click sobre un elemento que contenga un texto en específico

        :param texto: Texto que se buscara en pantalla el cual se hara la accion de click
        :param tiempo:valor numerico tipo float que determina el tiempo de espera.
        :return: Accion de click sobre un elemento con el texto enviado en el valor Texto
        """

        try:
            element = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, f"//android.widget.TextView[contains(@text, '{texto}')]")))
            element.click()
            print(f"Se ejecuto click sobre el elemento: {texto}")
            BaseActions.Tiempo(tiempo)
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento con el texto: {texto}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento con el texto: {texto}\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento que " \
                          f"contiene el texto {texto}\n El Error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def clickOnElementBySelector(self, by_tipo: By, selector: str, tiempo: float):
        """
        Hacer click sobre un elemento

        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta o path del elemento a cliquear.
        :param tiempo: valor numerico tipo float que determina el tiempo de espera.
        :return: Accion de hacer click sobre un elemento específico
        """

        try:
            ele = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            ele.click()
            print(f" Se ejecuto click sobre el elemento: {selector}")
            BaseActions.Tiempo(tiempo)
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba " \
                          f"el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"

        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} " \
                          f"de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            print(f"Error desconocido: {ex}")

    def multiClickMethodBy(self, by_tipo: By, selector: str, Cant_Click: int):
        """
        Realiza multiples clics sobre un elemento

        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta o path del elemento a cliquear.
        :param Cant_Click: cantidad de veces que se hara click sobre el elemento.
        :return: Accion de cliquear la cantidad de veces definida por Cant_Click
        """

        try:
            ele = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            for i in range(1, (int(Cant_Click) + 1)):
                ele.click()
            print(f"Se hicieron {Cant_Click} Clicks sobre el elemento {selector}")
            time.sleep(1)
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba " \
                          f"el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} " \
                          f"de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            print(f"Error desconocido: {ex}")

    def selectDateInDatePickerNative(self, by_tipo: By, selector: str, Day, Month: str, Year, tiempo: float):
        """
        Funcion que permite selecciona una fecha en un DatePicker nativo de android
        :param tiempo: tiempo de espera luego de la ejecucion de la funcion
        :param selector: URL del elemento datepicker a buscar para hacer click
        :param by_tipo: Tipo de By del elemento datepicker
        :param Day: Día a seleccionar
        :param Month: Mes a seleccionar
        :param Year: Año a seleccionar
        """
        try:
            # Diccionario para obtener el numero del mes correspondiente a seleccionar como mes de nacimiento
            meses = {
                "enero": 1,
                "febrero": 2,
                "marzo": 3,
                "abril": 4,
                "mayo": 5,
                "junio": 6,
                "julio": 7,
                "agosto": 8,
                "septiembre": 9,
                "octubre": 10,
                "noviembre": 11,
                "diciembre": 12
            }
            Day = str(Day)
            Year = str(Year)
            Month = str(Month).lower()
            number_month_birth = meses.get(Month.lower())
            ele = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            ele.click()
            print(f"Se hizo Click sobre el elemento {selector}")
            year = WebDriverWait(self.driver, 50).until \
                (EC.visibility_of_element_located((By.ID, "android:id/date_picker_header_year")))
            # Seleccionar año de nacimiento
            if year.text == Year:
                print(f"Año seleccionado: {Year}")
            else:
                year.click()
                i = 0
                while i < 1:
                    search_text = None
                    search_text = self.driver.find_elements(By.CLASS_NAME,
                                                            "android.widget.TextView")  # Hacer listado de elementos con la misma class name
                    for sear in search_text:  # Iterar listado de elementos para buscar el texto de cada elemento de clase "android.widget.TextView"
                        if Year in sear.text:  # Encontrar coincidencias del listado de elementos con el texto deseado
                            print(f"Año de nacimiento encontrado: {Year}")
                            sear.click()  # Click sobre el elemento con el texto buscado
                            BaseActions.Tiempo(tiempo)
                            i += 1
                            break
                        elif sear.text == search_text[
                            -1].text:  # Si el listado de elementos llego al final y no hubo coincidencia, debera generar scroll y repetir el ciclo de busqueda
                            # Obtener medida de pantalla
                            window_size = self.driver.get_window_size()
                            width = window_size['width']
                            height = window_size['height']
                            # Calcular coordenadas para desplazamiento hacia arriba (Scroll Down)
                            start_x = width // 2
                            start_y = int(height * 0.6)
                            end_y = int(height * 0.8)
                            # Realizar desplazamiento
                            self.driver.swipe(start_x, start_y, start_x, end_y)
                            break
            # Seleccionar Mes de nacimiento
            date_today = datetime.datetime.now()  # Obtener mes actual para tomarlo como punto de partida
            this_month = date_today.month

            if this_month == number_month_birth:  # Comparar si el mes de nacimiento coincide con el mes actual
                print(f"Mes seleccionado correctamente: {Month}")
            elif number_month_birth < this_month:  # Evaluar si el mes de nacimiento es menor que el mes actual
                difference = this_month - number_month_birth
                # Hacer click en boton retroceder el mes, hasta llegar al mes de nacimiento
                BaseActions.multiClickMethodBy(self, By.XPATH,
                                               "//android.widget.ImageButton[@content-desc='Mes anterior']", difference)
                print(f"Se retrocedió {difference} veces para ubicar el mes: {Month}")
            else:  # Evaluar si el mes de nacimiento es mayor al mes actual
                difference = (number_month_birth - this_month)
                # Hacer click en boton avanzar el mes, hasta llegar al mes de nacimiento
                BaseActions.multiClickMethodBy(self, By.XPATH,
                                               "//android.widget.ImageButton[@content-desc='Mes siguiente']",
                                               difference)
                print(f"Se avanzó {difference} veces para ubicar el mes: {Month}")

            # Seleccionar Dia de nacimiento
            BaseActions.clickOnElementBySelector(self, By.XPATH, f"//android.view.View[contains(@text,'{Day}')]",
                                                 tiempo)

            # Guardar Fecha de nacimiento seteada
            BaseActions.clickOnElementBySelector(self, By.ID, "com.assistcard.assistcard.qa:id/btnDatePickerDialogOk",
                                                 tiempo)

        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba " \
                          f"el datepicker con el selector: {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el datepicker con el selector: {selector} de tipo {by_tipo}" \
                          f"\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el datepicker con el selector: {selector} " \
                          f"de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            print(f"Error desconocido al intentar acceder al datepicker: {ex}")

    ################################## EVALUATE ELEMENT TO RETURN BOOLEAN ##############################

    def findElementIsVisibleByText(self, texto: str):
        """
        Esta funcion permite Encontrar un texto específico en pantalla y que retorne True si lo consigue

        :param texto: texto que se desea buscar dentro de la pantalla.
        :return: Un valor True si se encuentra el elemento en pantalla de ser caso contrario retornara False
        """

        try:
            result = False
            element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located
                                                           ((By.XPATH, f"//android.widget.TextView"
                                                                       f"[contains(@text, '{texto}')]")))
            if element.is_displayed():
                result = True
                print(f"Se encontro el elemento con el texto: {texto}")
            return result
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento con el texto: {texto}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento con el texto: {texto}\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento que " \
                          f"contiene el texto {texto}\n El Error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def findElementIsVisibleBySelector(self, by_tipo: By, selector: str):
        """
        Esta funcion permite Encontrar un texto específico en pantalla y que retorne True si lo consigue

        :param by_tipo: Ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta del elemento a localizar para identificar si está visible.
        :return: Un valor True si se encuentra el elemento en pantalla de ser caso contrario retornará False
        """

        try:
            result = False
            element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located
                                                           ((by_tipo, selector)))
            if element.is_displayed():
                result = True
                print(f"Se encontro en pantalla el elemento: {selector} de tipo {by_tipo}")
            return result
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento: {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento: {selector} de tipo {by_tipo}\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento:" \
                          f" {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def findElementIsDisplayed(self, by_tipo: By, selector: str):
        """
        Esta función permite encontrar un elemento específico en pantalla y devuelve True si está visible o False si no lo encuentra.

        :param by_tipo: Tipo de selector a usar, como XPATH, CLASS_NAME, ID, etc.
        :param selector: Selector del elemento a buscar.
        :return: True si el elemento está visible, False si no lo está o se produce un error.
        """
        try:
            element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by_tipo, selector)))
            if element.is_displayed():
                print(f"Se encontró en pantalla el elemento: {selector} de tipo {by_tipo}")
                return True
            else:
                print(f"El elemento: {selector} de tipo {by_tipo} no está visible en pantalla.")
                return False
        except TimeoutException:
            print(f"Error: Tiempo de espera agotado mientras se buscaba el elemento: {selector} de tipo {by_tipo}")
            return False
        except NoSuchElementException:
            print(f"Error: No se encontró el elemento: {selector} de tipo {by_tipo}")
            return False
        except ElementNotInteractableException:
            print(f"Error: No se puede interactuar con el elemento: {selector} de tipo {by_tipo}")
            return False
        except Exception:
            print(f"Error desconocido: No se localizo el elemento")
            return False

    def findTexts_In_ListSelectors_With_SameClassName(self, selector: str, text_compare: str, tiempo: float):
        """
        Busca en todos los elementos de la misma clase aquel que contenga el texto indicado y retorna un true

        :param selector: Path del selector de tipo ClassName, para traer todos los elementos de la misma clase.
        :param text_compare: texto para buscar alguna coincidencia entre todos los elementos de la misma clase.
        :param tiempo: Valor numerico flotante que determina el
                        tiempo de espera luego de la ejecucion de la funcion.
        :return: Retornará True si en la lista de elementos de la misma clase
                existe algun elemento que contenga el text_compare
        """

        try:
            self.driver.implicitly_wait(10)
            elements = self.driver.find_elements(By.CLASS_NAME, selector)
            result = False
            for ele in elements:
                if ele.text in text_compare:
                    print(f"Se encontró en pantalla el texto: {ele.text}")
                    result = True
                    break
                else:
                    result = False
            if result is False:
                print("No se muestra ninguna alerta en pantalla")
            BaseActions.Tiempo(tiempo)
            return result
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se" \
                          f"buscaba el elemento {selector}\n El error es: {ex} "
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector}\n El error es: {ex} "
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector}\n El error es: {ex} "
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def validateToastWithTextVisible(self, texto: str):
        """
        funcion para identificar si un toast contiene un texto esperado y como resultado retornará True
        :param texto: Texto que se espera encontrar dentro del toast.
        :return: Si coincide el texto retornará True
        """

        try:
            self.driver.implicitly_wait(20)
            element = self.driver.find_element(By.XPATH, "//android.widget.Toast[1]")
            result = False
            # Obtener el texto del toast
            if texto == element.text:
                result = True
                print("Se encontro el Texto del toast:", element.text)
            else:
                assert False, f"Error el mensaje del toast: {element.text}, no coincide con el mensaje esperado: {texto}"
            return result
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se" \
                          f"buscaba el elemento con el texto: {texto}\n El error es: {ex} "
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento con el texto: {texto}\n El error es: {ex} "
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento con el texto: {texto}\n El error es: {ex} "
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def is_checkbox_selected(self, by_tipo: By, selector: str):
        """
        Verifica si un checkbox está seleccionado.

        Args:
        :param by_tipo: Tipo de selector a usar, como XPATH, CLASS_NAME, ID, etc.
        :param selector: Selector del elemento a buscar.

        Returns:
            bool: True si el checkbox está seleccionado, False si no lo está o si no se encuentra.
        """
        try:
            checkbox_element = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((by_tipo, selector)))
            return checkbox_element.is_selected()
        except Exception as e:
            assert False, f"Error al verificar el estado del checkbox: {str(e)}"

    ########################### SELECCIONAR LISTAS ##############################################

    def select_Option_In_List(self, by_tipo=By, selector=str, tipo=str, dato=str or int, tiempo=float):
        """
        Esta funcion Selecciona una opcion de un input tipo select donde los parametros son:

        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Path del selector que contiene la lista de opciones (elemento de tipo select)
        :param tipo: Definir que tipo de búsqueda realizara la funcion, si es por tipo "text", "value" o "index"
        :param dato: Dato que se desea buscar dentro del select si es int() seria
                    para tipo index, si es str() seria para value o text.
        :param tiempo: Valor numerico flotante que determina el
                        tiempo de espera luego de la ejecucion de la funcion.
        :returns
            Ejecucion de buscar elemento en listado de input select
        """
        try:
            tipo_new = str(tipo).lower()
            result_tipo = True
            ele = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by_tipo, selector)))
            find = Select(ele)
            if tipo_new == "text":
                find.select_by_visible_text(dato)
            elif tipo_new == "index":
                find.select_by_index(dato)
            elif tipo_new == "value":
                find.select_by_value(dato)
            else:
                result_tipo = False
            assert result_tipo is True, "El valor del parametro tipo debe ser " \
                                        "entre las tres opciones (text, value, index) \n" \
                                        f"El valor ingresado fue {tipo} "
            print(f"La opcion seleccionada es: {dato}")
            BaseActions.Tiempo(tiempo)
        except TimeoutException as ex:
            assert False, f"Error no se localizo una opcion en la lista con el valor: {dato}\n El error es: {ex}"

    #################################### ALLURE SCREENCSHOT ##############################################

    def screenshot(self, nombre=str):
        """
        Funcion que permite tomar una captura de pantalla

        :param
            nombre (str): Nombre con el cual se guardata la captura.
        :return
            Captura de pantalla en el reporte allure
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.PNG)
        print("Imagen capturada")
        BaseActions.Tiempo(0.5)

    def uploadFile(self, tipo=By, selector=str, ruta=str):
        try:
            val = self.driver.find_element(tipo, selector)
            val.send_keys(ruta)
            print("\n Elemento Cargado -> {} ".format(selector))
        except Exception as ex:
            assert False, f"No se pudo subir el archivo {ruta}\n El error es: {ex}"

    @staticmethod
    def saveFileStorageEmulator(uri_destino, path_local, emulador_id=Datatest.EMULADOR_ID):
        """
        Copia un archivo desde la ruta local al almacenamiento interno del emulador Android en la carpeta "Downloads".

        Parámetros:
        - path_local (str): La ruta local del archivo que deseas copiar.
        - uri_destino (str): Ruta donde se almacenara la imagen o archivo.
        - emulador_id (str, opcional): El ID del emulador Android (por defecto es 'emulator-5554').
        """
        try:
            comando_adb = f"adb -s {emulador_id} push {path_local} {uri_destino}"

            resultado = subprocess.run(comando_adb, shell=True, check=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, text=True)
            if resultado.returncode == 0:
                print(f"Archivo copiado exitosamente a {uri_destino}.")
            else:
                assert False, f"Error al copiar el archivo a {uri_destino}: {resultado.stderr}"

        except subprocess.CalledProcessError as e:
            assert False, f"Error al copiar el archivo '{path_local}' al emulador: {e.stderr}"

    @staticmethod
    def deleteAllFilesEmulator(uri_destino, emulador_id=Datatest.EMULADOR_ID):
        """
        Elimina todos los archivos descargados en el emulador de Android Studio.

        Parámetros:
        - uri_destino (str): Ruta de la carpeta que dese eliminar el contenido
        - emulador_id (str, opcional): El ID del emulador Android (por defecto es 'emulator-5554').
        """
        try:
            comando_adb = f"adb -s {emulador_id} shell rm -rf {uri_destino}"

            resultado = subprocess.run(comando_adb, shell=True, check=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, text=True)
            BaseActions.Tiempo(1)
            if resultado.returncode == 0:
                print("Todos los archivos eliminados exitosamente.")
            else:
                assert False, f"Error al eliminar todos los archivos: {resultado.stderr}"
        except subprocess.CalledProcessError as e:
            assert False, f"Error al eliminar todos los archivos: {e.stderr}"
