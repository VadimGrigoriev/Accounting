from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date


if __name__ == '__main__':
    current_date = date.today().strftime('[%d-%m-%Y]')
    print(current_date, calculate_salary())
    print(current_date, get_employees())
