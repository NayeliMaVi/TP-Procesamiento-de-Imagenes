import os
import shutil
carpeta_origen1 = "TP procesamiento//dataset_original_1//data//anime_images//A Silent Voice"
carpeta_origen2 = "TP procesamiento//dataset _original_2//test_set//test_set//cats"

carpeta_destino = "TP procesamiento//dataset"

subcarpeta_destino1 = os.path.join(carpeta_destino, "dataset1")
subcarpeta_destino2 = os.path.join(carpeta_destino, "dataset2")
os.makedirs(subcarpeta_destino1, exist_ok=True)
os.makedirs(subcarpeta_destino2, exist_ok=True)


def copiar_primeras_cincuenta_imagenes(carpeta_origen, subcarpeta_destino):
    
    archivos = os.listdir(carpeta_origen)
    contador = 0
    
    for archivo in archivos:        
        if archivo.endswith((".jpg", ".jpeg", ".png")):
            ruta_origen = os.path.join(carpeta_origen, archivo)
            ruta_destino = os.path.join(subcarpeta_destino, archivo)
            shutil.copyfile(ruta_origen, ruta_destino)
            contador += 1
            if contador == 50:
                break


copiar_primeras_cincuenta_imagenes(carpeta_origen1, subcarpeta_destino1)
copiar_primeras_cincuenta_imagenes(carpeta_origen2, subcarpeta_destino2)
