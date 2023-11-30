# Automatización de pruebas con Selenium y Appium


# AssistCard

Este proyecto es una automatización de pruebas con Selenium y Appium bajo el framework Behave. En este README encontrarás toda la información necesaria para instalar y configurar el entorno virtual, así como para ejecutar las pruebas.

## Estructura del proyecto

El proyecto está estructurado de la siguiente manera:

1. La carpeta (**app**) contiene una clase inicializadora de cada clase que provenga de una página.

	- init.py: Archivo de inicialización de la carpeta.
	- application.py: Archivo que contiene la clase inicializadora.
2. La carpeta (**configuration**) contiene un archivo de configuración.

	- init.py: Archivo de inicialización de la carpeta.
	- config.py: Archivo que contiene la configuración.

3. La carpeta (**features**) contiene la estructura del framework Behave y el modelo Page Object.

	- La carpeta (**pages_object**) contiene todos los objetos de cada página de la aplicación.

		* init.py: Archivo de inicialización de la carpeta.

		* Init_Page.py: Archivo que contiene la clase de objeto de página para la página de inicio.

		* Login_Page.py: Archivo que contiene la clase de objeto de página para la página de inicio de sesión.

	- La carpeta (**steps**) contiene las definiciones de los pasos de los features.

		* init.py: Archivo de inicialización de la carpeta.

		* InitPageStep.py: Archivo que contiene las definiciones de los pasos para la página de inicio.

		* LoginSteps.py: Archivo que contiene las definiciones de los pasos para la página de inicio de sesión.

	- La carpeta (**tests**) guarda todos los features creados.
    
		* Sub Carpetas modularizando cada seccion del aplicativo:

	- El archivo (**environment.py**): Archivo que contiene el hook para inicializar antes y después de cada escenario.

4. Carpeta (**resources**): :::SE DEBERA CREAR ESTA CARPETA CON NOMBRE "resources"::: Esta carpeta contiene archivos de recursos para la ejecucion de pruebas, como por ejemplo archivo excel como BD, la apk de Assist Card, la apk de navegador Browser, almacenar algun screenshot, o archivo de ser necesario
   Esta carpeta debe ser descargada de un drive y actualizada a la version de apk mas actual de Assist Card...
   

    NOTA: No actualizar la apk de browser, porque implicaria cambios mayores en el codigo para acceder a navegador


	La ruta para descargar el contenido de la carpeta resources es:  https://drive.google.com/drive/u/0/folders/1C9vATvbKG8VVgpBll4gmlI40RnVvXDTu

5. La carpeta (**support**) contiene archivos de soporte sobre metodos y funciones utilizados en el codigo.

    - init.py: Archivo de inicialización de la carpeta.

    - BaseActions.py: Archivo que contiene todas las acciones en métodos que serán utilizados por las diferentes funciones de Page.

	- GeneralLocator.py: Archivo donde se alojan las clases por cada page que a su vez reposan los diferentes locators utilizados

6. El archivo (**Comandos.txt**): Archivo que contiene los pasos para ejecutar las pruebas a través de consola.


7. El archivo (**requirements.txt**) contiene las dependencias necesarias para ejecutar el proyecto.


## Instalación de Appium

Para instalar Appium, sigue los siguientes pasos:

1. Instala Node.js desde https://nodejs.org/en/download/.
2. Abre una terminal y ejecuta el siguiente comando: npm install -g appium.
3. Descarga La version estable 2.0 o superior de Appium Server GUI desde https://github.com/appium/appium-desktop/releases/.
4. Instala JDK y SDK.
5. Crea las variables de entorno JAVA_HOME y ANDROID_HOME con la ruta donde están instalados los archivos JDK y SDK respectivamente.


## Instalación del archivo requirements

Para instalar todas las dependencias necesarias para este proyecto, sigue los siguientes pasos:

1. Después de descargar el repositorio, abre tu IDE y selecciona la carpeta del proyecto para crear un entorno virtual de Python. Asegúrate de tener Python 3.11 o una versión superior instalada.

2. Crea una variable de entorno para el intérprete de Python actualizado. Copia la ruta absoluta de la variable de entorno hasta la carpeta "Scripts". Por ejemplo, "C:\Users\user\Documents\EpidataSA\appiumassistcardpython\venv\Scripts".

3. Abre una consola de comando y accede a la ruta copiada.

4. Ejecuta el siguiente comando para activar la variable de entorno:
```
activate
```
5. Retrocede a la carpeta del entorno virtual con el comando "cd..".

6. Una vez allí, ejecuta el siguiente comando para instalar todas las dependencias del proyecto:

```
pip install -r <ruta absoluta del archivo requirements.txt>
```

