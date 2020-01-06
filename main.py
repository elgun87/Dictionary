# Created empty dictionary to add word and then to check if the word in the dictionary
# If yes print the meaning of the word
'''
dictionary = {} 
while True:
    word = input("Enter the word : ")
    if word in dictionary: #checking if the word in the list
        print(f'I have this word in my dictionary  : {dictionary[word]}')
    else:
        add = input("I dont have this word meaning.Please add the meaning : ")
        dictionary [word] = add
'''

## In this program asking the name of the user then inserting his age.
'''
check_list = {} #Created empty dictionary
while True: 
    name = input("What is your name : ")
    if name in check_list: #Checking if the name in the check_list.If yes print the check_list
        print(f'I found you in the system.Your age is {check_list[name]}')
        continue
    number = int(input("what is your age : ")) # asking his age
    check_list[name] = number
    ask = input("Enter the name to find your age : ") #asking his name to find how old is he
    if ask in check_list:
        print(check_list[name])
    else :
        print('We dont have your in our system ')
        number = int(input("what is your age : "))
        check_list [ask] = number
'''
