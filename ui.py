import tkinter as tk
from tkinter import messagebox, ttk
from schedule_project.modules.schedule_logic import generate_schedule


def start_gui():
    root = tk.Tk()
    root.title("Smart Study Planner")
    root.geometry("600x500")
    root.configure(bg="#f0f8ff")
    
    tk.Label(root, text="Study Schedule Planner", font=("Arial", 18, "bold"), bg="#4682B4", fg="white").pack(fill=tk.X, pady=10)
    
    tk.Label(root, text="Enter subjects (comma-separated):", bg="#f0f8ff").pack()
    subject_entry = tk.Entry(root, width=50)
    subject_entry.pack(pady=5)
    
    tk.Label(root, text="Enter priorities (high, medium, low, comma-separated):", bg="#f0f8ff").pack()
    priority_entry = tk.Entry(root, width=50)
    priority_entry.pack(pady=5)
    
    tk.Label(root, text="Enter total study hours per day:", bg="#f0f8ff").pack()
    time_entry = tk.Entry(root, width=10)
    time_entry.pack(pady=5)
    
    schedule_text = tk.StringVar()
    
    def generate_and_display_schedule():
        subjects = subject_entry.get().split(',')
        priorities = priority_entry.get().split(',')
        try:
            total_time = int(time_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for total study hours!")
            return
        
        if len(subjects) != len(priorities):
            messagebox.showerror("Input Error", "Subjects and priorities count must be the same!")
            return
        
        subjects_with_priority = list(zip([s.strip() for s in subjects], [p.strip() for p in priorities]))
        schedule = generate_schedule(subjects_with_priority, total_time)
        
        schedule_text.set("\n".join(schedule))
        start_button.config(state=tk.NORMAL)
        
    schedule_display = tk.Label(root, textvariable=schedule_text, fg="blue", font=("Arial", 12), bg="#f0f8ff", wraplength=500, justify="left")
    schedule_display.pack(pady=10)
    
    generate_button = tk.Button(root, text="Generate Schedule", command=generate_and_display_schedule, bg="green", fg="gray", font=("Arial", 12, "bold"))
    generate_button.pack(pady=10)
    
    def start_study_sessions(index=0):
        study_plan = schedule_text.get().split("\n")
        if index < len(study_plan):
            messagebox.showinfo("Study Session", f"Session {index+1}: {study_plan[index]}")
            root.after(2000, start_study_sessions, index+1)  # Wait for 2 seconds before showing the next session
        else:
            messagebox.showinfo("Completed!", "All study sessions completed! Good job!")
    
    start_button = tk.Button(root, text="Start Study Session", command=lambda: start_study_sessions(0), bg="blue", fg="white", font=("Arial", 12, "bold"), state=tk.DISABLED)
    start_button.pack(pady=10)
    
    root.mainloop()
    
if __name__ == "__main__":
    start_gui()