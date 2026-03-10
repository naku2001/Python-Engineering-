import matplotlib.pyplot as plt

def get_params():
    """Prompts user for simulation parameters."""
    pop = float(input("Enter total population: "))
    init_inf = float(input("Enter initially infected: "))
    contact_rate = float(input("Enter contact rate (beta): "))
    recovery_period = float(input("Enter recovery period (days): "))
    return pop, init_inf, contact_rate, recovery_period

def run_simulation(pop, init_inf, beta, rec_period, s_list, i_list, r_list):
    """Calculates disease progression and appends data to lists."""
    # Day 0 Setup
    s = pop - init_inf
    i = init_inf
    r = 0.0
    gamma = 1 / rec_period
    
    day = 0
    print(f"\n{'Day':<8} {'S':<10} {'I':<10} {'R':<10}")
    print("-" * 40)
    
    # Store and print Day 0
    s_list.append(s)
    i_list.append(i)
    r_list.append(r)
    print(f"Day {day:<4}: {s:>8.2f} {i:>8.2f} {r:>8.2f}")
    
    # Simulation Loop
    while i >= 0.5:
        day += 1
        # Calculate changes based on previous day (the last items in our lists)
        s_prev = s_list[-1]
        i_prev = i_list[-1]
        r_prev = r_list[-1]
        
        # SIR Equations
        new_infections = beta * i_prev * s_prev
        new_recoveries = gamma * i_prev
        
        s_curr = s_prev - new_infections
        i_curr = i_prev + new_infections - new_recoveries
        r_curr = r_prev + new_recoveries
        
        # Update lists
        s_list.append(s_curr)
        i_list.append(i_curr)
        r_list.append(r_curr)
        
        # Update loop variable for condition check
        i = i_curr
        
        print(f"Day {day:<4}: {s_curr:>8.2f} {i_curr:>8.2f} {r_curr:>8.2f}")

def analyze_and_plot(s_list, i_list, r_list):
    """Performs data analysis and generates a line graph."""
    # Analysis
    max_inf = max(i_list)
    peak_day = i_list.index(max_inf)
    duration = len(i_list)
    
    print("\n--- Outbreak Analysis ---")
    print(f"Peak Infectious Count: {max_inf:.2f}")
    print(f"Day of Peak: {peak_day}")
    print(f"Total Duration (including Day 0): {duration} days")
    
    # Plotting
    days = list(range(duration))
    
    plt.plot(days, s_list, label="Susceptible", color="blue")
    plt.plot(days, i_list, label="Infectious", color="red")
    plt.plot(days, r_list, label="Recovered", color="green")
    
    plt.title("SIR Disease Outbreak Simulation")
    plt.xlabel("Days")
    plt.ylabel("Population Count")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Local variable lists
    susceptible_history = []
    infectious_history = []
    recovered_history = []
    
    # Get inputs
    population, initial_infected, beta, recovery_period = get_params()
    
    # Run simulation
    run_simulation(population, initial_infected, beta, recovery_period, 
                   susceptible_history, infectious_history, recovered_history)
    
    # Perform analysis and visualization
    analyze_and_plot(susceptible_history, infectious_history, recovered_history)

if __name__ == "__main__":
    main()