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
                print(f"Reminder: '{task}' is HIGH priority and urgent — complete it immediately today!")
            else:
                print(f"Reminder: '{task}' is HIGH priority. Make sure you finish it soon.")
        
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is MEDIUM priority but urgent — don’t delay, finish it today!")
            else:
                print(f"Reminder: '{task}' is MEDIUM priority. Try to schedule it in your day.")
        
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is LOW priority but urgent — it still needs to be done today!")
            else:
                print(f"Reminder: '{task}' is LOW priority. Do it when you have free time.")
        
        case _:
            print(f"Reminder: '{task}' has an unknown priority. Please double-check what you entered.")

    # Exit loop after one reminder
    break
