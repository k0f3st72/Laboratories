class Employee:
    def __init__(self, name: str, id: int):
        self.name = name
        self._id = id

    def get_info(self) -> str:
        return f'Сотрудник: {self.name}, ID: {self._id}'

    def __str__ (self):
        return self.get_info()

class Manager(Employee):
    def __init__(self, name: str, id: int, department: str):
        super().__init__(name, id)
        self.department = department
        self.team = []

    def manager_project(self, project_name: str) -> str:
        return f"Менеджер {self.name} управляет проектом {project_name} в отделе {self.department}"

    def get_info(self):
        return (f'{super().get_info()}, Должность: менеджер, '
                f'Отдел: {self.department}')

    def add_employee(self, employee: Employee):
        self.team.append(employee)
        return f"Сотрудник {employee.name} добавлен в команду"

    def get_team_info(self) -> list:
        return [emp.get_info() for emp in self.team]

    def get_team_detail(self) -> str:
        if not self.team:
            return 'В команде нет сотрудников'
        team_info = '\n'.join([f' - {emp.get_info()}' for emp in self.team])
        return f'Команда менеджера {self.name}: \n{team_info}'

class Technician(Employee):
    def __init__(self, name: str, id: int, specialization: str):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self) -> str:
        return f"Техник {self.name} выполняет техническое обслуживание в области {self.specialization}"

    def get_info(self) -> str:
        return (f"{super().get_info()}, Должность: Техник, "
                f" Специализация: {self.specialization}")

class TechManager(Manager, Technician):
    def __init__(self, name: str, id: int, department: str, specialization: str):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)

    def get_info(self) -> str:
        base_info = Manager.get_info(self)
        return f'{base_info}, Специализация {self.specialization}'

    def __str__(self):
        return f"TechManager: {self.get_info()}"

