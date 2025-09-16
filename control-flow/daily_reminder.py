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
                reminder = f"🚨 Reminder: '{task}' is a HIGH priority task that requires immediate attention today!"
            else:
                reminder = f"Reminder: '{task}' is a HIGH priority task. Plan to finish it as soon as possible."
        
        case "medium":
            if time_bound == "yes":
                reminder = f"⚠️ Reminder: '{task}' is a MEDIUM priority task, but since it's time-sensitive, do it today!"
            else:
                reminder = f"Reminder: '{task}' is a MEDIUM priority task. Try to schedule it soon."
        
        case "low":
            if time_bound == "yes":
                reminder = f"⏰ Reminder: '{task}' is a LOW priority task, but it is time-bound, so handle it today!"
            else:
                reminder = f"Note: '{task}' is a LOW priority task. Do it when you have free time."
        
        case _:
            reminder = f"Reminder: '{task}' has an unknown priority. Please double-check."

    # Print the customized reminder
    print("\n" + reminder)

    # Exit loop after one reminder
    break
