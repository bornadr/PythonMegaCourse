todos = []

while True:

    user_actions = input("Type add, show, or exit: ")
    user_actions = user_actions.split()

    match user_actions:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

print("Be")
