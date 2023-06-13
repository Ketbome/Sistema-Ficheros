# Sistema de Ficheros

Este es un programa de sistema de ficheros simple que permite crear, administrar y manipular archivos y carpetas. Puedes interactuar con el sistema utilizando comandos similares a los utilizados en la terminal.

## Requisitos

Antes de ejecutar este programa, asegúrate de tener instalado Python en tu sistema.

## Funcionalidades

El programa ofrece las siguientes funcionalidades:

- cd: Cambiar de directorio. Utiliza el comando cd nombre_directorio para navegar a un directorio específico. Puedes usar ".." para ir al directorio padre.
- ls: Listar archivos y carpetas. Utiliza el comando ls para mostrar una lista de los archivos y carpetas en el directorio actual. Puedes agregar las siguientes opciones:
  - i: Muestra una lista de archivos y carpetas con su número de inodo.
  - R: Muestra una lista recursiva de archivos y carpetas en el árbol completo.
- mkdir: Crear una nueva carpeta. Utiliza el comando mkdir nombre_carpeta para crear una nueva carpeta en el directorio actual.
- rm: Eliminar un archivo o carpeta. Utiliza el comando rm nombre para eliminar un archivo o carpeta en el directorio actual.
- touch: Crear un nuevo archivo. Utiliza el comando touch nombre_archivo para crear un nuevo archivo en el directorio actual.
- mv: Mover un archivo o carpeta. Utiliza el comando mv nombre_origen nombre_destino para mover un archivo o carpeta a un nuevo directorio.

## Uso

1. Abre una terminal y navega hasta la ubicación donde se encuentra el archivo del programa.
2. Ejecuta el programa con el comando python nombre_programa.py.
3. Se mostrará un prompt con la ruta del directorio actual.
4. Ingresa los comandos disponibles para interactuar con el sistema de ficheros.

## Ejemplo de Uso

```
/Usuarios/tu_usuario/Proyecto$ ls
archivo1.txt  carpeta1
/Usuarios/tu_usuario/Proyecto$ mkdir carpeta2
/Usuarios/tu_usuario/Proyecto$ ls
archivo1.txt  carpeta1  carpeta2
/Usuarios/tu_usuario/Proyecto$ touch archivo2.txt
/Usuarios/tu_usuario/Proyecto$ ls
archivo1.txt  archivo2.txt  carpeta1  carpeta2
/Usuarios/tu_usuario/Proyecto$ cd carpeta1
/Usuarios/tu_usuario/Proyecto/carpeta1$ ls
archivo3.txt  subcarpeta
/Usuarios/tu_usuario/Proyecto/carpeta1$ cd ..
/Usuarios/tu_usuario/Proyecto$ rm archivo1.txt
/Usuarios/tu_usuario/Proyecto$ ls
archivo2.txt  carpeta1  carpeta2
/Usuarios/tu_usuario/Proyecto$ mv archivo2.txt carpeta1
/Usuarios/tu_usuario/Proyecto$ ls
carpeta1  carpeta2
/Usuarios/tu_usuario/Proyecto$ exit
```

## Notas

- Este programa solo ofrece una funcionalidad básica de sistema de ficheros y no es adecuado para entornos de producción o tareas avanzadas.
- Ten en cuenta que algunas funcionalidades pueden variar según el sistema operativo en el que se ejecute el programa.
