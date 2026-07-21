#1.Remove duplicate from list
data=[10,20,20,30,40,40]
unique_data=list(dict.fromkeys(data))
print(unique_data)

#2.find max min
data=[10,20,20,30,40,40]
maxi=max(data)
mini=min(data)
print("maximum:",maxi)
print("minimum:",mini)

#3.sort a list 
data=[8,3,1,6,2]
data.sort()
print("Ascending order:",data)
data.sort(reverse=True)
print("Descending order:",data)

#4. modify a tuple( Converting into list & then back to tuple)
t=(1,2,3,4,5)
#convert tuple into list
lst=list(t)

lst[2]=10 #modify indx 2

t=tuple(lst)  # cnvt lst to tuple

print("updated tuple:",t)

#5.perform set operation (union,intersection,diff on 2 sets)
A={1,2,3,4}
B={3,4,5,6}

#union
union_set=A.union(B)

#intersection
inter_set=A.intersection(B)

#diff
diff_set=A.difference(B)

print("union:",union_set)
print("intersction:",inter_set)
print("difference:", diff_set)

#6. check ele in set
s={10,20,30,40}
check=20

if check in s:
    print("ele exists in the set")
else:
    print("does not exist")
#7. dictionary operations
student= {'A': 80, 'B':75, 'C':90}

#add new std
student['D']=85

#update marks
student['B']=82

#find std with highest marks
h=max(student, key=student.get)

print("Updated dictionary:",student)
print("Highest marks:",h ,"=", student[h])

#8. count frequency of ele
data=[1,2,2,2,3,3,3]
frequency={}

for i in data:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)
#9. find common ele between 2 sets
A= {1,2,3,4}
B={3,4,5}
common= A.intersection(B)
print("Common elements:",common)

#10. create dict from 2 lists
keys=['a','b','c']
values=[1,2,3]
result=dict(zip(keys,values))
print(result)

#11. Word frequency( advanced)
from collections import Counter
sentence="apple banana apple orange banana apple"

#cnvt sent into a lst of words
words=sentence.split()

#count word frequency
frequency={}
count= dict(Counter(words))

#find unique words
unique_w =set(words)

print("word frequency:", count)
print("unique words:", unique_w)

# Advance problems
#1.Problem: Numbers 1-20. Replace multiples of 3 with 'Fizz', 5 with 'Buzz', both with 'FizzBuzz'.   
result=[]

for i in range(1,16):
    if i%3==0 & i%5==0:
        result.append("FizzBuzz")
    elif i%3==0:
        result.append("Fizz")
    elif i%5==0:
        result.append("Buzz")
    else:
        result.append(i)
print(result)

#2.removing negative values( filtering)
temps = [22, -5, 18, -1, 30, 25, -10]

positive = [i for i in temps if i > 0]

print(positive)

#3. E-commerce analysis
sales_data = [ 
(101, "Laptop", "Electronics", 1200), 
(102, "Mouse", "Electronics", 25), 
(101, "Laptop", "Electronics", 1200),  # Duplicate 
(103, "Monitor", "Electronics", 300), 
(104, "Desk Chair", "Furniture", 150), 
(105, "Lamp", "Furniture", 45), 
(106, "Mouse", "Electronics", 25) 
] 
unique_sales = list(set(sales_data)) 
category_products = {} 
product_revenue = {} 
for _, name, cat, price in unique_sales: 
    if cat not in category_products: 
        category_products[cat] = set() 
        category_products[cat].add(name) 
# Revenue 
product_revenue[name] = product_revenue.get(name, 0) + price 
print("--- Unique Products per Category ---") 
for cat, prods in category_products.items(): 
    print(f"{cat}: {prods}") 
print("\n--- Total Revenue per Product ---") 
for prod, rev in product_revenue.items(): 
    print(f"{prod}: ${rev}") 

#4.multi source log aggregator
raw_logs = [
    ("10:00:01", "192.168.1.1", 200),
    ("10:00:02", "192.168.1.5", 404),
    ("10:00:02", "192.168.1.5", 404),  # Duplicate
    ("10:00:03", "192.168.1.1", 500),
    ("10:00:04", "172.16.0.45", 403),
    ("10:00:05", "192.168.1.1", 200),
    ("10:00:06", "172.16.0.45", 403)   # Duplicate
]

# I. Remove duplicate logs
unique_logs = set(raw_logs)

# II & III. Filter Error logs and Group by IP
error_report = {}

# IV. Store unique attackers
attackers = set()

for timestamp, ip, status in unique_logs:
    
    # Error status code (400-599)
    if 400 <= status <= 599:
        
        # Group timestamps by IP
        if ip not in error_report:
            error_report[ip] = []
            
        error_report[ip].append(timestamp)

        # Add IP to attackers set
        attackers.add(ip)


# Output
print("--- Error Report (IP: Timestamps) ---")

for ip, timestamps in error_report.items():
    print(ip + ":", timestamps)

print("Total Unique Attackers:", len(attackers))
print("Attacker List:", attackers)

#5. std performance analysis
from collections import defaultdict

# Raw academic records
academic_records = [
    ("CS", "Alice", "Python", 90),
    ("Math", "Bob", "Calculus", 80),
    ("CS", "Alice", "Python", 90),   # Duplicate record
    ("CS", "Charlie", "C++", 70),
    ("Math", "Bob", "Algebra", 70),
    ("Physics", "David", "Optics", 85),
    ("CS", "Alice", "Algorithms", 95)
]

# I. Remove duplicate records using Set
unique_records = set(academic_records)

# II. Group scores by Department using defaultdict
department_scores = defaultdict(list)
department_students = defaultdict(set)

for dept, student, subject, score in unique_records:
    
    # Store scores
    department_scores[dept].append(score)
    
    # Store unique students
    department_students[dept].add(student)


# III. Create final Dictionary
result = {}

for dept in department_scores:
    total_students = len(department_students[dept])
    
    avg_score = sum(department_scores[dept]) / len(department_scores[dept])
    
    result[dept] = (total_students, avg_score)


# IV. Print in alphabetical order
print("Department | Unique Students | Avg Score")
print("---------------------------------------------")

for dept in sorted(result):
    print(dept, "|", result[dept][0], "|", result[dept][1])
