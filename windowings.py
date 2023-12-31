import numpy as np
import math as mt
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, windows


# Função para plotagem de gráficos
def plot_graph(
    x,
    y,
    title,
    xlabel,
    ylabel,
    y2=None,
    y3=None,
    label=None,
    label2=None,
    label3=None,
    color="blue",
    color2="red",
    color3="green",
    mode="plot",
):
    plt.figure(figsize=(8, 4))

    if mode == "plot":
        plt.plot(x, y, label=label, color=color)
        if y2 is not None:
            plt.plot(x, y2, label=label2, color=color2)
        if y3 is not None:
            plt.plot(x, y3, label=label3, color=color3)
    elif mode == "stem":
        plt.stem(x, y, label=label)
        if y2 is not None:
            plt.stem(x, y2, label=label2)
        if y3 is not None:
            plt.stem(x, y3, label=label3)

    # Adicionar um título ao gráfico
    plt.title(title)
    # Adicionar rótulos aos eixos
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    if label is not None:
        # Adicionar uma legenda
        plt.legend()

    plt.show()


# __________________________ Questão 01 _____________________________________

# Define parâmetros
fs = 1000  # Frequência de amostragem em Hz
cutOffFreq = 0.5 * np.pi  # Frequência de corte
M = 20  # ordem
n = np.arange(0, M)  # amostras

# Calcula a largura de banda de transição
Bt = cutOffFreq / fs

# Projeta o filtro com janela de retangular
h_rectangular = firwin(M, cutoff=cutOffFreq, window='boxcar', fs=fs)

# Projeta o filtro com janela de hamming
h_hamming = firwin(M, cutoff=cutOffFreq, window='hamming', fs=fs)

# Projeta o filtro com janela de blackman
h_blackman = firwin(M, cutoff=cutOffFreq, window='blackman', fs=fs)


plot_graph(
    n,
    h_rectangular,
    "Respostas ao Impulso",
    "Tempo",
    "Amplitude",
    y2=h_hamming,
    y3=h_blackman,
    label="rectangular",
    label2="hanning",
    label3="blackman",
)

# __________________________ Questão 02 _____________________________________

# Gere as respostas em magnitude dos filtros
magnitude_rectangular = np.abs(np.fft.fftshift(np.fft.fft(h_rectangular)))
magnitude_hanning = np.abs(np.fft.fftshift(np.fft.fft(h_hamming)))
magnitude_blackman = np.abs(np.fft.fftshift(np.fft.fft(h_blackman)))

# Gere as frequências correspondentes
frequencies = np.linspace(-np.pi, np.pi, M)

plot_graph(
    frequencies,
    magnitude_rectangular,
    "Respostas em Magnitude",
    "Frequência",
    "Amplitude",
    y2=magnitude_hanning,
    y3=magnitude_blackman,
    label="rectangular",
    label2="hanning",
    label3="blackman",
)


# __________________________ Questão 03 _____________________________________

plot_graph(
    frequencies,
    20 * np.log10(magnitude_rectangular),
    "Respostas em Magnitude (Escala dB)",
    "Frequência",
    "Amplitude",
    y2=20 * np.log10(magnitude_hanning),
    y3=20 * np.log10(magnitude_blackman),
    label="rectangular",
    label2="hanning",
    label3="blackman",
)


# __________________________ Questão 04 _____________________________________
'''
    O filtro passa baixa FIR com janela retangular é fácil de implementar devido 
    à sua forma simples
    
    A desvantagem é que possui lobos laterais significativos, o que pode causar 
    vazamentos espectral, introduzindo componentes fora da banda de interesse e
    também apresenta um pequeno ripple (flutuações ou variações indesejadas)
    na banda de passagem. Tem uma resposta ao impulso mais longa, 
    resultando em uma largura de transição maior.

    Já o filtro com a janela de Hanning tem uma banda de transição menor que o retangular.
    Apresenta uma melhor supressão dos lobos laterais em comparação com a janela retangular e
    tem menos ripple na banda de passagem. Mas ainda apresenta uma banda de transição um pouco
    maior que a janela de blackman
    
    O filtro blackman tem uma resposta ao impulso mais curta, 
    resultando em uma largura de transição menor, o que aumenta
    a precisão do corte do sinal.

'''
