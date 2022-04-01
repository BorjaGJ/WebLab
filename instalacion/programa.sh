#!/usr/bin/env bash
while true
do
    echo "-------------- MENU ----------------"
    echo "1 crear entorno virtual"
    echo "2 arrancar entorno virtual"
    echo "3 instalar paquetes requirements del proyecto"
    echo "4 comprobar paquetes instalados"
    echo "5 crear archivo.conf"
    echo "6 activar archivo.conf"
    echo "7 desactivar archivo.conf"
    echo "8 crear archivo.wsgi"
    echo "9 migracion base datos"
    echo "10 cambiar propietario del proyecto a www-data"
    echo "11 actualizar proyecto (git pull)"
    echo "12 crear superuser"
    echo "13 install nginx"
    echo "0 salir"
    echo "-------------- MENU ----------------"

    echo "Elija una opcion del menu:"

    read opcion
    case $opcion in

        0)
        echo "------------------------------------------"
        echo "Saliendo"
        exit 1
        ;;


        1)
        echo "------------------------------------------"
        echo "Ruta entorno:" ${RUTA_ENTORNO}

        # creamos el directorio para los entornos en caso de que no esten
        if [ ! -d ${RUTA_ENTORNO} ]
        then
            echo "El directorio del entorno no existe, creando directorio"
            mkdir -p "${RUTA_ENTORNO}"
        fi

        # creamos el entornovirtual
        echo "Creando entorno virtual"
        virtualenv ${RUTA_ENTORNO}${NOMBRE_ENTORNO}
        echo "------------------------------------------"
        ;;



        2)
        # arrancamos el entornovirtual
        echo "------------------------------------------"
        echo "para dejar iniciado el entorno virtual despues de cerrar, debe iniciar este script con SOURCE delante"
        source ${RUTA_ENTORNO}${NOMBRE_ENTORNO}/bin/activate
        echo "entorno iniciado"
        echo "------------------------------------------"
        ;;


        3)
        echo "------------------------------------------"
        if [ $VIRTUAL_ENV ]
        then
            pip install -r ${DIRECTORIO_PROYECTO}requirements
        else

            echo "Debe iniciar el entorno virtual (opcion 2)"

        fi
        echo "------------------------------------------"
        ;;


        # opcion para ver los paquetes que tiene instalado el virtualenv
        4)
        echo "------------------------------------------"
        if [ $VIRTUAL_ENV ]
        then
            pip freeze
        else
            echo "Debe iniciar el entorno virtual (opcion 2)"

        fi
        echo "------------------------------------------"
        ;;



        # opcion para crear el archivo de apache
        5)
        echo "------------------------------------------"
        . ${DIRECTORIO_PROYECTO}instalacion/archivo_conf
        echo "------------------------------------------"
        ;;


        # opcion para arrancar un archivo conf de apache
        6)
        a2ensite ${NOMBRE_ENTORNO}.conf
        service apache2 restart
        ;;


        # opcion para desactivar un archivo conf de apache
        7)
        a2dissite ${NOMBRE_ENTORNO}.conf
        service apache2 restart
        ;;

        # opcio para crear archivo wsgi para apache
        8)
        . ${DIRECTORIO_PROYECTO}instalacion/archivo_wsgi
        ;;

        # opcion para migrar la base de datos
        9)
        echo "------------------------------------------"
        if [ $VIRTUAL_ENV ]
        then
            python ${DIRECTORIO_PROYECTO}manage.py makemigrations
            python ${DIRECTORIO_PROYECTO}manage.py migrate
        else
            echo "Debe iniciar el entorno virtual (opcion 2)"

        fi
        echo "------------------------------------------"
        ;;

        #opcion para cambiar permisos del directorio raiz a www-data
        10)
        chown -R www-data:www-data ${DIRECTORIO_PROYECTO}
        ;;

        11)

        ;;

        # opcion para ver los paquetes que tiene instalado el virtualenv
        12)
        echo "------------------------------------------"
        if [ $VIRTUAL_ENV ]
        then
            python manage.py createsuperuser
        else
            echo "Debe iniciar el entorno virtual (opcion 2)"

        fi
        echo "------------------------------------------"
        ;;

        13)
         echo "------------------------------------------"
         sudo apt install nginx
         sudo ufw allow 'Nginx HTTP'
        echo "------------------------------------------"
        ;;



    esac
done

