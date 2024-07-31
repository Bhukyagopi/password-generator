import random as rd
import string
while True:  
    length=int(input("enter the length of the password:"))
    character_list=''
    letters=input("do u want letters in your password(yes/no):").lower()=='yes'
    digits=input("do u want digits in your password(yes/no):").lower()=='yes'
    punctuations=input("do u want punctuations in your password(yes/no):").lower()=='yes'
    if letters:
        character_list+=string.ascii_letters
    if digits:
        character_list+=string.digits
    if punctuations:
        character_list+=string.punctuation
    if character_list: 
        password=''
        for i in range(length):
            randomchar=rd.choice(character_list)
            password+=randomchar
        print("The random Password is:",password)
        ans=input("do u want to generate another password(yes/no):").lower()=='no'
        if ans:
            break
    else:
        print("select any one of them")