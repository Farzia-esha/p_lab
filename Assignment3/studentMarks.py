import numpy as np
marks=np.array([75,80,65,90,85])

print('avg marks:',np.mean(marks))
print('highest marks:',np.max(marks))
print('filterd marks above 80:',marks[marks>80])