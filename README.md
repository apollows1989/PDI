# Exercícios de Processamento Digital de Imagens (PDI)

## Exercício 2.2 - Programa regions (negativo de uma região)

<p align = "Justify">&nbsp &nbsp &nbsp Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa regions.cpp. Esse programa deverá solicitar ao usuário as coordenadas de dois pontos P1 e P2 localizados dentro dos limites do tamanho da imagem e exibir que lhe for fornecida. Entretanto, a região definida pelo retângulo de vértices opostos definidos pelos pontos P1 e P2 será exibida com o negativo da imagem na região correspondente. O efeito é ilustrado na Figura 1.
</p>
<p align = "CENTER">Figura 01 </br> <img src="/README_FILES/Imagens_geral/Exemplo 2.2.png"></p>

</br>

<p align = "Justify">&nbsp &nbsp &nbsp Para a resolução desse problema, eu criei uma função chamada regions_gray() e regions_color(). Essas duas funções tem a mesma finalidade de inverter as cores de uma região da imagem através de dois pontos passados como parâmetro. Para esse exemplo, eu optei por escolher a função regions_color() para fazer o processamento de uma imagem colorida. 
</p>

```

def regions_color(img, pi, pf):

    # Começamos colotando as dimensões da imagems ( largura e altura) e armazenando nas variáveis x e y.

    y = img.shape[0]
    x = img.shape[1]

    # Depois disso eu defini, a partir dos pontos pi e pf, o intervalo onde será aplicado o efeito através das variáveis ai, af, pi, pf.
    ai = pi[0]
    af = pf[0]
    bi = pi[1]
    bf = pf[1]

    # Caso o intervalo seja informado errado, a função irá retorna nulo.
    if ai < 0 or af > x or bi < 0 or bf > y:
        print("Intervalo invalido")
        return

    # Com o intervalo definido, criei um laço para percorrer a imagem e para cada pixels (img[j][i]) apliquei o efeito.
    # Como a imagem é colorida, o efeito teve que ser aplicado para cada camada de cor da matriz img[][].
    for i in range(ai, af):
        for j in range(bi, bf):
            img[j, i] = (
                (255 - img[j, i][0]),
                (255 - img[j, i][1]),
                (255 - img[j, i][2]),
            )

    return img
```
