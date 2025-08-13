students=("Amit","Vikas","Shruti","Neha")

print(students)

students=students+("Vivek",)
print(students)

#print the last name
print(students[-1])

print(students[::-1])


#delete a student

students_list=list(students)

students_list.remove("Vivek")

print(students_list)
students=tuple(students_list)

print(students)

#d slicing

print("Students from index 1 to 3:",students[1:4])

try:
    students[2] = "Priya"
except TypeError as e:
    print("Error:", e)


# question no. 3

students_age={
    "Amit": 19,
    "Riya": 21,
    "Sahil": 22,
    "Neha": 18,
    "Tina": 25
}


for name,age in students_age.items():
    if age>20:
        print(name)
students_age["Rohan"]=12

print(students_age.items())

# add more student
students_age["Amitabh"]=99

del students_age["Riya"]

print(students_age.items())

avg_age=sum(students_age.values())/len(students_age)
print(avg_age)


# question 4

numbers = [1, 2, 3,3, 4, 1, 12, 1]
evenNum = []  

for i in numbers:
    if i % 2 == 0:
        evenNum.append(i)

print(evenNum)

dupl=set()

for i in numbers:
    if numbers.count(i)>1:
        dupl.add(i)

print(dupl)

s="Shaurya"
print("Reversed String ",s[::-1])

a,b=0,1
print("Fibonacci Series")
for _ in range(5):
    print(a,end=" ")
    a,b=b,a+b



with open("sample.txt", "w") as f:
    f.write("Hi, I am currentlyursuing my BTech from Jaypee.")
print("File content replaced.")
