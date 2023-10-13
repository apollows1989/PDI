# Exercícios de Processamento Digital de Imagens (PDI)
#### Todas as funções dos exercícios estão dentro do arquivo app.py dentro da pasta codigos_py
</br>

* ## Exercício 2.2 - Programa regions (negativo de uma região)

<p align = "Justify">&nbsp &nbsp &nbsp <i>Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa regions.cpp. Esse programa deverá solicitar ao usuário as coordenadas de dois pontos P1 e P2 localizados dentro dos limites do tamanho da imagem e exibir que lhe for fornecida. Entretanto, a região definida pelo retângulo de vértices opostos definidos pelos pontos P1 e P2 será exibida com o negativo da imagem na região correspondente. O efeito é ilustrado na Figura 1.</i></p>
<p align = "CENTER">Figura 01 </br> <img src="/README_FILES/Imagens_geral/Exemplo 2.2.png"></p>

</br>
</br>

<p align = "Justify">&nbsp &nbsp &nbsp Para a resolução desse problema, eu criei uma função chamada regions_gray() e regions_color(). Essas duas funções tem a mesma finalidade de inverter as cores de uma região da imagem através de dois pontos passados como parâmetro. Para esse exemplo, eu optei por escolher a função regions_color() para fazer o processamento de uma imagem colorida. 
</p>


```
def regions_color(img, pi, pf):

    y = img.shape[0]
    x = img.shape[1]

    ai = pi[0]
    af = pf[0]
    bi = pi[1]
    bf = pf[1]

    if ai < 0 or af > x or bi < 0 or bf > y:
        print("Intervalo invalido")
        return

    for i in range(ai, af):
        for j in range(bi, bf):
            img[j, i] = (
                (255 - img[j, i][0]),
                (255 - img[j, i][1]),
                (255 - img[j, i][2]),
            )

    return img
```
</br>
</br>
<p>Explicação do código:</p>

</br>
<p>Começamos colotando as dimensões da imagems ( largura e altura) e armazenando nas variáveis x e y.</p> 
   
```
    y = img.shape[0]
    x = img.shape[1]
```

</br>
<p>Depois disso eu defini, a partir dos pontos pi e pf, o intervalo onde será aplicado o efeito através das variáveis ai, af, pi, pf.</p>

```
    ai = pi[0]
    af = pf[0]
    bi = pi[1]
    bf = pf[1]
```

</br>
<p>Caso o intervalo seja informado errado, a função irá retorna nulo.</p>

```
    if ai < 0 or af > x or bi < 0 or bf > y:
        print("Intervalo invalido")
        return
```

</br>
<p>Com o intervalo definido, criei um laço para percorrer a imagem e para cada pixels apliquei o efeito. Como a imagem é colorida, o efeito teve que ser aplicado para cada camada de cor da matriz img[][].</p>

```
    for i in range(ai, af):
        for j in range(bi, bf):
            img[j, i] = (
                (255 - img[j, i][0]),
                (255 - img[j, i][1]),
                (255 - img[j, i][2]),
            )

    return img
```
</br>

<p align = "Justify">Para testar a função, criei o arquivo exercicio2.2.py para testar a função, onde nele eu carrego uma imagem e aplico a função regions_color(). O resultado do processamento obtido esta representado na figura 02 </p>

```
import os
import cv2
from codigos_py import app

arq_path = "README_FILES/Imagens_geral"

pasta_saida = "README_FILES/Imagens_processadas"

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

img = app.load_image(f"README_FILES/Imagens_geral/Diogo.jpg", "COLOR")

y = img.shape[0]
x = img.shape[1]

imagem_processada = app.regions_color(img, (x // 4, y // 4), (3 * x // 4, 3 * y // 4))

cv2.imwrite(f"README_FILES/Imagens_processadas/Diogo.jpg", imagem_processada)
```

</br>
<p align = "CENTER">Figura 02 </br> <img src="/README_FILES/Imagens_processadas/Diogo.jpg"></p>

</br>
</br>

* ## Exercício 2.3 - Programa trocaregioes (trocar as diagonais)
<p align = "Justify">&nbsp &nbsp &nbsp<i> Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa trocaregioes. Seu programa deverá trocar os quadrantes em diagonal na imagem. Explore o uso da classe Mat e seus construtores para criar as regiões que serão trocadas. O efeito é ilustrado na Figura 3.</i></p>

<p align = "CENTER">Figura 03 </br> <img src="/README_FILES/Imagens_geral/Exemplo 2.3.png"></p>

</br>
</br>

<p align = "Justify">Tendo como base o programa fornecido pelo professor, criei a função trocaregioes, onde a função recebe uma imagem como parametro e retorna a imagem com os quadrantes em diagonal trocado </p>

```
def trocaregioes(image):

    y = image.shape[0]
    x = image.shape[1]

    img_proc = image.copy()

    img1 = image[0 : y // 2, 0 : x // 2]
    img2 = image[0 : y // 2, x // 2 : x]
    img3 = image[y // 2 : y, 0 : x // 2]
    img4 = image[y // 2 : y, x // 2 : x]

    for i in range(0, img1.shape[1]):
        for j in range(0, img1.shape[0]):
            img_proc[j + y // 2, i + x // 2] = img1[j, i]

    for i in range(0, img2.shape[1]):
        for j in range(0, img2.shape[0]):
            img_proc[j + y // 2, i] = img2[j, i]

    for i in range(0, img3.shape[1]):
        for j in range(0, img3.shape[0]):
            img_proc[j, i + x // 2] = img3[j, i]

    for i in range(0, img4.shape[1]):
        for j in range(0, img4.shape[0]):
            img_proc[j, i] = img4[j, i]

    return img_proc
```
</br>
</br>
<p align = "Justify">Explicação do código:</p>
</br>

