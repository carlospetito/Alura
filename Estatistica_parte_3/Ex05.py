from scipy.stats import chi
import numpy as np

chi_2 = 7.45
raiz_chi_2 = np.sqrt(chi_2)
p_valor = chi.sf(raiz_chi_2, df=5)
print(f'O valor de p é {p_valor.round(4)}')
