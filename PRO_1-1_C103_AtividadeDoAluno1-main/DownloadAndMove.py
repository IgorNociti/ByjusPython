import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "DIGITE O CAMINHO DA PASTA DE DOWNLOAD (USE " / ") no VSC"
# to_dir = "DIGITE A PASTA DE CAMINHO DE DESTINO (USE " / ") no VSC"

from_dir = "C:/Users/Familia Nociti/Downloads"
to_dir = "C:/Users/Familia Nociti/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,extension = os.path.splitext(event.src_path)
        
        time.sleep(1)
        for key, value in dir_tree.items():
            
            file_name = os.path.basename(event.src_path)
            
            print("Baixando" + file_name)
            
            path = from_dir + '/' + file_name 
            path = to_dir + '/' + key
            path = to_dir + '/' + key + '/' + file_name
            
            time.sleep(1)
            if os.path.exists(path2):
                
                print("Diretório Extistente..")
                time.sleep(1)
                
                if os.path.existst(path3):
                    
                    print("Arquivo Já Existe em  " + key + "....")
                    print("Renomeando Arquivo " + file_name + "....")

                    new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0, 999)) + os.path.splitext(file_name)[1]

                    path4 = to_dir + '/' + key + '/' + new_file_name

                    print("Movendo " + new_file_name + "....")
                    shutil.move(path1, path4)
                    time.sleep(1)
                    
                else:
                    print("Movendo" + file_name + "...")
                    shutil.sleep(1)
            else:
                print("Criando Diretório...")
                os.makedirs(path2)
                print("Movendo" + file_name + "...")
                shutil.move(path1, path3)
                time.sleep(1)
                    

# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()


while True:
    time.sleep(2)
    print("executando...")
    
