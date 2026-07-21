# histogram
import matplotlib.pyplot as plt
marks = [65, 70, 75, 80, 85, 90, 72, 68, 95, 88, 77, 83, 91, 73, 69, 81, 86, 92, 78, 74]

plt.hist(marks,bins=5,edgecolor='black')
plt.title('marks distribution')
plt.xlabel('marks')
plt.ylabel('frequency')
plt.show()