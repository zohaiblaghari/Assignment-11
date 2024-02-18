def categorize_task(due_date):
    if due_date == "urgent":
        category = "Urgent"
    elif due_date == "important":
        category = "Important"
    else:
        category = "Less Important"
    return category

todo_list = []

while True:
    task_name = input("Enter the name of the task (or 'quit' to exit):")
    if task_name.lower() == "quit":
        break
    due_date = input("Is the task due soon (urgent),moderately soon (important), or not urgent (less important)?")
    category = categorize_task(due_date.lower())
    todo_list.append((task_name, category))

print("\nYour To-Do List:")
for idx,task in enumerate(todo_list,start=1):
    print(f"{idx}.Task:{task[0]} | Category:{task[1]}")