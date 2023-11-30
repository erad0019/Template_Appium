from behave import *
from app.application import Application


@given(u'Inicializo la aplicacion Assist Card')
def step_impl(context):
    try:
        context.application = Application(context.driver)
    except Exception as ex:
        assert False, f"Fallo el step al Inicializar la aplicacion Assist Card\n Motivo del Error: {ex}"


@then(u'Mostrar Splash de assist card')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ValidateMessageOfPageInitial()
    except Exception as ex:
        assert False, f"Fallo el step al confirmar que se muestre la pagina inicial de bienvenida\n Motivo del Error: {ex}"


@when(u'Pulsar boton continuar en la pagina de bienvenida')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ClickOnButtonContinueSetupPage()
    except Exception as ex:
        assert False, f"Fallo el step al hacer click en el boton continuar\n Motivo del Error: {ex}"


@then(u'Mostrar modal de solicitud de permisos de notificacion en la app')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ValidateModalNotificationAndGPS()
    except Exception as ex:
        assert False, f"Fallo el step al validar modal de acceso a notificaciones y GPS\n Motivo del Error: {ex}"


@when(u'Pulsar boton continuar de la modal de permisos de notificacion y ubicacion')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ClickOnButtonContinueOfModal()
    except Exception as ex:
        assert False, f"Fallo el step al hacer click en continuar dentro de la modal de acceso\n Motivo del Error: {ex}"


@then(u'Mostrar modal de permisos para permitir acceso a ubicacion del dispositivo')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ValidateAlertOfPermission()
    except Exception as ex:
        assert False, f"Fallo el step al validar que se muestre la modal de permisos\n Motivo del Error: {ex}"


@when(u'Pulsar boton "Mientras la app esta en uso"')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ClickOnButtonAccepPermission()
    except Exception as ex:
        assert False, f"Fallo el step al hacer click en conceder permisos de GPS\n Motivo del Error: {ex}"


@then(u'Validar que redireccione a la pagina Initial steps')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ValidatePageLoginInitialSteps()
    except Exception as ex:
        assert False, f"Fallo el step al validar la visualizacion de login page\n Motivo del Error: {ex}"
