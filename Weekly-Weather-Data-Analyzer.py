#15 Weekly Weather Data Analyzer
import numpy as np

print("🌤️ Weekly Weather Data Analyzer")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Input temperature data
temps = []
for day in days:
    temp = float(input(f"Enter temperature for {day} (°C): "))
    temps.append(temp)

temps_np = np.array(temps)

# Analysis
avg_temp = np.mean(temps_np)
max_temp = np.max(temps_np)
min_temp = np.min(temps_np)
variance = np.var(temps_np)

print("\n📊 Weather Summary:")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Maximum Temperature: {max_temp:.2f} °C")
print(f"Minimum Temperature: {min_temp:.2f} °C")
print(f"Temperature Variance: {variance:.2f}")

# Days hotter than average
above_avg_days = [days[i] for i in range(len(days)) if temps_np[i] > avg_temp]
print(f"Days with temperature above average: {', '.join(above_avg_days)}")
