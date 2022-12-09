#the loop variable is updated automatically
for j in range(10):
    print(j * 5)

print("--------------------------------" )

#repeat a string as many times as indicated by the value of the loop variable
for num in range(4):
    print("Hello" * num)

print("--------------------------------" )

#built in data structures such a lists
my_list = ["a", "b","c","d"]
for i in range(len(my_list)):
    print(my_list[i])

print("--------------------------------" )

#when use range(len(<seq>)) we get the sequence of numbers that goes from 0 up to
# len(<seq>)-1
for i in range(2, 5):
    print(i)

print("--------------------------------" )

#three parameters
for i in range(3,16,2):
    print(i)

print("--------------------------------" )

my_list = ["a", "b", "c", "d", "e", "f", "g"]
for i in range(len(my_list)-1, 2, -1):
    print(my_list[i])

print("--------------------------------" )

message= "Hello, World"
for char in message:
    print(char)

print("--------------------------------" )
word = "Hello"

for char in word.upper(): # calling the string method
    print(char)

print("--------------------------------" )
#When it is found during the execution of the loop,
# the current iteration stops and a new one begins with the updated value of the loop variable
my_list = [1, 2, 3, 4, 5]

for elem in my_list:
    if elem % 2 == 0:
        print("continue")
        continue
    print("Odd:", elem)
