import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('test.csv')

x = data['treatment']
y = data['yield']
plt.bar(x, y)
plt.xlabel('Treatments')
plt.ylabel('Yield (kg/ha)')
plt.show()


x = data['treatment']
y = data['height']
plt.bar(x, y)
plt.xlabel('Treatments')
plt.ylabel('Height (cm)')
plt.show()

x = data['treatment']
y = data['size']
plt.bar(x, y)
plt.xlabel('Treatments')
plt.ylabel('Size (cm)')
plt.show()

x = data['treatment']
y = data['weight']
plt.bar(x, y)
plt.xlabel('Treatments')
plt.ylabel('Weight (g)')
plt.show()
