def task ():
    tasks = []
    print("Welcome to the Todo App!")
    
    total_tasks = int(input("How many tasks would you like to add? "))
    for i in range(1, total_tasks + 1):
        task = input(f"Enter task {i}: ")
        tasks.append(task)
        
    print(f"Today's tasks are \n{tasks}")  
    
    while True:
        operation = int(input("Choose an operation - 1: Add Task, 2: Update Task, 3: Delete Tasks, 4: View Tasks, 5: Exit: ")) 
        if operation == 1:
            add = input("Enter the task to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been added successfully.")
            
        elif operation == 2:
            updated_value  = input("Enter the task name you want to update: ")
            
            if updated_value in tasks:
                update = input("Enter the new task name: ")
                index = tasks.index(updated_value)
                tasks[index] = update
                print(f"Task '{updated_value}' has been updated to '{update}'.")
                
        elif operation == 3:
            delete_task = input("Enter the task name you want to delete: ")
            if delete_task in tasks:
                index = tasks.index(delete_task)
                del tasks[index]
                print(f"Task '{delete_task}' has been removed successfully.")
                
        elif operation == 4:
            print(f"Today's tasks are \n{tasks}")  
            
        elif operation == 5:
            print("Exiting the Todo App. Goodbye!")
            break
        
        else :
            print("Invalid operation. Please try again.")
           
                    
   