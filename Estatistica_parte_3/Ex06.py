import pandas as pd
from scipy.stats import wilcoxon

sem_Alura = pd.Series([7,  8, 6, 6, 10, 4, 2, 5,  9, 2, 4, 9, 1, 10])
com_Alura = pd.Series([10, 10, 9, 9,  9, 7, 5, 8, 10, 6, 3, 7, 4,  8])

significancia = 0.1

T, p_valor = wilcoxon(sem_Alura, com_Alura)
print(f'T = {int(T)}')
print(f'O valor de p é {p_valor.round(4)}')

if p_valor < T:
    print('Rejeitar H0')
else:
    print('Aceitar H0')
