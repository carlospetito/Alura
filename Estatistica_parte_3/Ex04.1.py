import pandas as pd
import numpy as np
from scipy.stats import t as t_student

shampoo_Novo = pd.Series([3.4, 4.9, 2.8, 5.5, 3.7, 2.5, 4.3, 4.6, 3.7, 3.4])
shampoo_Antigo = pd.Series([0.3, 1.2, 1.2, 1.7, 1.1, 0.6, 1.2, 1.5, 0.5, 0.7])

significancia = 0.05
confianca = 1 - significancia

media_shampoo_novo = shampoo_Novo.mean()
desvio_shampoo_novo = shampoo_Novo.std()

media_shampoo_antigo = shampoo_Antigo.mean()
desvio_shampoo_antigo = shampoo_Antigo.std()

n_novo = len(shampoo_Novo)
n_antigo = len(shampoo_Antigo)

graus_de_liberdade_shampoo = n_novo + n_antigo - 2
D_0 = 2

t_alpha_shampoo = t_student.ppf(confianca, graus_de_liberdade_shampoo)
print(f't alpha = {t_alpha_shampoo.round(4)}')

numerador = (media_shampoo_novo - media_shampoo_antigo) - D_0
denominador = np.sqrt((desvio_shampoo_novo ** 2 / n_novo) + (desvio_shampoo_antigo ** 2 / n_antigo))
t_shampoo = numerador / denominador

print(f't = {t_shampoo.round(4)}')

if t_shampoo >= t_alpha_shampoo:
    print('Rejeitar H0')
else:
    print('Aceitar H0')
