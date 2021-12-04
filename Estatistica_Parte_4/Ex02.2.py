import pandas as pd
import statsmodels.api as sm

dataset = {
    'Y': [670, 220, 1202, 188, 1869, 248, 477, 1294, 816, 2671, 1403, 1586, 3468, 973, 701, 5310, 10950, 2008, 9574, 28863, 6466, 4274, 6432, 1326, 1423, 3211, 2140],
    'X': [1.59, 0.56, 2.68, 0.47, 5.2, 0.58, 1.32, 3.88, 2.11, 5.53, 2.6, 2.94, 6.62, 1.91, 1.48, 10.64, 22.39, 4.2, 21.9, 59.66, 14.22, 9.57, 14.67, 3.28, 3.49, 6.94, 6.25]
}

dataset = pd.DataFrame(dataset)
Y = dataset.Y
X = sm.add_constant(dataset.X)
resultado_regressao = sm.OLS(Y, X, missing='drop').fit()
renda_estado = 2345678
renda_estado_conv = renda_estado / 1000000

print(f'No total {int(resultado_regressao.predict([1, renda_estado_conv])[0].round())} domicilios possuem computador')