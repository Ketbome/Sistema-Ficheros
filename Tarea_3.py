import os
import shutil
import pathlib


class Tree(object):
    def __init__(self, name, ruta, padre=None):
        self.name = name
        self.ruta = ruta+"/"+name
        self.ruta_padre = ruta
        self.padre = None
        if (padre):
            self.padre = padre
        self.carpetas = {}
        self.archivos = {}
        if not os.path.exists(self.ruta):
            os.mkdir(self.ruta, 0o777)

    def borrar(self):
        if os.path.exists(self.ruta):
            shutil.rmtree(self.ruta)

    def listdir(self, agregado):
        lista = []
        ls = ['-i', '-R']
        if agregado == ls[0]:
            for i in self.carpetas:
                lista.append(i)
            for i in self.archivos:
                lista.append(i)
            for i in lista:
                try:
                    ruta = self.carpetas[i].ruta
                    print(str(os.stat(ruta).st_ino)+". "+i)
                except:
                    ruta = self.archivos[i].ruta
                    print(str(os.stat(ruta).st_ino)+". "+i)
        elif agregado == ls[1]:
            # recorrido por el Arbol
            print("----------------------ARBOL--------------------------")
            for i in self.archivos:
                print(self.name+"->"+i)
            for i in self.carpetas:
                print(self.name+"->"+i)
                print("-----------")
                recur(self.carpetas[i])
            print("---------------------FISICO--------------------------")
            for root, dirs, files in os.walk(self.ruta, topdown=False):
                for name in files:
                    print(os.path.join(root, name))
                for name in dirs:
                    print(os.path.join(root, name))
            print("------------------Termino ls -R-----------------------")
        elif agregado == "nada":
            for i in self.carpetas:
                lista.append(i)
            for i in self.archivos:
                lista.append(i)
            lista.sort()
            for i in lista:
                print(i)  # ls en orden alfabetico

    def mkdir(self, carpeta):
        #path = os.path.join(self.ruta, carpeta)
        carp = Tree(carpeta, self.ruta, self)
        self.carpetas[carpeta] = carp
        if not os.path.exists(self.ruta):
            os.mkdir(self.ruta, 0o777, dir_fd=None)

    def remove(self, name):  # Directorios completos incluyendo todo
        try:
            if self.carpetas[name]:
                path = os.path.join(self.ruta, name)
                shutil.rmtree(path)
                self.carpetas.pop(name)
        except:
            try:
                if self.archivos[name]:
                    path = os.path.join(self.ruta, name)
                    os.remove(path)
                    self.archivos.pop(name)
            except:
                print("No encontrado o no existe")

    def touch(self, archivo):
        archi = Archivo(archivo, self.ruta)
        self.archivos[archivo] = archi
        arch = os.path.join(self.ruta, archivo)
        pathlib.Path(arch).touch()

    def move(self, aux_r, name, hacia):
        desde = self.ruta+"/"+name
        array_desde = desde.split("/")
        array_hacia = hacia.split("/")

        n1 = len(array_desde)
        n2 = len(array_hacia)
        aux_r2 = aux_r

        i = 0
        while (i < n2):
            if (array_hacia[i] == "Main"):
                #num = n2 - i
                i += 1
                while (i < n2):
                    try:
                        aux_r = aux_r.carpetas[array_hacia[i]]
                    except:
                        archi = Archivo(str(array_hacia[i]), hacia)
                        aux_r.archivos[str(array_hacia[i])] = archi
                    i += 1
            i += 1

        i = 0
        while (i < n1):
            if (array_desde[i] == "Main"):
                #num = n2 - i
                i += 1
                while (i < n1):
                    try:
                        aux_r2 = aux_r2.carpetas[array_desde[i]]
                    except:
                        aux_r2.archivos.pop(array_desde[i])
                    i += 1
            i += 1
        print(desde)
        print(hacia)
        # pathlib.Path(desde).rename(hacia)
        shutil.move(desde, hacia)


class Archivo(object):
    def __init__(self, name, ruta):
        self.name = name
        self.ruta = ruta + "/" + name

    def nueva_ruta(self, ruta):
        self.ruta = ruta+'/'+self.name


def recur(ruta):
    for i in ruta.archivos:
        print(ruta.name+"->"+i)
    for i in ruta.carpetas:
        print(ruta.name+"->"+i)
        print("-----------")
        recur(ruta.carpetas[i])


# https://docs.python.org/es/3.8/library/os.path.html
def main():
    ruta = pathlib.Path().absolute()

    raiz = Tree("Main", str(ruta))
    aux = raiz
    while (1):
        bash = str(input(aux.ruta+"$ "))
        aux_bash = bash.split(" ")
        if (aux_bash[0] == "cd"):
            try:
                name = aux_bash[1]
                if (name == ".."):
                    if (aux.padre):
                        aux = aux.padre
                elif (name in aux.carpetas):
                    aux = aux.carpetas[name]
            except:
                print("Error comando cd")
        elif (aux_bash[0] == "exit"):
            break
        else:
            if (aux_bash[0] == "ls"):
                if len(aux_bash) == 2:
                    aux.listdir(aux_bash[1])
                else:
                    aux.listdir("nada")
            elif (aux_bash[0] == "mkdir"):
                aux.mkdir(aux_bash[1])
            elif (aux_bash[0] == "rm"):
                aux.remove(aux_bash[1])
            elif (aux_bash[0] == "touch"):
                aux.touch(aux_bash[1])
            elif (aux_bash[0] == "mv"):
                print(aux.move(raiz, str(aux_bash[1]), str(aux_bash[2])))
            else:
                print("Comando no encontrado o mal puesto")
    raiz.borrar()


if __name__ == "__main__":
    main()
