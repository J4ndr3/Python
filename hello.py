Student_Number = "17055386"
p = 0
print("0. The student number is:",Student_Number)
for x in Student_Number:
    if int(x) > 1:
        for i in range(2,int(x)):
            if (int(x) % i) == 0:
                break
        else:
            p = p +1
print("1. The number of prime numbers in this student number is:",p)
import random
q = random.randint(25,50)
print("2. The random Number is:",q)
r = round(q/p)
print("3. Number of random strings to generate:",r)
import string
def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for m in range(length))
mylist =[]
i=1
while i < r+1:
    mod = i % 2
    if mod > 0:
        mylist.append(random_string(5))
    else:
        mylist.append(random_string(7))
    i +=1
print("4. List of strings:")
print("**********")
i = 0
for c in mylist:
    print(i,"-",mylist[i])
    i += 1
print("**********")
mylist.sort
print("5. Sorted list of strings:")
print("**********")
i = 0
for c in mylist:
    print(i,"-",mylist[i])
    i += 1
print("**********")
