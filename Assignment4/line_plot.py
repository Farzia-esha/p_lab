import matplotlib.pyplot as plt
months=["jan","feb","mar","apr","may","jun"]
sales=[120,150,170,160,180,220]

plt.plot(months,sales,marker='o')
plt.title("Monthly sales trend")
plt.xlabel("months")
plt.ylabel("sales")
plt.grid(True)
plt.show()