import time

# --- Configuration for simulation (in seconds for quick demo, but represents minutes) ---
# Time required for a core focused task (e.g., planning, coding, problem-solving)
FOCUSED_WORK_DURATION = 10 # Represents 10 minutes of actual work

# Time spent on a typical morning distraction (e.g., checking emails, messages)
DISTRACTION_DURATION = 5   # Represents 5 minutes spent on email/Slack

# The hidden cost of context switching: time lost to regain focus after a distraction.
# This is the "15 minutes" the article refers to, added when focus is broken early.
CONTEXT_SWITCH_COST = 15   # Represents 15 minutes to re-focus

def perform_focused_work(task_name):
    """Simulates performing a focused work task."""
    print(f"  --> Starting focused work: '{task_name}' for {FOCUSED_WORK_DURATION} seconds...")
    time.sleep(FOCUSED_WORK_DURATION)
    print(f"  <-- Finished focused work: '{task_name}'.")

def engage_in_distraction(distraction_name):
    """Simulates engaging in a distraction."""
    print(f"  --> Engaging in distraction: '{distraction_name}' for {DISTRACTION_DURATION} seconds...")
    time.sleep(DISTRACTION_DURATION)
    print(f"  <-- Finished distraction: '{distraction_name}'.")

def pay_context_switch_cost():
    """Simulates the time lost due to context switching."""
    print(f"  !!! Paying context switch cost: {CONTEXT_SWITCH_COST} seconds to regain focus...")
    time.sleep(CONTEXT_SWITCH_COST)
    print(f"  !!! Focus regained.")

print("--- Morning Routine Simulation: The Cost of Distraction ---")
print(f"  (Note: Durations are in seconds for demo purposes, representing minutes in real life)")
print(f"  Focused Work: {FOCUSED_WORK_DURATION}s | Distraction: {DISTRACTION_DURATION}s | Context Switch Cost: {CONTEXT_SWITCH_COST}s\n")

# --- Scenario 1: Distraction-First Morning ---
print("Scenario 1: Checking emails/messages FIRST (Distraction-First)")
start_time_scenario1 = time.time()

engage_in_distraction("Checking morning emails and messages") # The article's "E-posta ve Mesajlaşma Bataklığı"
pay_context_switch_cost() # The hidden cost of starting with distractions
perform_focused_work("Planning daily tasks and priorities")

end_time_scenario1 = time.time()
total_time_scenario1 = round(end_time_scenario1 - start_time_scenario1)
print(f"\nTotal time for Scenario 1 (Distraction-First): {total_time_scenario1} seconds.")
print("-" * 50 + "\n")

# --- Scenario 2: Focused-Work-First Morning ---
print("Scenario 2: Doing focused work FIRST (Focused-Work-First)")
start_time_scenario2 = time.time()

perform_focused_work("Planning daily tasks and priorities")
engage_in_distraction("Checking morning emails and messages") # Now, after focused work

end_time_scenario2 = time.time()
total_time_scenario2 = round(end_time_scenario2 - start_time_scenario2)
print(f"\nTotal time for Scenario 2 (Focused-Work-First): {total_time_scenario2} seconds.")
print("-" * 50 + "\n")

# --- Comparison ---
time_difference = total_time_scenario1 - total_time_scenario2
print(f"Comparison:")
print(f"  Distraction-First took: {total_time_scenario1} seconds")
print(f"  Focused-Work-First took: {total_time_scenario2} seconds")
print(f"  Difference: {time_difference} seconds.")
print(f"  This {time_difference} seconds difference illustrates the '15 minutes lost' concept from the article,")
print(f"  primarily due to the {CONTEXT_SWITCH_COST} seconds context switch cost when starting with distractions.")
