# pylint: disable=invalid-name
# Este arquivo serve apenas para testar as funções de cada exercício. Para facilitar, criei funções
# para cada processo, como negativar um trecho de uma imagem,
# ou contar quantos objetos tem em uma imagem.

import os
import cv2

# Adicionando as funções python dos exercícios que se encontram na pasta "codigos_py"
from codigos_py import app

arq_path = "README_FILES/Imagens_geral"

pasta_saida = "README_FILES/Imagens_processadas"

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Lendo o arquivo "Diogo.jpg"
img = app.load_image(f"README_FILES/Imagens_geral/Diogo.jpg", "COLOR")

# Coletando as dimensões da imagem
y = img.shape[0]
x = img.shape[1]

# Aplicando a função regions.py em uma região retangular no meio da imagem
imagem_processada = app.regions_color(img, (x // 4, y // 4), (3 * x // 4, 3 * y // 4))

# Salvando a imagem processada na pasta "README_FILES/Imagens_processadas"
cv2.imwrite(f"README_FILES/Imagens_processadas/Diogo.jpg", imagem_processada)
