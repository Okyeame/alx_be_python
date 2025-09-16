# daily_reminder.py

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop (to demonstrate control flow, though it runs once here)
while True:
    # Use match-case for priority handling
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            reminder = f"Reminder: '{task}' has an unknown priority level."

    # Check if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    # Print the reminder
    print("\n" + reminder)

    # Exit loop (we only need one reminder)
    break
