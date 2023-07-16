from tqdm import tqdm
from time import sleep


def calculate_salary():
    for _ in tqdm(range(10), ncols=81, desc='Расчет заработной платы'):
        sleep(0.1)
    return 'Ваша заработная плата рассчитана.'
