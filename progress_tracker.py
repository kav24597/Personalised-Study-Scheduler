# progress_tracker.py

import time

def track_progress(schedule):
    print("\nStarting your study sessions...\n")
    for i, block in enumerate(schedule):
        print(f"Session {i + 1}: {block}")
        input("Press Enter when you've completed this session: ")
        print("Great job! Moving to the next session.")
        time.sleep(2)  # Optional pause to simulate breaks