class EmployeeSystem:
    def __init__(self):
        self.employees = []
        self.managers = []
        self.technicians = []
        self.techmanagers = []

    def input_employee(self):
        print('Добавление обычного сотрудника')
        name = input('Введите имя сотрудника: ')
        while True:
            try:
                emp_id = int(input('Введите ID сотрудника: '))
                break
            except (ValueError):
                print("Ошибка: ID должно быть числом. Попробуйте ещё раз")
                continue

        employee = Employee(name, emp_id)
        self.employees.append(employee)
        print(f'Сотрудник {name} успешно добавлен')
        return employee

    def input_manager(self):
        print("Добавление менеджера")
        name = input('Введите имя менеджера: ')
        while True:
            try:
                emp_id = int(input('Введите ID сотрудника: '))
                break
            except (ValueError):
                print("Ошибка: ID должно быть числом. Попробуйте ещё раз")
                continue

        department = input('Введите отдел менеджера: ')
        manager = Manager(name, emp_id, department)
        self.employees.append(manager)
        self.managers.append(manager)
        print(f'Менеджер {name} успешно добавлен')
        return manager

    def input_technician(self):
        print('Добавление техника')
        name = input('Введите имя техника: ')
        while True:
            try:
                emp_id = int(input('Введите ID техника: '))
                break
            except (ValueError):
                print("Ошибка: ID должно быть числом. Попробуйте ещё раз")
                continue

        specialization = input("Введдите специализацию техника: ")
        technician = Technician(name, emp_id, specialization)
        self.employees.append(technician)
        self.technicians.append(technician)
        print(f'Техник {name} успешно добавлен')
        return technician

    def input_techmanager(self):
        print("Добавление технического менеджера")
        name = input('Введите имя технического менеджера: ')
        while True:
            try:
                emp_id = int(input("Введите ID технического менеджера: "))
                break
            except (ValueError):
                print("Ошибка: ID должно быть числом. Попробуйте ещё раз")
                continue

        department = input("Введите отдел: ")
        specialization = input("Введите специализацию: ")
        techmanager = TechManager(name, emp_id, department, specialization)
        self.employees.append(techmanager)
        self.techmanagers.append(techmanager)
        print(f"Технический менеджер {name} успешно добавлен")
        return techmanager

    def add_employee_to_manager(self):
        print("Добавление сотрудника в команду менеджера")
        if not self.managers:
            print("Нет свободных менеджеров")
            return

        if not self.employees:
            print("Нет свободных сотрудников")
            return

        print("Выбор менеджера")
        for i, manager in enumerate(self.managers, 1):
            print(f'{i}. {manager.name} (ID: {manager._id})')

        try:
            mgr_choice = int(input('Выбери номер менеджера: ')) - 1
            selected_manager = self.managers[mgr_choice]
        except (ValueError, IndexError):
            print("Неверный выбор")
            return

        print("Выбор сотрудника для добавления в команду")
        available_employees = [emp for emp in self.employees if emp != selected_manager]
        for i, emp in enumerate(available_employees, 1):
            print(f'{i}. {emp.get_info()}')

        try:
            emp_choice = int(input("Введите номер сотрудника: ")) - 1
            selected_employee = available_employees[emp_choice]
        except (ValueError, IndexError):
            print('Неверный выбор')
            return

        result = selected_manager.add_employee(selected_employee)
        print(f'{result}')

    def show_all_employees(self):
        """ПОКАЗАТЬ ВСЕХ СОТРУДНИКОВ"""
        print("Все сотрудники")
        if not self.employees:
            print("нет сотрудников")
            return

        for i, employee in enumerate(self.employees, 1):
            print(f'{i}. {employee.get_info()}')

    def show_team_info(self):
        """"ПОКАЗАТЬ ИНФОРМАЦИЮ О КОМАНДАХ МЕНЕДЖЕРОВ"""
        if not self.managers:
            print("Нету менеджеров")
            return

        print("Информация о командах")
        for manager in self.managers:
            print(manager.get_team_info())
            print('-' * 30)

    def perform_actions(self):
        if not self.employees:
            print("Нет сотрудников")
            return

        print("Выбор сотрудника для действия")
        for i, employee in enumerate(self.employees, 1):
            print(f'{i}. {employee.get_info()}')

        try:
            choice = int(input("Выбери номер сотрудника: ")) - 1
            selected_employee = self.employees[choice]
        except (ValueError, IndexError):
            print("Неверный выбор")
            return

        print(f"Действия для {selected_employee.name}")

        #Полиморфизм
        if isinstance(selected_employee, Manager):
            project = input("Введите название проекта: ")
            print(f'{selected_employee.manager_project(project)}')

        if isinstance(selected_employee, Technician):
            print(f'{selected_employee.perform_maintenance()}')

    def polymorphism(self):
        if not self.employees:
            print("Нет сотрудников")
            return

        for employee in self.employees:
            print(f"{employee.get_info()}")

    def show_menu(self):
        """МЕНЮ"""
        while True:
            print("-" * 30)
            print("СИСТЕМА УПРАВЛЕНИЯ СОТРУДНИКАМИ")
            print("-" * 50)
            print("1. Добавить обычного сотрудника")
            print("2. Добавить менеджера")
            print("3. Добавить техника")
            print("4. Добавить TechManager")
            print("5. Показать всех сотрудников")
            print("6. Добавить сотрудника в команду менеджера")
            print("7. Показать информацию о командах")
            print("8. Выполнить специальные действия")
            print("9. Демонстрация полиморфизма")
            print("0. Выход")
            print("-" * 30)
            try:
                choice = int(input('Выберите действие: '))
            except (ValueError):
                print("Ошибка! Введите число от 0 до 9.")
                continue

            if choice == 1:
                self.input_employee()
            elif choice == 2:
                self.input_manager()
            elif choice == 3:
                self.input_technician()
            elif choice == 4:
                self.input_techmanager()
            elif choice == 5:
                self.show_all_employees()
            elif choice == 6:
                self.add_employee_to_manager()
            elif choice == 7:
                self.show_team_info()
            elif choice == 8:
                self.perform_actions()
            elif choice == 9:
                self.polymorphism()
            elif choice == 0:
                print("До свидания!")
                break
            else:
                print(" Неверный выбор! Попробуйте снова.")

def run_program():
    system = EmployeeSystem()
    system.show_menu()

if __name__ == "__main__":
    run_program()