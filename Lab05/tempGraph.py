# Author: Perfect Makuwerere
# Date: 02/24/2026
# Description: Plotting cities against temperature

import matplotlib.pyplot as plt
import random

time = list(range(1, 13))

cities = ["Denton", "Allentown", "Raritan"]

for city in cities:
    
    city_temps = []
    
   
    for _ in range(12):
        city_temps.append(random.randint(10, 30))
    
   
    plt.plot(time, city_temps)


plt.title("Hourly Temperatures")


plt.xlabel("Hours")
plt.ylabel("Temperature")

plt.legend(cities)

plt.show()