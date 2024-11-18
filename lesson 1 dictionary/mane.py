'''for i in range(1000000):
    print(i)
    i=i+1'''
   
#creating dictinary
student={
    'name':'Bobby mc Bobson BobbyBob',
    'age':12.42149052123145798235469,
    'subject':'Dogs!'
}
print(student['subject'])
# getting all keys
print(student.keys())
#getting all values
print(student.values())
print(student.items())
#if a key exists
if "Dogs!" in student:
    print("I know your watching me... FBI!")
#it doesnt by the way
#changing values
student["age"]=198.2134231567021567032485640125213563
print(student['age'])
for key in student:
    print(key)
#Write a program that uses a dictionary that contains ten usernames and passwords. The program should ask the user to enter their username and password. If the username is not in the dictionary, the program should indicate that the person is not a valid user of the system. If the username is in the dictionary, but the user does not enter the right password, the program should say that the password is invalid. If the password is correct, then the program should tell the user that they are now logged in to the system.