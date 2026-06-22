# Processamento de Imagens com OpenCV e Python

Este repositório contém dois trabalhos práticos de Processamento Digital de Imagens desenvolvidos em ambiente Linux. O projeto utiliza as bibliotecas **OpenCV** e **NumPy** para realizar filtragem morfológica, binarização e segmentação baseada em agrupamento (*clustering*).

---

## 📌 Descrição dos Trabalhos

### 🧠 Trabalho 1: Identificação de Elemento Conexo (Cérebro/Tumor)
* **Objetivo:** Isolar e identificar mecanicamente o maior elemento conexo (neste caso, uma região anómala/tumor) na imagem de um cérebro (`brain.jpg`).
* **Fluxo de Processamento:**
  1. Remoção de ruído utilizando filtros passa-baixas sequenciais (**Gaussiano** e **Mediana**).
  2. Determinação automática do limiar de binarização através do método de **Otsu** baseado no histograma.
  3. Aplicação de operações morfológicas de **Abertura** e **Fechamento**.
  4. Análise de componentes conectados (`connectedComponentsWithStats`) para filtrar e destacar o elemento com a maior área útil da imagem.

### 🧅 Trabalho 2: Segmentação de Vegetais (K-Means)
* **Objetivo:** Segmentar e isolar os vegetais presentes numa imagem utilizando o algoritmo de agrupamento **K-Means**.
* **Fluxo de Processamento:**
  1. Conversão da matriz da imagem para o formato `float32` (exigência do OpenCV para o K-Means).
  2. Execução de um algoritmo de procura iterativo que testa quantidade de clusters ($K$).
  3. Escolha automática do **melhor valor de $K$** com base num limiar de melhoria de custo.
  4. Segmentação das cores médias e aplicação da máscara para gerar o resultado final.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **OpenCV (`cv2`)**
* **NumPy**

---

## 🚀 Como Configurar e Executar (Linux)

O projeto possui uma interface de utilizador simples via terminal que permite alternar e testar ambos os trabalhos através de um menu interativo.

### 1. Clonar o Repositório
```bash
git clone https://github.com/Schatten900/IPI-Proj2
```
### 2. Configurar o ambiente (Venv)
Cria e ativa o ambiente virtual isolado para evitar conflitos de dependências:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
Instalar os pacotes necessários por meio do requirements.txt
```bash
pip install -r requirements.txt
```

### 4. Executando a aplicação
```bash
python main.py
```