# Trabajo-Integrador-Final-BACK-END---DJANGO---COMISION-23507
Trabajo integrador final del front y del back end utilizando Django 

 # Trabajo Integrador Final y Muestra de Proyectos DJANGO

 ## Tabla de Contenido
***
- [Trabajo Integrador Final y Muestra de Proyectos DJANGO](#trabajo-integrador-final-y-muestra-de-proyectos-django)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Descripción](#descripción)
  - [Tecnologías ocupadas](#tecnologías-ocupadas)
  - [Animaciones usadas y Js](#animaciones-usadas-y-js)
  - [API consumida](#api-consumida)
  - [Creacion del proyecto para el back end](#creacion-del-proyecto-para-el-back-end)
  - [Nombre del Grupo](#nombre-del-grupo)
  - [Integrantes del Grupo](#integrantes-del-grupo)


 ## Descripción
 ***
 Se trata de una pagina web sobre un Pub de Cerveceria que tambien podria vender algunas minutas para consumir con la cerveza.

 - Se puede ir entrando a cada pagina desde una barra de menu donde puede ver la localizacion y datos del pub.
 - Tambien se puede ingresar a un formulario de contactos para dejar sus datos y con respecto al contacto con el cliente tambien se puede ingresar a otro formulario de contacto (mas reducido) para registrarse como usuario y asi participar de promos.
 - Por otro lado, podemos encontrar una pagina del menu ACERCADE donde se visualiza un banner, 4 imagenes que cambian en un lapso de tiempo y descripciones sobre porque venir al pub.
 - por ultimo y no menos importante se puede encontrar la pagina del menu FAQ donde se expones las preguntas mas importantes de los clientes y sus respuestas. 
 - Agregando al Front-End se realiza el Back-End Utilizando Python, Django y MySQL, deberás crear una API REST o usando con el modelo MVT de django.
 - Se clona el front-end y se crea un CRUD (Create, Read, Update, Delete) que interactúe con la API REST que se ha desarrollado en el back-end.
 -  Se utilizan las siguientes tecnologías: HTML, CSS y Bootstrap para la estructura y diseño de la interfaz. JavaScript para la interacción con la API REST y la manipulación de los datos.
 - Thunder Client, POSTMAN o una herramienta similar para testear la API y asegurarte de su correcto funcionamiento. 

 ## Tecnologías ocupadas
 ***
    1. HTML
    2. CSS
    3. JS
    4. Python
    5. Django
    6. SQL
   
 ## Animaciones usadas y Js
 ***
    Podemos describir las siguientes:

        1. luz dada a varias imagenes que se encuentran contenidas en div
        2. un slice que se recorren 4 imagenes de derecha a izquierda y vuelve en sentido inverso sin detenerse.
        3. Trabajando con Js interactuamos con el boton hamburguesa para que aparezca y desaparezca el menu vertical al cambiar a pantalla tablet o movil
        4. Con Js se han realizados los siguientes pasos
           a. Validaciones de los formularios, tanto del formulario de registrase como de contacto
           b. Animacion a la pagina FAQ.
           c. Animacion al boton hamburguesa para que sea reposive y al ser mas reducida la pantalla se muestre el menu vertical.

 ## API consumida
 ***
    Se consume la api de un direccion que nos brinda entre sus datos, imagenes de la tematica de cerveza, nosotros de toda la API solo mostramos las imagenes
    esta API es "https://api.sampleapis.com/beers/stouts", esta API era usada en el primer proyecto del front, en esta oportunidad utilizamos  nuestra API creado con API REST FRAMEWORK.
    El breakpoint (punto de acceso) es "http://127.0.0.1:8000/api/"
    Tambien interactuamos con una API de formulario pero no es consumida en su totalidad, solo se envia datos en ellas sin recuperarlos. esta API es "https://formspree.io"
    Por otro lado hemos creado utilizando la API de Google Sheets, un formulario para crear usuarios/clientes
    registrados de los cuales al validar su usuario y clave podran acceder al CRUD.


 ## Creacion del proyecto para el back end
 ***
          
- Entorno Virtual:
   En todo proyecto es importante primero crear un entorno virtual para que tanto la versión de Python, Django y demás librerías se queden aisladas
- Creo un directorio con el nombre TPO2_backEnd, en donde colocaré todos los archivos de mi proyecto
  
    // Directorio con el nombre "TPO2_backEnd" 
 
      /TPO2_backEnd
         ... Acá irán todos los archivos del proyecto
           ...
            ...

- Usaré el paquete virtualenv para crear mi entorno virtual. Para instalarlo voy a mi consola de comandos y ejecuto el siguiente comando:
 
      pip install virtualenv

- Después de instalar el paquete, creo mi entorno virtual, yo le pondré de nombre .miev, tu le puedes poner el nombre que desees. Ejecuto el siguiente comando para crear mi entorno virtual.
 
   Comando para crear un entorno virtual con el paquete 'virtualenv' 

      python -m venv .miev  
- Ahora debemos activar nuestro entorno virtual ejecutando el siguiente comando:
 
   Comando para activar el entorno virtual 
         
      .miev/Scripts/activate

- Luego que el entorno virtual se activa, aparece en la consola o terminal, entre parentesis el nombre del entorno virtual, es decir: (.miev).

NOTA: Recuerda que siempre debes activar tu entorno virtual, antes de continuar trabajando en un proyecto con Django.

- Creación de Nuevo Proyecto
Primero debemos instalar Django, ejecutamos el siguiente comando para instalarlo:
 
      pip install django 

- Paso seguido, creo un nuevo proyecto para el sistema CRUD, le pondré de nombre appBeerPub, ejecuto el siguiente comando en mi consola de comandos.
 
   Comando para crear un nuevo proyecto con Django
      
      django-admin startproject appBeerPub

- Para verificar que el proyecto se ha creado correctamente, ingresamos al directorio del proyecto y allí arrancaremos el servidor local de Django Framework ejecutando el siguiente comando.
 
Ejecutamos el servidor local de Django 
      
      python manage.py runserver 


Si vamos al navegador y abrimos la ruta local http://localhost:8000/ puedo ver el proyecto por defecto que Django nos ha creado.

- El proyecto se ha creado correctamente. Ahora en Django necesitamos crear un nuevo modulo o aplicación para nuestro sistema CRUD, yo trabajaré con datos de beerpub entonces a mi aplicación le pondré de nombre beerpub y lo crearé ejecutando el siguiente comando:
 
Comando para crear la aplicación 'beerpub' 

      python manage.py startapp beerpub
 
- Registro la app 'postres' en el archivo  settings.py

- Base de Datos 
  usamos MySQL como base de datos. Instalo el paquete mysqlclient que da soporte a Django Framework para usar MySQL.  
  Ejecuto el siguiente comando: 
      
      pip install mysqlclient 

- Estoy usando XAMPP como servidor local, esta herramienta viene con MySQL y phpMyAdmin. Voy a crear la base de datos, la llamaré beerpub y dentro de ella creare la tabla llamada beerpub, esta tabla va tener los campos id, nombre, contacto, experiencia, img, created_at y updated_at. Como sabemos el campo id debe ser Autoincrementable, este se genera automáticamente cuando haga la migración en Django para la tabla beerpub.

      Defino los campos que va tener la tabla beerpub, abro el archivo llamado models.py que se encuentra en el directorio llamado también beerpub:

- Dentro del archivo settings.py agrego soporte y conexión a la base de datos MySQL, ya que usaré la base de datos MySQL, le colocaré el termino ‘default’ para indicarle a Django que MySQL será el motor que usaré como base de datos y debajo coloco el nombre de mi base de datos, usuario, password  y como opción le digo a Django que usaré el modo SQL tradicional. 
     
      DATABASES = {
         'sqlite': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         },
         'default': { # le coloco default para poder usar MySQL 
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'beerpub',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {
                  'sql_mode': 'traditional',
            }
         }
      }

- Ahora voy a crear la migración de la tabla beerpub, en mi consola de comandos y ejecuto el siguiente comando: 
 
      python manage.py makemigrations beerpub 

- Bien ahora procederé a crear la tabla beerpub en la base de datos, ejecuto el siguiente comando en mi consola de comandos.
 
      python manage.py migrate beerpub 

-  Cuando creamos este proyecto, Django nos generó un archivo llamado views.py en donde podemos definir las vistas y otras tares para nuestro proyecto. Django nos permite trabajar con vistas genéricas de su propio core, estas vistas genéricas nos permiten realizar de manera ágil ciertas tareas en nuestro proyecto sin escribir mucho código.

El termino CRUD significa Create, Read, Update y Delete, por ende usaré las siguientes vistas genéricas:

ListView (Para listar en la vista principal, todos los registros de la tabla beerpub)

      DetailView (Leer)
      CreateView (Crear)
      UpdateView (Actualizar)
      DeleteView (Eliminar)

Abro el archivo llamado views.py que se encuentra en TPO2_backEnd > beerpub > views.py 

- Bootstrap 5
El Framework Bootstrap 5 nos permite crear interfaces HTML de manera rápida, asi nos enfocamos solamente en la lógica de la aplicación. Voy a instalar la librería django-bootstrap5 ejecutando el siguiente comando, esta librería nos instala Bootstrap 5 dentro del Framework Django:
 
   Comando para instalar el paquete 'django-bootstrap5' 
      
      pip install django-bootstrap5 

- Django Widget Tweaks
Ahora instalaré el paquete django-widget-tweaks que me permite renderizar y gestionar los campos de los formularios de manera ágil, ejecuto el siguiente comando para instalarlo:
 
Comando para instalar el paquete 'django-widget-tweaks' 
      
      pip install django-widget-tweaks 
- Mensajes
En el archivo index.html van a recaer todos los mensajes de las operaciones Crear, Eliminar y Actualizar, es decir después de Insertar, Eliminar o Actualizar un registro o jugo de la Base de Datos, mostramos un mensaje para confirmar que dicha operación ha sido realizada Correctamente.

   Abro el archivo momentos.html que se encuentra en la carpeta templates y agrega el siguiente código:
 
      {% if messages %}
      <ul class="messages list-group mb-3">
         {% for message in messages %}
         <li{% if message.tags %} class="{{ message.tags }} list-group-item list-group-item-primary"{% endif %}>{{ message }}</li>
         {% endfor %}
      </ul>
      {% endif %}
 

   Por ejemplo cuando el usuario Edite un registro o beerpub, se le va mostrar un mensaje diciendo que la operación ha sido realizada correctamente, este mensaje también le va aparecer cuando Crea o Elimina un registro.

- La carpeta uploads
Debemos de crear una carpeta para las imágenes de cada Registro que el usuario crea, yo le pondré de nombre uploads a esta carpeta y la creamos dentro de la carpeta beerpub > static > uploads.

- Desplegando Django REST Framework
Existe una herramienta muy usada para crear APIs REST en Django, esta se llama Django REST Framework y para poder usarla debemos instalarla ejecutando el siguiente comando en nuestra consola de comandos.
 
      pip install djangorestframework 

- Abro el archivo serializers.py y dentro de el importo Django REST Framework y mi modelo beerpub. Asimismo creo una clase llamada BeerpubSerializer y le paso el modelo Serializer de Django REST Framework, debajo uso el modelo Beerpub, defino los campos que quiero enviar a mi Endpoint /beerpub y le indico que no es necesario escribir un id de un registro para poder obtener los datos.

- Dentro del archivo views.py importo algunos elementos que son importantes y necesarios para que el API REST funcione sin problemas, entre estas importaciones llamamos a la clase BeerpubSerializer que creamos anteriormente dentro del archivo serializers.py, también llamo al modelo Beerpub y a otros elementos.

   Asimismo creo un ViewSet con el nombre de clase BeerpubViewSet y dentro de el voy a llamar a los datos ordenándolos por id y le paso la clase BeerpubSerializer.

- Inicio el servidor local de Django Framework.
 
Comando para iniciar el servidor local de Django Framework 
      
      python manage.py runserver 
 
   Y si pruebo nuestra APIs REST, hago una solicitud de tipo GET a mi Endpoint http://localhost:8000/api/, pues me lista los datos en formato JSON.

- ESTRUCTURA DEL DIRECTORIO 

 
      /TPO2_backEnd 
      ├── /appBeerPub
         ├── /_pycache_ 
            ├── _init_.py   
            ├── asgi.py
            ├── setting.py 
            ├── urls.py 
            ├── wsgi.py 
      ├── /.miev  
      ├── /beerpub
            ├── /_pycache_ 
            ├── /migrations 
            ├── /static
               ├── /css
               ├── /js
               ├── /media
               ├── /uploads
            ├── /templantes
               ├── beerpub
                  ├── acercade.html
                  ├── actualizar.html
                  ├── contacto.html
                  ├── crear.html
                  ├── detalles.html
                  ├── faq.html
                  ├── index.html
                  ├── localizacion.html
                  ├── momentos.html
            ├── _init_.py       
            ├── admin.py
            ├── apps.py 
            ├── models.py 
            ├── router.py
            ├── serializers.py 
            ├── tests.py 
            ├── views.py  
            ├── viewsets.py    
      ├── /sql
         ├── beerpub.pdf.pdf
         ├── beerpub.sql
      ├── /TPO-BACK END 
         ├── TPO.TXT
      ├── db.sqlite3
      ├── manage.py
      ├── readme.md
      ├── requirements.txt

 ## Nombre del Grupo
 ***
      Grupo N° 24
      Comision N° 23507
      Full Stack Python*

 ## Integrantes del Grupo
 ***
   1. Julio Maldonado
   2. Leonardo G. Suppa
   


