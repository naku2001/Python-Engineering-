
import matplotlib as mt
def get_simulation_parameters():
    """Prompts the user for input and returns the initial values."""
    print("--- SIR Model Input Parameters ---")
    population = float(input("Enter total population: "))
    initial_infected = float(input("Enter initially infected individuals: "))
    contact_rate = float(input("Enter contact rate (beta): "))
    recovery_period = float(input("Enter recovery period (days): "))
    return population, initial_infected, contact_rate, recovery_period

def run_simulation(pop, initial_i, beta, rec_period, s_list, i_list, r_list):
    """Calculates SIR values and appends them to lists."""
    gamma = 1 / rec_period
    day = 0
    

    s_list.append(pop - initial_i)
    i_list.append(initial_i)
    r_list.append(0.0)

    print(f"\n{'Day':<8} {'S':<12} {'I':<12} {'R':<12}")
    print(f"{day:<8} {s_list[0]:<12.2f} {i_list[0]:<12.2f} {r_list[0]:<12.2f}")

    # 2. Simulation Loop (checks the last item in i_list)
    while i_list[-1] >= 0.5:
        day += 1
        
        # Use [-1] to get the most recent values from the lists
        s_prev = s_list[-1]
        i_prev = i_list[-1]
        r_prev = r_list[-1]

        # SIR Formulas using previous values
        new_s = s_prev - (beta * i_prev * s_prev / pop) # Note: beta often scaled by population
        new_i = i_prev + (beta * i_prev * s_prev / pop) - (gamma * i_prev)
        new_r = r_prev + (gamma * i_prev)

        # 3. Append new values to the lists
        s_list.append(new_s)
        i_list.append(new_i)
        r_list.append(new_r)

        print(f"{day:<8} {new_s:<12.2f} {new_i:<12.2f} {new_r:<12.2f}")

def perform_analysis(s_list, i_list, r_list):
    """Analyzes the results stored in the lists."""
    max_i = 0.0
    peak_day = 0
    
    # Loop through the list to find the highest infection count
    for idx in range(len(i_list)):
        if i_list[idx] > max_i:
            max_i = i_list[idx]
            peak_day = idx
            
    duration = len(i_list) # Total days including Day 0

    print("\n--- Simulation Analysis ---")
    print(f"Highest count of infectious individuals: {max_i:.2f}")
    print(f"Day with highest count: {peak_day}")
    print(f"Duration of outbreak: {duration} days")

def main():
    # 1. Variables defined in main (No Globals!)
    pop, init_i, beta, rec_period = get_simulation_parameters()
    
    # 2. Create the three Lists here as required
    s_vals = []
    i_vals = []
    r_vals = []

    # 3. Pass lists to the simulation to be filled
    run_simulation(pop, init_i, beta, rec_period, s_vals, i_vals, r_vals)
    
    perform_analysis(s_vals, i_vals, r_vals)

    mt.plot()

if __name__ == "__main__":
    main()