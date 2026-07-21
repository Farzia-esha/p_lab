#task 6: Student performance Dashboard
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 1. Line Plot: Attendance
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
attendance = [85, 88, 90, 87, 92, 95]

axs[0, 0].plot(months, attendance, marker='o')
axs[0, 0].set_title("Monthly Attendance")
axs[0, 0].set_xlabel("Months")
axs[0, 0].set_ylabel("Attendance (%)")
axs[0, 0].grid(True)

# 2. Bar Chart: Marks
subjects = ["Math", "Physics", "Chemistry", "English", "ICT"]
marks = [88, 75, 82, 90, 95]

bars = axs[0, 1].bar(subjects, marks)

for bar in bars:
    yval = bar.get_height()
    axs[0, 1].text(bar.get_x() + bar.get_width()/2, yval, yval,ha='center', va='bottom')

axs[0, 1].set_title("Subject-wise Marks")
axs[0, 1].set_xlabel("Subjects")
axs[0, 1].set_ylabel("Marks")

# 3. Pie Chart: Activities
activities = ["Study", "Sleep", "Exercise", "Entertainment", "Others"]
hours = [6, 8, 1, 3, 6]

axs[1, 0].pie(hours, labels=activities, autopct='%1.1f%%', explode=[0, 0.1, 0, 0, 0])
axs[1, 0].set_title("Daily Time Allocation")

# 4. Histogram: Scores
scores = [65, 70, 75, 80, 85, 90, 72, 68, 95, 88,77, 83, 91, 73, 69, 81, 86, 92, 78, 74]

axs[1, 1].hist(scores, bins=5, edgecolor='black')
axs[1, 1].set_title("Exam Score Distribution")
axs[1, 1].set_xlabel("Scores")
axs[1, 1].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("student_dashboard.png")
plt.show()