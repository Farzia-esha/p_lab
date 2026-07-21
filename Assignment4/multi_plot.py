import matplotlib.pyplot as plt
subjects=['math','physics','chemistry','biology','english','ict']
student_A=[85,78,90,88,76,92]
student_B=[80,82,87,85,79,89]

plt.plot(subjects,student_A,marker='o',linestyle='-',label="Student A")
plt.plot(subjects,student_B,marker='s',linestyle='--',label="Student B")
plt.title('Student performance comparison')
plt.xlabel("subjects")
plt.ylabel("marks")
plt.legend()
plt.grid(True)
plt.show()