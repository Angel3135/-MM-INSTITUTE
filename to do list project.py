def task_management():
    tasks = []
    while True:
        print("1. add task")
        print("2. update task")
        print("3. delete task")
        print("4. view task")
        print("5. exit")
        choice= int(input("enter your choice:"))

        if choice==1:
            task_name= input("enter task name:").strip()
            tasks.append(task_name)
            print(f"task'{task_name}' added successfully.")

        elif choice==2:
            updated_val= input("enter task name to update:").strip()
            if updated_val in tasks:
                new_task_name= input("enter new task name:").strip()
                tasks[tasks.index(updated_val)] = new_task_name
                print(f"task '{updated_val}' updated to '{new_task_name}'.")
            else:
                print("task not found.")

        elif choice==3:
            del_val= input("enter task name to delete:").strip()
            if del_val in tasks:
                tasks.remove(del_val)
                print(f" task '{del_val}' deleted successfully.")
            else:
                print("task not found.")

        elif choice==4:
            print("tasks:")
            for task in tasks:
                print(task)

        elif choice==5:
            print("exiting task management system.")
            break
        else:
            print("invalid choice")

task_management()                                                
            