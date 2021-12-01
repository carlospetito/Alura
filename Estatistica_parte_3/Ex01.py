import numpy as np
from scipy.stats import norm

media_farinha = 500
significancia_farinha = 0.05
confianca_farihna = 1 - significancia_farinha
n_farinha = 30
media_amostra_farinha = 485
desvio_farinha = 20

z_alpha_farinha = norm.ppf(0.5 + (confianca_farihna / 2))
print(f'z alpha = {z_alpha_farinha}')

z_farinha = (media_amostra_farinha - media_farinha) / (desvio_farinha / np.sqrt(n_farinha))
print(f'z = {z_farinha}')

H0_1 = (z_farinha <= -z_alpha_farinha)

H0_2 = (z_farinha >= z_alpha_farinha)

if H0_1 is True or H0_2 is True:
    print('Rejeitar H0')
else:
    print('Aceitar H0')

p_valor_farinha = 2 * (norm.sf(abs(z_farinha)))
print(f'O valor de p é {p_valor_farinha:.5f}')
