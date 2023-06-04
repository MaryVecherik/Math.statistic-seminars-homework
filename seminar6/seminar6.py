import scipy.stats as stats
import numpy as np

def task1():
    """На препарате А положительный результат лечения наблюдается у 17 из 32 пациентов, 
    а на препарате В у 9 из 22. Построить 95% доверительный интервал для разности долей.
    Обнаружены ли статистически значимые различия?."""
    
    delta = 17/32 - 9/22
    Zt = stats.norm.ppf(0.975)
    p = (17+9)/(32+22)
    
    #стандартная ощибка 
    SE = np.sqrt(p*(1-p)*(1/32 + 1/22))

    left = delta - Zt*SE
    right = delta + Zt*SE
    
    print(f'доверительный интервал: [{left:.3f}; {right:.3f}].')

def task2():
    """Решить задачу 1 через тестирование гипотезы.
    На препарате А положительный результат лечения наблюдается у 17 из 32 пациентов, а
    на препарате В у 9 из 22. Являются ли различия статистически значимые между долями
    пациентов с положительным эффектом в этих двух группах.
    Уровень статистической значимости принять за 0.05"""
    
    Zt = stats.norm.ppf(0.975)
    print(f'Табличный критерий = {Zt:.2f}')

    p1 = 17/32
    p2 = 9/22
    p = (17+9)/(32+22)

    #стандартная ощибка 
    SE = np.sqrt(p*(1-p)*(1/32 + 1/22))

    Z = (abs(p1 - p2) - 1/2*(1/32 + 1/22)) / SE
    print(Z)

    if Zt > Z:
        print('Принимаем нулевую гипотезу')
    else:
         print('Принимаем альтернативную гипотезу')

def task3():
    """С помощью 90% доверительного интервала оценить средний вес нормально
    распределенной популяции, если дисперсия генеральной совокупности 3.6, а среднее
    арифметичекое по выборке объемом 100 получилось равным 71.2."""


task2()