import numpy as np
from scipy import stats

def task1():
    """Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых 
    футболистов, хоккеистов и штангистов.
    Даны значения роста в трех группах случайно выбранных спортсменов:
    Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
    Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
    Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170."""
    
    # Формулирование гипотез:
    # # H0: μ(x1) = μ(x2) = μ(x3) - средний рост спортсмена не зависит от вида спорта, которым он занимается (из представленных трех)
    # # H1: μ(x) != μ(x2) != μ(x3) - средний рост спортсмена зависит от выбранного им спорта.

    football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
    hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
    weightlifting = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

    print(f'{stats.f_oneway(football, hockey, weightlifting)}.')
    print(f'Вывод: Т.к pvalue < a(0,05) => статистически значимые различия есть.')
    print ('Принимаем альтернативную гипотезу - средний рост спортсмена зависит от выбранного им вида спорта')

def task2():
    """Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых 
    футболистов, хоккеистов и штангистов.
    Даны значения роста в трех группах случайно выбранных спортсменов:
    Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
    Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
    Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170."""
    
    football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
    hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
    weightlifting = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

    n1 = football.shape[0]
    n2 = hockey.shape[0]
    n3 = weightlifting.shape[0]

    f_mean = football.mean()
    h_mean = hockey.mean()
    w_mean = weightlifting.mean()
    
    y = np.concatenate([football, hockey, weightlifting])
    y_mean = y.mean()
    
    S2_F = n1 * (f_mean - y_mean) ** 2 + n2 * (h_mean - y_mean) ** 2 + n3 * (w_mean - y_mean) ** 2
    S2_res = ((football - f_mean) ** 2).sum() + ((hockey - h_mean) ** 2).sum() + ((weightlifting - w_mean) ** 2).sum()

    print(f'Проверим выполнение равенства {S2_F + S2_res} = {((y - y_mean) ** 2).sum()}')

    p = 3
    n = n1 + n2 + n3
    
    df1 = p - 1
    df2 = n - p
    
    # Оценки дисперсий
    sigma2_F = S2_F / df1 #факторная
    sigma2_res = S2_res / df2 #остаточная

    # значение статистики Т
    T = sigma2_F / sigma2_res

    # значение статистики Fcrit
    F_crit = stats.f.ppf(1 - 0.05, df1, df2)
  
    print(f'Вывод: Т.к T={T: .3f} > Fcrit={F_crit: .3f}  => отличие среднего роста спортсменов является статистически значимым.')


task2()