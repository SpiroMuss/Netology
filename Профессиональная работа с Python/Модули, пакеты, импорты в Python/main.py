import application.salary as salary
import application.db.people as people
import datetime

def show_date():
    print(datetime.date.today())

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    show_date()