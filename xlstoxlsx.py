import os
import pyexcel as p

#Ingresa el directorio donde estan los archivos .xls
path = input("Ruta: ")

#Une la ruta del directorio con xlsx, para luego crear la carpeta
savepath = os.path.join(path,"xlsx")
os.mkdir(savepath)

#Guarda en la variable folder la lista con todos los archivos existentes en la carpeta
folder = os.listdir(path)

#Recorre cada archivo
for i in folder:
    
    #Separa el nombre del archivo de su extension
    root, ext=os.path.splitext(i)

    #Si el archivo es xls, lo guarda como xlsx dentro de la carpeta creada anteriormente
    if ext==".xls":
        p.save_book_as(file_name=f"{path}"+i,dest_file_name=f"{savepath}/"+i+'x')