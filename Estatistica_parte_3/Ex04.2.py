import pandas as pd
from statsmodels.stats.weightstats import DescrStatsW

shampoo_Novo = pd.Series([3.4, 4.9, 2.8, 5.5, 3.7, 2.5, 4.3, 4.6, 3.7, 3.4])
shampoo_Antigo = pd.Series([0.3, 1.2, 1.2, 1.7, 1.1, 0.6, 1.2, 1.5, 0.5, 0.7])

significancia_shampoo = 0.05

test_novo = DescrStatsW(shampoo_Novo)
test_antigo = DescrStatsW(shampoo_Antigo)
test = test_novo.get_compare(test_antigo)

t, p_valor, df = test.ttest_ind(alternative='larger', value=2)

print(f't = {t.round(4)}')
print(f'p-valor = {p_valor.round(4)}')
print(f'graus de liberdade = {int(df)}')

if p_valor <= significancia_shampoo:
    print('Rejeitar H0')
else:
    print('Aceitar H0')
