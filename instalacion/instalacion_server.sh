#!/bin/bash
NOMBRE_ENTORNO=weblab
# finalizar con la barra siempre que sea directorios
RUTA_ENTORNO=/var/www/entornos
DIRECTORIO_PROYECTO=/var/www/weblab/
ARCHIVO_WSGI=${DIRECTORIO_PROYECTO}configuracion/apache.wsgi


# creacion del archivo de configuracion de apache
ARCHIVO_CONF_NGINX=/etc/nginx/sites-available/${NOMBRE_ENTORNO}.conf

SERVER_NAME=weblab.desarrollobinario.com
SERVER_ALIAS=weblab.desarrollobinario.com


ARCHIVO_LOG=/root/${NOMBRE_ENTORNO}.log


source ${DIRECTORIO_PROYECTO}instalacion/programa.sh

