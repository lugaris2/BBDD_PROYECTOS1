Smart city
Descripción del proyecto: Estamos creando una aplicación para controlar unos sensores que nos dan información sobre varios items de salubridad y otros
Guía de inicio rápido: Preparamos un docker-compose.ymly lo ejecutamos desde la consola de Docker
  Define los servicios (contenedores) que forman parte de tu aplicación.
  Especifica imágenes, volúmenes, redes, variables de entorno, puertos, etc.
  Permite levantar todo el entorno con un único comando:  docker-compose up
  Crear los sensores mediante Archivo py al que le pasamos un json dentro de un array y un for para crear las entidades de una en una, ya que no permite hacerlo con todas a la vez.
  Creamos una suscripción en Orion es como decirle: “Avísame cuando cambie algo en esta entidad o atributo.”
  patch: hemos creado un patch para cargar de forma aleatorio y automática 400 registros en crate, modificando su fecha para distinguir unos de otros y poder accedr a ellos por fecha a posteriori
