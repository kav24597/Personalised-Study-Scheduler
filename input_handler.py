# input_handler.py

def get_user_data():
    subjects_input = input("Enter subjects to study, separated by commas: ")
    priorities_input = input("Enter priorities for each subject (high, medium, low), separated by commas: ")
    daily_hours = int(input("Enter the total study hours available per day: "))

    # Convert inputs to appropriate lists
    subjects = [subject.strip() for subject in subjects_input.split(",")]
    priorities = [priority.strip() for priority in priorities_input.split(",")]

    # Pair subjects with their priorities
    subjects_with_priority = list(zip(subjects, priorities))

    return subjects_with_priority, daily_hours