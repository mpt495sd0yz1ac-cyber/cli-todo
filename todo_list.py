import json
import os

FILE_NAME = "todo.json"

def load_todos():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todos(todos):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def add_todo(todos):
    title = input("TODOを入力: ")
    todos.append({"title": title, "done": False})

def show_todos(todos):
    if not todos:
        print("TODOはありません")
        return
    for i, todo in enumerate(todos):
        status = "✓" if todo["done"] else " "
        print(f"{i+1}. [{status}] {todo['title']}")

def toggle_todo(todos):
    show_todos(todos)
    num = int(input("番号を選択: ")) - 1
    if 0 <= num < len(todos):
        todos[num]["done"] = not todos[num]["done"]

def main():
    todos = load_todos()

    while True:
        print("\\n1:Add 2:Show 3:Toggle 4:Exit")
        choice = input("選択: ")

        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            show_todos(todos)
        elif choice == "3":
            toggle_todo(todos)
        elif choice == "4":
            save_todos(todos)
            print("終了します")
            break
        else:
            print("無効な入力です")

if __name__ == "__main__":
    main()
