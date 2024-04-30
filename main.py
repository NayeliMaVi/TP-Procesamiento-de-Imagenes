import cv2
import numpy as np
import os

# Directorio que contiene las imágenes
dir1 = "TP procesamiento//dataset//dataset1"
dir2 = "TP procesamiento//dataset//dataset2"

def similitudCoseno(vec1,vec2):
     return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def extraerHistogramaNormalizado (imagen):
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    r = cv2.calcHist([imagen_rgb], [0], None, [256], [0, 256])
    g = cv2.calcHist([imagen_rgb], [1], None, [256], [0, 256])
    b = cv2.calcHist([imagen_rgb], [2], None, [256], [0, 256])
    # Normalizar los histogramas
    r_normalizado = cv2.normalize(r, None, 0, 1, cv2.NORM_MINMAX)
    g_normalizado = cv2.normalize(g, None, 0, 1, cv2.NORM_MINMAX)
    b_normalizado = cv2.normalize(b, None, 0, 1, cv2.NORM_MINMAX)

    return r_normalizado.flatten(),g_normalizado.flatten(),b_normalizado.flatten()


imagenes_dataset1 = []
for archivo in os.listdir(dir1):
    if archivo.endswith(".jpg"):
        ruta = os.path.join(dir1, archivo)
        imagen = cv2.imread(ruta)
        imagenes_dataset1.append((archivo, imagen))

imagenes_dataset2 = []
for archivo in os.listdir(dir2):
    if archivo.endswith(".jpg"):
        ruta = os.path.join(dir2, archivo)
        imagen = cv2.imread(ruta)
        imagenes_dataset2.append((archivo, imagen))


for i, (nombre_d1, imagen_d1) in enumerate(imagenes_dataset1):
    nombre_d2, imagen_d2 = imagenes_dataset2[i]

    # Calcular los histogramas normalizados para las imágenes
    hist_r_perro, hist_g_perro, hist_b_perro = extraerHistogramaNormalizado(imagen_d1)
    hist_r_gato, hist_g_gato, hist_b_gato = extraerHistogramaNormalizado(imagen_d2)

    # Calcular la similitud de coseno para cada canal de color
    similarity_r = similitudCoseno(hist_r_perro, hist_r_gato)
    similarity_g = similitudCoseno(hist_g_perro, hist_g_gato)
    similarity_b = similitudCoseno(hist_b_perro, hist_b_gato)

    # Similitud general promediada entre los canales de color
    overall_similarity = (similarity_r + similarity_g + similarity_b) / 3

    print(f""" Similitud entre  {nombre_d1} y {nombre_d2}:
        Similitud en el color rojo: {similarity_r}
        Similitud en el color verde: {similarity_g}
        Similitud en el color azul: {similarity_b}
        Similitud promedio del histograma de colores: {overall_similarity}
          """)
