import os
import cv2
from codigos_py import app


pasta_saida = "README_FILES/Imagens_processadas"

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

img = app.load_image(f"README_FILES/Imagens_geral/bolhas.png", "COLOR")

img_proc = app.binary_image(img)
img_proc = app.retira_obj_bordas(img)

cv2.imwrite(f"{pasta_saida}/bolhas_s_borda_01.png", img_proc)


