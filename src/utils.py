import cv2
import numpy as np



def mostrar_imagem(img : np.ndarray, title : str ) -> None:
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def abrir_imagem(path : str, grayscale : bool) -> np.ndarray:
    if grayscale:
        img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    else:
        img = cv2.imread(path,cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError(f"Erro ao tentar ler  imagem: {path}")

    return img
