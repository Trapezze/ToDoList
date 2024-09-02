#To-Do-list 
tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Задачи не найдено.")

def show_tasks():
    if tasks:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("Список задач пуст.")

# Пример использования функций
add_task("Сходить в магазин")
add_task("Погулять с собакой")
show_tasks()
remove_task("Погулять с собакой")
show_tasks()
