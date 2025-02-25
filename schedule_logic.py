def generate_schedule(subjects_with_priority, daily_hours):
    # Convert daily hours to minutes
    total_minutes = daily_hours * 60

    # Priority weight mapping (high: 3x time, medium: 2x time, low: 1x time)
    priority_weights = {"high": 3, "medium": 2, "low": 1}

    # Calculate total weight for all subjects
    total_weight = sum(priority_weights[priority] for _, priority in subjects_with_priority)

    # Allocate time for each subject based on priority
    time_allocations = {
        subject: (priority_weights[priority] / total_weight) * total_minutes
        for subject, priority in subjects_with_priority
    }

    # Reserve time for breaks (e.g., 10% of total available time for breaks)
    total_study_time = sum(time_allocations.values())
    total_break_time = int(total_minutes * 0.1)  # Allocate 10% of total time for breaks

    # Dynamically assign break times proportional to study times
    break_times = []
    for _, study_time in time_allocations.items():
        break_time = min(total_break_time * (study_time / total_study_time), study_time * 0.5)
        break_times.append(int(break_time))

    # Adjust break times to fit the total allocated break time
    total_assigned_break_time = sum(break_times)
    if total_assigned_break_time > total_break_time:
        scale_factor = total_break_time / total_assigned_break_time
        break_times = [int(break_time * scale_factor) for break_time in break_times]

    # Create the schedule
    schedule = []
    for i, (subject, _) in enumerate(subjects_with_priority):
        study_time = int(time_allocations[subject])
        schedule.append(f"Study {subject} for {study_time} minutes.")
        if i < len(subjects_with_priority) - 1:  # Add break except after the last session
            schedule.append(f"Take a {break_times[i]}-minute break.")

    return schedule