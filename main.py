from src.utils import abrir_imagem
import cv2
import src.q1 as q1
import src.q2 as q2

def run_q1() -> None:
    print("Rodando [Q1]")
    img = abrir_imagem("img/brain.jpg",grayscale=True)
    q1.main_q1(img)


def run_q2() -> None:
    print("Rodando [Q2]")
    img = abrir_imagem("img/onion.jpg",grayscale=True)
    q2.main_q2(img)


if __name__ == "__main__":

    saiu = False
    print("Ola, seja bem vindo!")
    while not saiu:
        print("Selecione qual exercicio deseja executar: \n")
        print("1- Trabalho 1")
        print("2- Trabalho 2")
        print("3- Sair\n")

        escolha = input("Digite sua escolha: ")
        if escolha == '1':
            run_q1()
        elif escolha == '2':
            run_q2()
        elif escolha == '3':
            print("Ate logo!")
            saiu = True
        else:
            print("Escolha uma opcao valida")