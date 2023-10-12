import os
import cv2
from codigos_py import app
import matplotlib.pyplot as plt

imagem_processada, arq_l = app.file_storage(256, 4, 127, pasta_saida)

img1 = cv2.imread("README_FILES/Imagens_processadas/senoide-256.png")

if img1 is not None:
    print(f"Arquivo 1 encontrado")
else:
    print(f"Arquivo 1 nao encontrado")

l1 = img1[0, :][:, 0]
l2 = arq_l[0, :]

diferenca = abs(l1 - l2)

profile = diferenca.sum(axis=0)

plt.plot(diferenca)
plt.xlabel("Coluna")
plt.ylabel("Diferença")
plt.title("Perfil da Diferença entre as Imagens")
plt.show()
