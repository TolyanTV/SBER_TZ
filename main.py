import json
from pathlib import Path


def load_tasks():
    file_path = Path('tasks.json')
    
    if file_path.exists() and file_path.is_file():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def main():
    while True:
        print("\nСписок дел:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Отметить задачу выполненной")
        print("4. Получить список задач")
        print("5. Выход")
        
        choice = input("Выберите пункт меню (1-5): ")
        
        try:
            if choice == '1':
                task_name = input("Введите название задачи: ").strip()
                
                if not task_name:
                    raise ValueError("Поле для задачи не должно быть пустым!")
                    
                tasks = load_tasks()
                tasks.append({"name": task_name, "done": False})
                save_tasks(tasks)
                print(f'Задача "{task_name}" успешно добавлена!')
            
            elif choice == '2':
                tasks = load_tasks()
                
                if len(tasks) > 0:
                    index = int(input("Введите номер задачи для удаления: "))
                    
                    if 1 <= index <= len(tasks):
                        removed_task = tasks.pop(index-1)
                        save_tasks(tasks)
                        print(f'Задача "{removed_task["name"]}" удалена!')
                    else:
                        print("Неверный индекс задачи!")
                else:
                    print("Список задач пуст!")
            
            elif choice == '3':
                tasks = load_tasks()
                
                if len(tasks) > 0:
                    index = int(input("Введите номер задачи для пометки как выполненную: "))
                    
                    if 1 <= index <= len(tasks):
                        tasks[index-1]["done"] = True
                        save_tasks(tasks)
                        print(f'Задача №{index} отмечена как выполненная!')
                    else:
                        print("Неверный индекс задачи!")
                else:
                    print("Список задач пуст!")
            
            elif choice == '4':
                tasks = load_tasks()
                
                if len(tasks) > 0:
                    for i, task in enumerate(tasks):
                        status = "Выполнено" if task["done"] else "Не выполнено"
                        print(f"{i+1}. {task['name']} ({status})")
                else:
                    print("Нет задач в списке!")
            
            elif choice == '5':
                break
            
            else:
                print("Некорректный выбор пункта меню!")
        
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()