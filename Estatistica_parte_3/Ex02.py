import numpy as np
from scipy.stats import t as t_student

media_esgoto = 150
media_amostra_esgoto = 230
desvio_amostra_esgoto = 90
significancia_esgoto = 0.05
confianca_esgoto = 1 - significancia_esgoto
n_esgoto = 20
graus_de_liberdade_esgoto = n_esgoto - 1

t_esgoto = (media_amostra_esgoto - media_esgoto) / (desvio_amostra_esgoto / np.sqrt(n_esgoto))
print(f't = {t_esgoto}')

t_alpha_esgoto = t_student.ppf(confianca_esgoto, graus_de_liberdade_esgoto)
print(f't alpha = {t_alpha_esgoto}')

H0 = t_esgoto >= t_alpha_esgoto

if H0:
    print('Rejeitar H0')
else:
    print('Aceitar H0')
