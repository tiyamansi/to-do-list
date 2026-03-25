task = []
while True:
    print('=== To Do-List ===')
    print('Menu \n1.Add Task \n2.View Tasks \n3.Delete Task' \
            '\n4.Exit')
    try:
        user = int(input('Enter the task to be done(1,2,3,4)'))
        if user == 1:
            print('Type back when you are done with adding task')
            while True:
                a = input('Enter task:').strip().lower()
                if a == 'back':
                    break
                elif a == '':
                    print('Empty task not allowed')
                else:
                    task.append(a)
        elif user == 2:
            if not task:
                print('No tasks to be displayed')
            else:
                for i, t in enumerate(task,1):
                    print(f'{i}:{t}')
        elif user == 3:
            if not task:
                print('No task to be deleted')
                continue
            try:
                delete = int(input('Enter the task to be deleted'))
                task.pop(delete-1)
            except (IndexError,ValueError):
                print('Wrong Task Number chosen')
        elif user == 4:
            break
        else:
            print('Enter Valid Input')
    except ValueError:
        print('Invalid Input')
        