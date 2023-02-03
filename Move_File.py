import os;
import shutil;

from_Dir = 'C:\Users\BRASIL\Downloads'
to_Dir = 'C:\Users\BRASIL\OneDrive\Documentos\Arquivos_Documentos'
list_Files = os.listdir(from_Dir)

print(list_Files)


for fileName in list_Files:
    name, extension = os.path.splitext(fileName)
   
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_Dir + '/' + fileName
        path2 = to_Dir + '/' + "Arquivos_Documentos"
        path3 = to_Dir + '/' + "Arquivos_Documentos" + '/' + fileName

        if os.path.exists(path2):
            print("movendo " + fileName + "...")

            shutil.move(path1, path3)
        else :
            os.makedirs(path2)

            print("movendo " + fileName + "...")

            shutil.move(path1, path3)