import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx
#trocar a barras "\" para assim "/"
from_dir = "C:/Users/Familia Nociti/Downloads"  #pasta de origem         
to_dir = "C:/Users/Familia Nociti/Downloads"   #pasta de destino

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Mova todos os arquivos de imagem da pasta Downloads para outra pasta
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        print(name)
        continue
    if extension in ['.doc', '.pdf', '.docx','.txt', '.PDF']:
       path1 = from_dir + '/' + file_name 
       path2 = to_dir + '/' + "Documentos"
       path3 = to_dir + '/' + "Documentos" + '/' + file_name
       
       if os.path.exists(path2):
         print("Movendo" + file_name + ".....")
         shutil.move(path1,path3)
       else:
         os.makedirs(path2)
         print("Movendo" + file_name + ".....")
         shutil.move(path1,path3)