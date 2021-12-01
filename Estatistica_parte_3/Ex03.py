import numpy as np
from scipy.stats import norm

media_pizza = 350
n_pizza = 35
media_amostra_pizza = 330
desvio_amostra_pizza = 80
significancia = 0.05
confianca = 1 - significancia

z_pizza = (media_amostra_pizza - media_pizza) / (desvio_amostra_pizza / np.sqrt(n_pizza))
print(f'z = {z_pizza}')

z_alpha_pizza = norm.ppf(confianca)
print(f'z alpha = {z_alpha_pizza}')

H0 = z_pizza <= -z_alpha_pizza

if H0:
    print('Rejeitar H0')
else:
    print('Aceitar H0')
