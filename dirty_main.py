from application.salary import *
from application.db.people import *
from datetime import date


if __name__ == '__main__':
    current_date = date.today().strftime('[%d-%m-%Y]')
    print(current_date, calculate_salary())
    print(current_date, get_employees())
