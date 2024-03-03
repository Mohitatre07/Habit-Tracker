import datetime

# Dictionary to store tasks and their details
tasks = {}

# Function to add a new task
def add_task():
    task_name = input("Enter the name of the task: ")
    priority = input("Enter the priority of the task (high, medium, low): ").lower()
    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
    
    # Parse due date string to a datetime object
    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
        return
    
    reminder = input("Do you want to set a reminder for this task? (yes/no): ").lower()
    if reminder == "yes":
        reminder_date = input("Enter the reminder date (YYYY-MM-DD): ")
        try:
            reminder_date = datetime.datetime.strptime(reminder_date, "%Y-%m-%d").date()
            reminder_time = input("Enter the reminder time (HH:MM): ")
            reminder_datetime = datetime.datetime.strptime(reminder_time, "%H:%M").time()
            reminder_datetime = datetime.datetime.combine(reminder_date, reminder_datetime)
        except ValueError:
            print("Invalid date or time format. Please enter date in YYYY-MM-DD and time in HH:MM format.")
            return
    else:
        reminder_datetime = None
    
    tasks[task_name] = {"priority": priority, "due_date": due_date, "reminder": reminder_datetime}
    print("Task added successfully.")

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print("Tasks:")
        for index, (task_name, details) in enumerate(tasks.items(), start=1):
            print(f"{index}. {task_name} - Priority: {details['priority']}, Due Date: {details['due_date']}")
            if details["reminder"]:
                print(f"   Reminder set for: {details['reminder']}")

# Main function
def main():
    while True:
        print("\n1. Add a new task")
        print("2. Display all tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
