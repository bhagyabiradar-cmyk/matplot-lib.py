import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [28, 30, 29, 32, 31, 33, 30]

plt.plot(days, temperature, marker="o")

plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

plt.grid(True)

plt.show()