#Assignment 4 : Data Visualization using matplotlib

#Task 1: Line plot
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 160, 200, 220]
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

#Task 2: Multiple line plot
subjects = ["Math", "Physics", "Chemistry", "Biology", "English", "ICT"]
student_A = [85, 78, 90, 88, 76, 92]
student_B = [80, 82, 87, 85, 79, 89]
plt.plot(subjects, student_A, marker='o', linestyle='-', label="Student A")
plt.plot(subjects, student_B, marker='s', linestyle='--', label="Student B")
plt.title("Student Performance Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()

#task 3: Bar Chart
departments = ["CSE", "EEE", "BBA", "Civil", "English"]
students = [250, 180, 300, 120, 150]

bars = plt.bar(departments, students, color=['blue', 'green', 'red',
'purple', 'orange'])
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, yval, ha='center',
va='bottom')
plt.title("Student Enrollment by Department")
plt.xlabel("Departments")
plt.ylabel("Number of Students")
plt.show()

#task 4: Histogram
marks = [65, 70, 75, 80, 85, 90, 72, 68, 95, 88,
77, 83, 91, 73, 69, 81, 86, 92, 78, 74]
plt.hist(marks, bins=5, edgecolor='black')

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

#task 5: pie chart
activities = ["Study", "Sleep", "Exercise", "Entertainment", "Others"]
hours = [6, 8, 1, 4, 5]
plt.pie(hours, labels=activities, autopct='%1.1f%%', explode=[0, 0.1, 0, 0,
0])
plt.title("Daily Activity Distribution")
plt.show()

#task 6: Student performance Dashboard
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
