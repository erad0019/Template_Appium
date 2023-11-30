@regression
Feature: Initial steps
  Background:
    Given Inicializo la aplicacion Assist Card

  Scenario: Configuracion Inicial - concediendo permisos de ubicación y notificacion
    # TC46565: Initial Setup
    Then Mostrar Splash de assist card
    When Pulsar boton continuar en la pagina de bienvenida
    Then Mostrar modal de solicitud de permisos de notificacion en la app
    When Pulsar boton continuar de la modal de permisos de notificacion y ubicacion
    Then Mostrar modal de permisos para permitir acceso a ubicacion del dispositivo
    When Pulsar boton "Mientras la app esta en uso"
    Then Validar que redireccione a la pagina Initial steps