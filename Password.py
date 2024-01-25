import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
         'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
         'U','V','W','X','Y','Z']
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=['!','@','#','$','%','^','&','*','(',')','-','+','=']
print("Welcome to password generator!")


n_letters = int(input("Enter how many alphabet you want in your password: "))
n_numbers =int( input("Enter how many numbers you want in your password: " ))
n_symbols = int(input("Enter how many symbols you want in your password: "))

list=[]
for i in range(1,n_letters+1):
    char= str(random.choice(letters))
    list+=char
for i in range(1,n_numbers+1):
    char= str(random.choice(numbers))
    list+=char
for i in range(1,n_symbols+1):
    char= str(random.choice(symbols))
    list+=char

random.shuffle(list)

password=""
for i in list:
    password+=i
print(password)
