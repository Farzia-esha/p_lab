#pie chart
import matplotlib.pyplot as plt
activities = ["Study", "Sleep", "Exercise", "Entertainment","Others"]
hours = [6, 8, 1, 4, 5]

plt.pie(hours,labels=activities, autopct='%1.1f%%', explode=[0,0.1,0,0,0])
plt.title("Daily Activity Distribution")
plt.show()