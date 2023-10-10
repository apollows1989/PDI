# Exercícios de Processamento Digital de Imagens (PDI)

## Exercício 2.2 - Programa regions (negativo de uma região)

<p align = "Justify">&nbsp &nbsp &nbsp Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa regions.cpp. Esse programa deverá solicitar ao usuário as coordenadas de dois pontos P1 e P2 localizados dentro dos limites do tamanho da imagem e exibir que lhe for fornecida. Entretanto, a região definida pelo retângulo de vértices opostos definidos pelos pontos P1 e P2 será exibida com o negativo da imagem na região correspondente. O efeito é ilustrado na Figura 1.
</p>
<p align = "CENTER">Figura 01 </br> <img src="/README_FILES/Imagens_geral/Exemplo 2.2.png"></p>

</br>

<p align = "Justify">&nbsp &nbsp &nbsp Para a resolução desse problema, eu criei uma função chamada regions_gray() e regions_color(). Essas duas funções tem a mesma finalidade de inverter as cores de uma região da imagem através de dois pontos passados como parâmetro. Para esse exemplo, eu optei por escolher a função regions_color() para fazer o processamento de uma imagem colorida. 
</p>

'''
def regions_color(img, pi, pf):

    y = img.shape[0]
    x = img.shape[1]

    ai = pi[0]
    af = pf[0]
    bi = pi[1]
    bf = pf[1]

    if(ai<0 or af>x or bi<0 or bf>y) :
        print('Intervalo invalido')
        return


    for i in range(ai, af):
        for j in range(bi, bf):
            b, g, r = img[j,i]
            img[j,i] = ((255 - img[j,i][0]), (255 - img[j,i][1]), (255 - img[j,i][2]))

    return img

'''
