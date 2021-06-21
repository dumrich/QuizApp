# QuizApp
Aplicación de prueba de eventos de programación y codificación de Fbla

## Acerca de
El proyecto es una aplicación FBLA Quiz. Tiene la capacidad de iniciar sesión, crear pruebas, realizar pruebas y calificarlas automáticamente.

## Instalación
Solo necesita una herramienta instalada: Docker
1. `git clone` o descargue el zip de este archivo y extráigalo. `cd` en ese directorio recién creado.
2. `docker-compose up --build`.
3. ¡Y ya está! Visite `localhost: 8000` para ver el sitio web. Para detener el servidor, ingrese `Ctrl-c`.

## Uso del sitio web
Cuando vaya a `localhost: 8000`, será redirigido a una página de inicio de sesión. Puede registrarse haciendo clic en el botón de registro en la barra de navegación. Una vez hecho esto, puede hacer clic en crear una prueba para crear una nueva prueba. Agregue un nombre y una descripción (opcional) y haga clic en crear.

 - * Edición de una prueba *
 En la vista de lista principal, haga clic en un título. Luego, dado que eres el propietario, haz clic en el botón editar. Ahora, debería ver todas las preguntas. Agregue una pregunta usando el formulario. También puede eliminar preguntas haciendo clic en el botón Eliminar. Para muchas preguntas, importe desde un archivo `* .json *`.
 
 - * Eliminar una prueba *
 Para eliminar, vuelva a la vista detallada del cuestionario. Haga clic en el botón grande de eliminar junto a editar. Se le pedirá un modal, y puede aceptarlo.
 
 - * Tomando una prueba *
 En la vista de detalles, haga clic en el botón de inicio. Responda el cuestionario completando la casilla de forma adecuada. Haga clic en enviar.
 
 - * Viendo resultados *
 Una vez enviado, los resultados aparecen automáticamente. Haga clic en ver PDF para encontrar una versión imprimible.
 
## Ampliación del sitio web con funcionalidad avanzada
La lógica detrás del sitio se almacena en el archivo `quiz / views.py`. Manipular eso le permitirá cambiar: Aleatoriedad de preguntas, consultas de bases de datos, requisitos de inicio de sesión, campos PDF, envíos de formularios de inicio de sesión y mucho más. Puede agregar campos de base de datos personalizados manipulando el ORM de Django en el archivo `models.py`. Después de cualquier cambio, ejecute: `docker-compose ejecutar web python manage.py makemigrations` y` docker-compose ejecutar web python manage.py migrate`.

## Que hacer
- [] Agregar WASM a la aplicación web
- [] Corregir presentación
- [] Agregar módulos Rust
- [] Agregar API con Django Rest Framework
- [] Agregar Rust CLI que usa Reqwest

## Colaboradores
Este proyecto fue creado únicamente por Abhinav Chavali, licencia GNU / GPLv3