<p>Começamos colotando as dimensões da imagems ( largura e altura) e armazenando nas variáveis x e y.</p> 

```
    y = img.shape[0]
    x = img.shape[1]
```
</br>
<p>Fiz uma cópia do arquivo para não alterar a original.</p> 

```
    img_proc = image.copy()
```
</br>
<p align = "Justify"> Aqui criei quatro matrizes que representa os quadrantes da imagem, basicamente recortar a imagem em 4 partes e os armazenei em quatro variáveis, sendo uma para cada quadrante, onde a variável img1 representa o quadrante superior esquerdo, o img2 representa o quadrante superior direito, o img3 o quadrante inferior esquerdo e por último o img4 que representa o quadrante inferior direito.</p> 

```
    img1 = image[0 : y // 2, 0 : x // 2]
    img2 = image[0 : y // 2, x // 2 : x]
    img3 = image[y // 2 : y, 0 : x // 2]
    img4 = image[y // 2 : y, x // 2 : x]
```
</br>
<p align = "Justify"> Por fim, fiz quatro laços para percorrer os 4 quadrantes da imagem, trocando o quadrante img1 por img4 e o img2 por img3 e armazenando na variável img_proc. </p> 

```
for i in range(0, img1.shape[1]):
        for j in range(0, img1.shape[0]):
            img_proc[j + y // 2, i + x // 2] = img1[j, i]

    for i in range(0, img2.shape[1]):
        for j in range(0, img2.shape[0]):
            img_proc[j + y // 2, i] = img2[j, i]

    for i in range(0, img3.shape[1]):
        for j in range(0, img3.shape[0]):
            img_proc[j, i + x // 2] = img3[j, i]

    for i in range(0, img4.shape[1]):
        for j in range(0, img4.shape[0]):
            img_proc[j, i] = img4[j, i]
```

</br>
<p align = "Justify">Para testar a função, criei um arquivo exercicio2.3.py, onde nele eu carrego uma imagem e aplico a função trocaregioes(). O resultado do processamento obtido esta representado na figura 04. </p>

```
import os
import cv2
from codigos_py import app

pasta_saida = "README_FILES/Imagens_processadas"

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

img = app.load_image(f"README_FILES/Imagens_geral/Diogo.jpg", "COLOR")

imagem_processada = app.trocaregioes(img)

cv2.imwrite(f"README_FILES/Imagens_processadas/Diogo_trocaregioes.jpg", imagem_processada)
```

<p align = "CENTER">Figura 04 </br> <img src="/README_FILES/Imagens_processadas/Diogo_trocaregioes.jpg"></p>

</br>
</br>

* ## Exercício 3.2 - Programa file_storage (criar uma imagem em espécie de onda)
</br>

<p align = "Justify">&nbsp &nbsp &nbsp<i> Utilizando o programa filestorage.cpp como base, crie um programa que gere uma imagem de dimensões 256x256 pixels contendo uma senóide de 4 períodos com amplitude de 127 desenhada na horizontal, como aquela apresentada na Figura 6 . Grave a imagem no formato PNG e no formato YML. Compare os arquivos gerados, extraindo uma linha de cada imagem gravada e comparando a diferença entre elas. Trace um gráfico da diferença calculada ao longo da linha correspondente extraída nas imagens. O que você observa?</i></p>

</br>

<p align = "Justify">&nbsp &nbsp &nbsp Com a função file_storage fornecida pelo professor, refiz ela em python e executei para gerar a imagem como solicitado no exercício. O resultado pode ser visto na figura 5.</p>

```
def file_storage(SIDE, PERIODS, AMPLITUDE):
    ss_img = f"senoide-{SIDE}.png"
    ss_yml = f"senoide-{SIDE}.yml"

    image = np.zeros((SIDE, SIDE), dtype=np.float32)

    for i in range(SIDE):
        for j in range(SIDE):
            image[i, j] = AMPLITUDE * math.sin(2 * math.pi * PERIODS * j / SIDE) + AMPLITUDE + 1

    fs = cv2.FileStorage(ss_yml, cv2.FILE_STORAGE_WRITE)
    fs.write("mat", image)
    fs.release()

    cv2.normalize(image, image, 0, 255, cv2.NORM_MINMAX)
    image = image.astype(np.uint8)

    cv2.imwrite(ss_img, image)

    fs = cv2.FileStorage(ss_yml, cv2.FILE_STORAGE_READ)
    image = fs.getNode("mat").mat()
    fs.release()

    cv2.normalize(image, image, 0, 255, cv2.NORM_MINMAX)
    image = image.astype(np.uint8)

    return image
```
</br>
<p align = "CENTER">Figura 04 </br> <img src="/README_FILES/Imagens_processadas/Diogo_trocaregioes.jpg"></p>

