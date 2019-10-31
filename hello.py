Student_Number = "17055386"
p = 0
print("0. The student number is:",Student_Number,"\n")
for x in Student_Number:
    if int(x) > 1:
        for i in range(2,int(x)):
            if (int(x) % i) == 0:
                break
        else:
            # print(x)
            p = p +1
print("1. The number of prime numbers in this student number is:",p,"\n")
import random
q = random.randint(25,50)
print("2. The random Number is:",q,"\n")
r = round(q/p)
print("3. Number of random strings to generate:",r,"\n")
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
print("**********\n")
def vowel_count_test(string):
    count=0
    for z in string:
        if z in ['a','e','i','o','u']:
            count=count+1
    return count
def sort_by_vowel_count(words):
    return words.sort(key=vowel_count_test,reverse=True)
print("5. Sorted list of strings:")
print("**********")
sort_by_vowel_count(mylist)
i = 0
for c in mylist:
    print(i,"-",mylist[i], "(vowels:",vowel_count_test(mylist[i]),")")
    i += 1
print("**********")
