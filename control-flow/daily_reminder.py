# daily_reminder.py

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop (demonstration of control flow)
while True:
    # Match-case for priority handling
    match priority:
        case "high":
            if time_bound == "yes":
                reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            else:
                reminder = f"Reminder: '{task}' is a high priority task. Plan to finish it soon."
        
        case "medium":
            if time_bound == "yes":
                reminder = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
            else:
                reminder = f"Reminder: '{task}' is a medium priority task. Try to schedule it soon."
        
        case "low":
            if time_bound == "yes":
                reminder = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
            else:
                reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
        
        case _:
            reminder = f"Reminder: '{task}' has an unknown priority. Please double-check."

    # Print the customized reminder
    print(reminder)

    # Exit loop after one reminder
    break
