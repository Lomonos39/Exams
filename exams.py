
import sys

if __name__ == '__main__':
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия и инициалы? ")
            group = input("Номер группы? ")
            marks = list(map(int, input('Введите оценки').split()))

            student = {
                'name': name,
                'group': group,
                'marks': marks,
            }

            students.append(student)

            if len(students) > 1:
                students.sort(key=lambda item: item.get('group', 0))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "No",
                    "Ф.И.О.",
                    "Группа",
                    "Успеваемость"
                )
            )
            print(line)

            for idx, student in enumerate(students, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                        student.get('marks[0]', '')
                    )
                )

            print(line)

        elif command.startswith('select'):

            count = 0
            for student in students:
                if sum(student.get('marks', '')) / len(marks) >= 4:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, student.get('name', ''))
                        )

            if count == 0:
                print("Студентов с такими оценками нет")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select <успеваемость> - запросить студентов с успеваемостью выше четверки;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)