import os
import cv2

# Adicionando as funções python dos exercícios que se encontram na pasta "codigos_py"
from codigos_py import app

pasta_saida = "README_FILES/Imagens_processadas"

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Lendo o arquivo "Diogo.jpg"
img = app.load_image(f"README_FILES/Imagens_geral/Diogo.jpg", "COLOR")

imagem_processada = app.trocaregioes(img)

# Salvando a imagem processada na pasta "README_FILES/Imagens_processadas"
cv2.imwrite(
    f"README_FILES/Imagens_processadas/Diogo_trocaregioes.jpg", imagem_processada
)
