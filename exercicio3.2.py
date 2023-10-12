import os
import cv2
from codigos_py import app

pasta_saida = "README_FILES/Imagens_processadas"

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)


app.file_storage(256, 4, 127, pasta_saida)
