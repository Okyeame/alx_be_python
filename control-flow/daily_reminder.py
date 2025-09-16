# daily_reminder.py

# Ask the user for inputs
task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is this it time-bound? (yes/no): ").lower()

# Loop just to demonstrate control flow (runs once here)
while True:
    # Use match-case to handle priority
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a HIGH priority task."
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task."
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task."
        case _:
            reminder = f"Reminder: '{task}' has an unknown priority."

    # Check if the task is time-bound
    if time_bound == "yes":
        reminder += " This requires immediate attention today!"

    # Print the customized reminder
    print(reminder)

    # Break the loop after showing the reminder once
    break
