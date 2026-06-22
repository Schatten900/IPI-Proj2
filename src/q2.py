import numpy as np
import cv2

from src.utils import mostrar_imagem


#======================
#   Utils
#======================


def converter_para_float32(img : np.ndarray):
    # Algoritmo k-means precisa ser em float 
    pixel_values = img.reshape((-1,3))
    return np.float32(pixel_values)

def calcular_cluster(pixels_values, criteria) -> int :
    # Identifica o melhor valor de cluster
    custos = []
    ks = []
    quantidade_k = 20
    for k in range(2,quantidade_k+1):
        # Compactacao dos grupos, qual cluster pertence o pixel, cores medias
        retval, labels, centers = cv2.kmeans(pixels_values, k, None, criteria, quantidade_k, cv2.KMEANS_PP_CENTERS)
        ks.append(k)
        custos.append(retval)
    
    #analisar os custos
    print(f"custos: {custos}")
    
    for k, custo in zip(ks, custos):
        print(f"K={k} -> custo={custo:.2f}")

    # escolher melhor k
    LIMIAR = 0.05
    for i in range(1,len(custos)):
        melhoria = (custos[i-1] - custos[i]) / custos[i-1]
        if melhoria < LIMIAR:
            print(f"melhor escolha: {ks[i-1]}")
            return ks[i-1]

    print(f"Nao encontrou um k otimo: {ks[-1]}")
    return ks[-1]

#======================
#   Aplicacoes
#======================


def k_means(pixels_values,k,criteria):
    retval, labels, centers = cv2.kmeans(pixels_values, k, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
    return labels, centers

def segmentar(img, centers, labels):
    # Segmente os vegetais da imagem
    centers = np.uint8(centers)

    segmentada = centers[labels.flatten()]      #Para cada pixel descobre seu cluster, pega a cor media do cluster e substitua o pixel pela cor
    segmentada = segmentada.reshape(img.shape)
    return segmentada


#======================
#   Funcao principal
#======================

def main_q2(img : np.ndarray):
    mostrar_imagem(img,"imagem original")
    pixels_values = converter_para_float32(img)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,0.2) 

    melhor_k = calcular_cluster(pixels_values,criteria)
    labels, centers = k_means(pixels_values,melhor_k,criteria)

    img_segmentada = segmentar(img,centers,labels)

    mostrar_imagem(img_segmentada,"imagem segmentada")