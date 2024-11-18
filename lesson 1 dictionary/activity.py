#Write a program that uses a dictionary that contains ten usernames and passwords.
#The program should ask the user to enter their username and password.
#If the username is not in the dictionary, the program should indicate that the person is not a valid user 
#of the system. If the username is in the dictionary, but the user does not enter the right password, 
#the program should say that the password is invalid. If the password is correct, 
#then the program should tell the user that they are now logged in to the system
thing={
    'JOSHYBOY8562':'Pa55w0rd',
    'BarruTheKid':'i234s6789',
    '@\/@':'/@@\ ',
    'YacobHanocby':'ThisIsMyRealName',
    '({[]})':'qwertyuiopasdfghjklzxcvbnm',
    'AlvinTheDalmation8590':'PaSsW0rD',
    'EPICGUY4628':'8264YUGCIPE',
    '1234567890QWERTYUIOPASDFGHJKLZXCVBNM':'!@£$%^&*()_+§±:[]"{|<}><>?:"|{!@£$%^&*()_?,./;',
    'Paswod':'eye can totale spel',
    'Guest2696':'g6o3cy96d!gd8'

}
username=input("Please write your username, so we can get you deta... umm we meant log you in.")
password=input("We still need your password to hack your accou... umm we mean log you in.")
if username not in thing:
    print("This is not a valid username!")
else:
    if thing[username]==password:
        print("Thank you, we now have everything we need to hack your accou... umm sorry, we mean you are now logged in!(:")
    else:
        print("invalid password")
