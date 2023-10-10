import cv2
import numpy as np
import math

#Carrega uma imagem, verificando se o arquivo foi carregado normalmamente
def load_image(path, _color):
    
    img = cv2.imread(path)
    
    #Verifica se o arquivo foi lido
    if  img is not None: 
        print(f"Arquivo encontrado")
    else:
        print(f"Arquivo nao encontrado") 
        return

    if (_color == 'GRAY_SCALE' or _color == 'COLOR' or _color == 'UNCHANGED') :
        if _color == 'GRAY_SCALE' :     
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) #ler o arquivo em escala de cinza(1 canal)
        elif _color == 'COLOR' :
            img = cv2.imread(path, cv2.IMREAD_COLOR) #ler o arquivo em escala de cinza(1 canal)
        else :
            img = cv2.imread(path, cv2.IMREAD_UNCHANGED) #ler o arquivo em escala de cinza(1 canal)
    else :
        print('Tipo de arquivo invalido!')
        return
 
    return img

#Aumenta o contraste da imagem para evitar que a imagem tenha pixels diferentes de 0 e 255
def binary_image(image):
    
    #Verifica se o arquivo foi lido
    if  image is not None: 
        print(f"Arquivo encontrado")
    else:
        print(f"Arquivo nao encontrado") 
        return
    
    img = image.copy()
    #Coleta as dimensões das imagens
    y = img.shape[0]
    x = img.shape[1]
    
    for i in range(0, x):
        for j in range(0, y):
            if img[j, i] >=128 :
                img[j, i] = 255
            else :
                img[j, i] = 0
    
    return img

#Retira as bolhas que tocam as bordas
def retira_obj_bordas(image):
    
    #Coleta as dimensões das imagens
    y = image.shape[0]
    x = image.shape[1]
    
    img = image.copy()
       
    #Cria uma mascara preta para ser usado no floodFill()
    mask = np.zeros((y+2 , x+2), dtype=np.uint8)
    
    #Retira os objetos que tocam as bordas, aplicando um floodfill() nos pixels das bordas
    for i in range(0, x):
        if img[0, i] == 255:
            cv2.floodFill(img, mask, (i, 0), 0)
        if img[y - 1, i] == 255:
            cv2.floodFill(img, mask, (i, y - 1), 0)

    for j in range(0, y):
        if img[j, 0] == 255:
            cv2.floodFill(img, mask, (0, j), 0)
        if img[j, x - 1] == 255:
            cv2.floodFill(img, mask, (x - 1, j), 0)
    
      
    return img

#Conta objetos em uma imagem
def count_obj(image):
    
    #Coleta as dimensões das imagens
    img = image.copy()
    y = img.shape[0]
    x = img.shape[1]
    
    #Cria uma mascara preta para ser usado no floodFill()
    mask = np.zeros((y+2 , x+2), dtype=np.uint8)
    
    objetos = 1
    for j in range(y):
        for i in range(x):
            if img[j,i] == 255:
                cv2.floodFill(img, mask, (i, j), objetos)
                objetos += 1    
    return img,objetos-1

#Faz o negativo da imagem em escala de cinza em uma região
def regions_gray(img, pi, pf):
    
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
            img[j,i] = 255 - img[j,i]
    
    return img

#Faz o negativo da imagem colorida em uma região
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

#Corta a imagem em 4 partes iguais e trocam as posições na diagonal
def troca_diagonal(image):
    
    y = image.shape[0]
    x = image.shape[1]
    
    img_proc = image.copy()
    
    img1 = image[0:y//2, 0:x//2]
    img2 = image[0:y//2, x//2:x]
    img3 = image[y//2:y, 0:x//2]
    img4 = image[y//2:y, x//2:x] 
    

    for i in range(0, img1.shape[1]):
        for j in range(0, img1.shape[0]):
            img_proc[j+y//2, i+x//2] = img1[j,i]
    
    for i in range(0, img2.shape[1]):
        for j in range(0, img2.shape[0]):
            img_proc[j+y//2, i] = img2[j,i]
            
    for i in range(0, img3.shape[1]):
        for j in range(0, img3.shape[0]):
            img_proc[j, i+x//2] = img3[j,i]
            
    for i in range(0, img4.shape[1]):
        for j in range(0, img4.shape[0]):
            img_proc[j, i] = img4[j,i]
    
    
    return img_proc

def file_storage(SIDE, PERIODS):
    
    ss_img = f"senoide-{SIDE}.png"
    ss_yml = f"senoide-{SIDE}.yml"

    image = np.zeros((SIDE, SIDE), dtype=np.float32)

    for i in range(SIDE):
        for j in range(SIDE):
            image[i, j] = 127 * math.sin(2 * math.pi * PERIODS * j / SIDE) + 128

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
