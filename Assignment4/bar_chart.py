import matplotlib.pyplot as plt
departments = ["CSE", "EEE", "BBA", "Civil", "English"]
students = [250, 180, 300, 120, 150]

bars=plt.bar(departments,students,color=['blue','green','red','orange','purple'])
for bar in bars:
    yval=bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2,yval,yval,ha='center',va='bottom')
plt.title("studnt enrollment by dept")
plt.xlabel("dept")
plt.ylabel("no of students")
plt.show()