7. Una vez que se hayan instalado todos los plugins y dependencias, ejecuta el siguiente comando para desactivar la variable de entorno:


```
deactivate
```

## Uso

Para ejecutar las pruebas en un dispositivo fisico, se deben seguir los siguientes pasos:

1. Clonar el repositorio en tu máquina local.
2. Obtener Datos del Device desde ADB
   - Abrir consola CMD y tener el dispositivo físico conectado a la pc
   - Ejecutar el comando:
      ```
      adb devices -l
      ```
   - Se obtendría la data sobre el nombre del dispositivo como device-name    

3. Configurar archivo config.py el capabilities que lleva por nombre (**ANDROID_CONFIG**), ubicando el package y activity correspondiente al app y el cambio de nombre de device y version de OS Android:
	- Abir consola CMD en Windows o terminal en linux
	- Tener dispositivo físico con permisos de depurar USB conectado a la pc
	- Acceder desde el dispositivo físico al app
	- Correr el comando: 
		```
		adb shell "dumpsys window windows ! grep -E 'mCurrentFocus|mFocusedApp'"	
		```
	- Sustraer el package y activity
	- Ingresar la información del package y activity donde corresponde dentro del archivo config.py

4. Crear Carpeta `resources` al mismo nivel que la carpeta `support`
5. Descargar el apk de Assist Card desde Firebase y alojarlo en carpeta `resources`.
6. Descargar apk de firefox desde esta ruta https://drive.google.com/file/d/1E30ih6g-vmNVK_890684R8UiwPQlewo6/view?usp=drive_link, una vez descargada debera ser almacenada en la carpeta `resources`.
7. Modificar el archivo `config.py` con las rutas correspondientes al package, activity de la app de assistcard y el device name del emulador o dispositivo a probar
8. Ejecutar los casos de prueba utilizando los comandos especificados en `comandos.txt`.
9. Ver los reportes de Allure en la carpeta `reports`.

## BD con Excel

1. EL archivo excel debe contar con 11 columnas de datos

| Nombre | Apellido | Correo | Contraseña | Genero | Pais | N° documento	 | Codigo Pais	 | Mes de nacimiento	 | Dia de nacimiento	 | Año de nacimiento |
|:-----|:-------|:-----|:---------|:-----|:---|:------------|:-----------|:-----------------|:-----------------|:----------------|
Tal como se muestra en la imagen

2. El archivo debe tener contener 3 hojas


* Correos_Inexistentes: Este listado contendra todos los correos que nunca se han regitrados en la app
* Registros_Buscar_Servicios: Este listado es donde se almacenaran los datos provenientes de la hoja "Correos_Inexistentes", estos datos servirán para hacer proceso de login por primera vez
* Usuarios_Sin_Servicios: Este listado es donde se almacenaran los datos provenientes de la hoja "Registros_Buscar_Servicios", estos datos son únicamente para registros de usuarios que NO vincularon ningun servicio con su registro, es decir, que seleccionaron la opcion "Registro nuevo"

3. **La libreria utilizada es Openpyxl de python**


4. Podras descargar el formato del excel en esta direccion: https://docs.google.com/spreadsheets/d/1A9xvNRYlao4lJzuqOhb45qulS4J86qVI/edit?usp=drive_link&ouid=104690734586893471662&rtpof=true&sd=true


5. Se debera llenar la primera página del archivo BD.xlsx con datos random que no existan en la app como registro, el archivo cuenta con validaciones que pintaran en rojo aquellos datos que esten repetidos en la misma columna **solo para los datos que deben ser unicos**, de tal forma que no puedan existir datos repetidos en la BD

**IMPORTANTE**: Deben crearse las hojas con estos nombres para que sean detectados por los algoritmos al momento de actualizar los registros en la BD

**NOTA**: El listado no debera contener cabecera, directamente deben ingresar los datos en el orden especificado por cada columna como se indica en el paso **1**

Dentro de la ejecucion de los flujos de registro y login, los datos del excel se iran modificando de manera automatica una vez se valide el paso final del feature de manera exitosa

Haciendo una actualización del registro empleado en el flujo ejecutado

Usando un algoritmo que itera sobre las celdas del excel en la hoja especificada, copiando cada celda y pegando en el hoja de destino

Una vez culminada la iteracion de celdas se procede a eliminar el registro inicial de origen y guardando la edicion del archivo BD.xlsx para que el registro mantenga el destino adecuado en la hoja indicada del archivo excel

6. Ubicacion donde debes guardar el archivo -> Dentro del folder resources que debe estar al nivel de features (resources/BD.xlsx) Ejemplo:


## Licencia

Este proyecto está bajo la licencia MIT. Consulte el archivo LICENSE para obtener más información.

