import os
import cv2
from codigos_py import app

arq_path = "README_FILES/Imagens_geral"
pasta_saida = "README_FILES/Imagens_processadas"

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

img = app.load_image(f"README_FILES/Imagens_geral/desafio-esteganografia.png", "COLOR")

img_msb = app.esteganografia_msb(img)
img_lsb = app.esteganografia_lsb(img)

cv2.imwrite(f"{pasta_saida}/esteganografia_msb.png", img_msb)
cv2.imwrite(f"{pasta_saida}/esteganografia_lsb.png", img_lsb)
