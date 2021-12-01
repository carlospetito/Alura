import pandas as pd
from scipy.stats import mannwhitneyu

sem_Exercicios = pd.Series([7, 6, 7, 8, 6, 8, 6, 9, 5])
com_Exercicios = pd.Series([8, 7, 6, 6, 8, 6, 10, 6, 7, 8])

significancia = 0.1

u, p_valor = mannwhitneyu(com_Exercicios, sem_Exercicios, alternative='greater')
print(f'u = {int(u)}')
print(f'O valor de p é {p_valor.round(4)}')

if p_valor <= significancia:
    print('Rejeitar H0')
else:
    print('Aceitar H0')
