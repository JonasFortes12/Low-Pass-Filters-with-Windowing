import numpy as np
import math as mt
import matplotlib.pyplot as plt
from scipy import signal

# Função para plotagem de gráficos
def plot_graph(x, y, title, xlabel, ylabel, y2=None, y3=None, label=None, label2=None, label3=None, color='blue', color2='red',color3='green', mode='plot'):
    plt.figure(figsize=(8, 4))
    
    if(mode == 'plot'):
        plt.plot(x, y, label=label, color=color)
        if(y2 is not None):
            plt.plot(x, y2, label=label2, color=color2)
        if(y3 is not None):
            plt.plot(x, y3, label=label3, color=color3)
    elif(mode == 'stem'):
        plt.stem(x, y, label=label)
        if(y2 is not None):
            plt.stem(x, y2, label=label2)
        if(y3 is not None):
            plt.stem(x, y3, label=label3)
    
    # Adicionar um título ao gráfico
    plt.title(title)
    # Adicionar rótulos aos eixos
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    
    if(label is not None):
        # Adicionar uma legenda
        plt.legend()
    
    plt.show()


#__________________________ Questão 01 _____________________________________

# Define parâmetros 
cutOffFreq = 0.5 * np.pi # Frequência de corte
M = 20 #ordem
n = np.arange(0, M+1) # amostras

# Define a janela retangular
rectangularWindow = np.ones(M+1)

# Define a janela de Hanning
hanningWindow = 0.5 - 0.5 * np.cos(2 * np.pi * n / M)

# Define a janela de Blackman
blackmanWindow = 0.42 - 0.5 * np.cos(2 * np.pi * n / M) + 0.08 * np.cos(4 * np.pi * n / M)

# Função para gerar a resposta ao inpulso dos filtros FIR
def fir_filter(frequencyCutoff, window):
    h = frequencyCutoff * np.sinc(frequencyCutoff * (n - M/2)) * window
    return h

# Definição dos Filtros FIR
rectangular_filter = fir_filter(cutOffFreq, rectangularWindow)
hanning_filter = fir_filter(cutOffFreq, hanningWindow)
blackman_filter = fir_filter(cutOffFreq, blackmanWindow)

plot_graph(n, rectangular_filter, 'Respostas ao Impulso', 'Tempo', 'Amplitude', y2=hanning_filter, y3=blackman_filter, label='rectangular', label2='hanning', label3='blackman')

#__________________________ Questão 02 _____________________________________

# Gere as respostas em magnitude dos filtros
magnitude_rectangular = np.abs(np.fft.fft(rectangular_filter))
magnitude_hanning = np.abs(np.fft.fft(hanning_filter))
magnitude_blackman = np.abs(np.fft.fft(blackman_filter))

# Gere as frequências correspondentes
frequencies = np.linspace(-np.pi, np.pi, M+1)

plot_graph(frequencies, magnitude_rectangular, 'Respostas em Magnitude', 'Frequência', 'Amplitude', y2=magnitude_hanning, y3=magnitude_blackman, label='rectangular', label2='hanning', label3='blackman')


#__________________________ Questão 03 _____________________________________

plot_graph(frequencies, 20*np.log10(magnitude_rectangular), 'Respostas em Magnitude (Escala dB)', 'Frequência', 'Amplitude', y2=20*np.log10(magnitude_hanning), y3=20*np.log10(magnitude_blackman), label='rectangular', label2='hanning', label3='blackman')