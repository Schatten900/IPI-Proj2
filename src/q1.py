import numpy as np
import cv2

from src.utils import mostrar_imagem


#======================
#   Aplicacoes
#======================


def aplicar_abertura(img : np.ndarray):
    # Aplica a abertura na imagem binarizacao
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


def aplicar_fechamento(img : np.ndarray):
    # Aplica o fechamento na imagem binarizacao
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


def aplicar_filtro_passa_baixas(img : np.ndarray) -> np.ndarray:
    # Aplicar o filtro passa baixas gaussiano
    return cv2.GaussianBlur(img, (5,5), 0)


def aplicar_filtro_mediana(img : np.ndarray) -> np.ndarray:
    # Aplicar o filtro passa baixas mediana
    return cv2.medianBlur(img, 5)


#======================
#   Utils
#======================

def mostrar_histograma():
    pass


def binarizar_imagem(img : np.ndarray, valor_limiar : int) -> np.ndarray:
    # Apos identificar o valor medio do histograma binarize a imagem
    _, binarizado = cv2.threshold(img,valor_limiar,255,cv2.THRESH_BINARY)
    return binarizado

def limiar_histograma(img : np.ndarray) -> int:
    # Identifique o histograma e o valor medio do limiar
    hist = cv2.calcHist([img],[0],None,[256],[0,256])

    limiar, _ = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print(f"Limiar escolhido pelo Otsu: {int(limiar)}")
    return int(limiar)


def elementos_conexos(img_binarizada : np.ndarray):
    # Aplique o algoritimo de elementos conexos para identificar elementos na imagem
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_binarizada, 8, cv2.CV_32S)

    # Iterar sobre os elementos conexos e salvar o de maior tamanho
    components = []

    for i in range(1,num_labels):
        area = stats[i,cv2.CC_STAT_AREA]
        components.append((area,i))

    components.sort(reverse=True)

    # O maior componente é o contorno do cerebro e o segundo maior é o tumor
    _,indice_tumor = components[1]

    mascara = np.zeros_like(img_binarizada)
    mascara[labels == indice_tumor] = 255

    return mascara


#======================
#   Funcao principal
#======================

def main_q1(img : np.ndarray):
    # Imagem sem ruido
    img_gaussiana = aplicar_filtro_passa_baixas(img)
    mostrar_imagem(img_gaussiana,"Gaussiana")

    img_mediana_com_gaussiana = aplicar_filtro_mediana(img_gaussiana)
    mostrar_imagem(img_mediana_com_gaussiana,"Gaussiana + mediana")

    # Imagem binarizada
    valor_limiar = limiar_histograma(img_mediana_com_gaussiana)
    img_binarizada = binarizar_imagem(img_mediana_com_gaussiana,valor_limiar)
    mostrar_imagem(img_binarizada,"Brain binarizado")

    # Aplicar operacoes morfologicas
    img_aberta = aplicar_abertura(img_binarizada)   # Remove contorno
    mostrar_imagem(img_aberta,"Abertura")

    img_fechada = aplicar_fechamento(img_aberta)    # Deixa o tumor mais nitido
    mostrar_imagem(img_fechada,"Fechamento")

    # Visualizacao do tumor
    tumor = elementos_conexos(img_fechada)          # retorna a mascara binarizada do tumor
    mostrar_imagem(tumor,"Tumor em destaque")

    