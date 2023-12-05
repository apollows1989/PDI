
import os
from codigos_py import app
import cv2

lista_arq = os.listdir("README_FILES/Imagens_geral")

pasta_saida = "README_FILES/Imagens_processadas"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

for arq in lista_arq:
    img = app.load_image(f"Imagens/{arq}", "COLOR")
    y = img.shape[0]
    x = img.shape[1]

    imagem_processada = app.regions_color(
        img, (x // 4, y // 4), (3 * x // 4, 3 * y // 4)
    )

    cv2.imwrite(f"{pasta_saida}/{arq}", imagem_processada)
    #obj += 1

# img_neg = app.regions_color(img, (20, 20), (300, 300))
# img_trocado = troca_reg.troca_diagonal(img)
# img_neg = app.file_storage(2048, 16)

# cv.imshow("teste",img_neg)
# cv.waitKey(0)
