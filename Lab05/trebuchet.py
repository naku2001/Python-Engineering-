# Author: Perfect Makuwerere
# Date: 02/24/2026
# Description: A small description in your own words that describes what

top_distances = [0, 0, 0]
top_trials = [0, 0, 0]

continue_input = "Y"
current_trial = 1


while continue_input.upper() == "Y":
    print(f"\n--- Trial #{current_trial} ---")
    new_distance = int(input("Enter the distance for this trial (in meters): "))

    
    if new_distance > top_distances[0]:
        
        top_distances[2] = top_distances[1]
        top_trials[2] = top_trials[1]
        top_distances[1] = top_distances[0]
        top_trials[1] = top_trials[0]
        top_distances[0] = new_distance
        top_trials[0] = current_trial
        print("New Personal Best!")

    elif new_distance > top_distances[1]:
        top_distances[2] = top_distances[1]
        top_trials[2] = top_trials[1]
        top_distances[1] = new_distance
        top_trials[1] = current_trial
        print("New Second Best!")

    elif new_distance > top_distances[2]:
        top_distances[2] = new_distance
        top_trials[2] = current_trial
        print("New Third Best!")
    
    else:
        print("Trial did not make the top three.")

    continue_input = input("\nWould you like to enter another trial? (Y/N): ")
    current_trial += 1

print("\n" + "="*20)
print("TOP THREE DISTANCES")
print("="*20)

print(f"{'Trial':<10} {'Distance':<10}")
print("-" * 20)

for i in range(3):
    print(f"{top_trials[i]:<10} {top_distances[i]:<10}")