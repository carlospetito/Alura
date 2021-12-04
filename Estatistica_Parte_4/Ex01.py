import numpy as np

sigma_XY = 2178803.59
sigma_X2 = 7328865.85
sigma_Y2 = 667839.78

sigma_X = np.sqrt(sigma_X2)
sigma_Y = np.sqrt(sigma_Y2)

r_XY = sigma_XY / (sigma_X * sigma_Y)
print(f'A Correlação enre X e Y é {r_XY.round(4)}')

