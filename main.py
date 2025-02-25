from schedule_project.modules.input_handler import get_user_data
from schedule_project.modules.schedule_logic import generate_schedule
from schedule_project.modules.progress_tracker import track_progress
from schedule_project.modules.ui import start_gui

def main():
    print("Welcome to the Smart Study Scheduler!")
    choice = input("Do you want to use the CLI or GUI? (cli/gui): ").strip().lower()
    
    if choice == "cli":
        subjects_with_priority, daily_hours = get_user_data()
        study_schedule = generate_schedule(subjects_with_priority, daily_hours)
        
        print("\nGenerated Study Schedule:")
        for session in study_schedule:
            print(session)
        
        start = input("Do you want to start tracking your study sessions? (yes/no): ").strip().lower()
        if start == "yes":
            track_progress(study_schedule)
        else:
            print("You can start later by running the program again!")
    
    elif choice == "gui":
        start_gui()
    
    else:
        print("Invalid choice. Please restart and enter 'cli' or 'gui'.")

if __name__ == "__main__":
    main()
