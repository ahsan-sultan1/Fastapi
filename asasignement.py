
# a=6
# b=9
# c=a!=b
# print(c)


# a = "31.2"
# b = float(a) # a but the type should be float
# t = type(b) 

# print(t)


# d = {} # Empty dictionary
# marks = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23
# }


# # print(marks, type(marks))
# print(marks["Harry"])


# e = set() # Dont use s = {} as it will create an empty dictionary
# s = {1, 5, 32, 54,5, 5, 5} 

# print(s)


# s1 = {1, 45, 6, 78}  
# s2 = {7, 8, 1, 78}

# print(s1.union(s2))
# print(s1.intersection(s2))


# marks = []

# f1 = int(input("Enter Marks here: "))
# marks.append(f1)
# f2 = int(input("Enter Marks here: "))
# marks.append(f2)
# f3 = int(input("Enter Marks here: "))
# marks.append(f3)
# f4 = int(input("Enter Marks here: "))
# marks.append(f4)
# f5 = int(input("Enter Marks here: "))
# marks.append(f5)
# f6 = int(input("Enter Marks here: "))
# marks.append(f6)

# marks.sort()

# print(marks)


# friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
# print(friends)
# friends.append("Harry")
# print(friends)


# a = 7
# b = 4
# c = a + b
# print(c)


# a = int(input("Enter your age: "))

# # If elif else ladder
# if(a>=18):
#     print("You are above the age of consent")
#     print("Good for you")

# elif(a<0):
#     print("You are entering an invalid negative age")

# elif(a==0):
#     print("You are entering 0 which is not a valid age")    

# else:
#     print("You are below the age of consent")


# print("End of Program")


# a = int(input("Enter your age: "))

# # If else statement
# if(a>=18):
#     print("You are above the age of consent")
#     print("Good for you")

# else:
#     print("You are below the age of consent")


# print("End of Program")



# def avg():
#     a = int(input("Enter your number: "))
#     b = int(input("Enter your number: "))
#     c = int(input("Enter your number: "))
    
#     average = (a + b + c)/3
#     print(average)
# avg() # Function Call
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# avg()


# def goodDay(name, ending):
#     print("Good Day, " + name)
#     print(ending)
#     return "ok"

# a = goodDay("Harry", "Thank you") 
# print(a)


# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)


# n = int(input("Enter a number: "))
# print(f"The factorial of this number is: {factorial(n)}")



# import random
# '''
# 1 for snake
# -1 for water 
# 0 for gun
# '''
# computer = random.choice([-1, 0, 1])
# youstr = input("Enter your choice: ")
# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# you = youDict[youstr]

# # By now we have 2 numbers (variables), you and computer

# print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# if(computer == you):
#     print("Its a draw")

# else:
#     if(computer ==-1 and you == 1): 
#         print("You win!")

#     elif(computer ==-1 and you == 0):
#         print("You Lose!")

#     elif(computer == 1 and you == -1):
#         print("You lose!")

#     elif(computer ==1 and you == 0):
#         print("You Win!")

#     elif(computer ==0 and you == -1):
#         print("You Win!")

#     elif(computer == 0 and you == 1):
#         print("You Lose!")

#     else:
#         print("Something went wrong!")




# import random
# n = random.randint(1, 100) 
# a = -1
# guesses = 1
# while(a != n):
#     a = int(input("Guess the number: ")) 
#     if(a >n):
#         print("Lower number please")
#         guesses +=1
#     elif(a<n):
#         print("Higher number Please")
#         guesses +=1

# print(f"You have guessed the number {n} correctly in {guesses} attempts")



# import random
# import string

# length = int(input("Password length: "))

# chars = string.ascii_letters + string.digits + string.punctuation

# password = "".join(random.choice(chars) for _ in range(length))

# print("Your password:", password)



# import random

# print("Welcome to Heads or Tails!")
# a = input("Choose Heads or Tails: ").strip().lower()

# if a not in ["heads", "tails"]:
#     print("Invalid choice! Please type 'Heads' or 'Tails'.")
# else:
#     result = random.choice(["heads", "tails"])
#     print(f"The coin landed on: {result.capitalize()}")
    
#     if a == result:
#         print("You win🏆")
#     else:
#         print("You lose💀!")



# if (n := len([1, 2, 3, 4, 5])) > 3: 
#     print(f"List is too long ({n} ")



# def a(status): 
#     match status:  
#         case 200: 
#             return "OK" 
#         case 404: 
#             return "Not Found" 
#         case 500: 
#             return "Internal Server Error" 
#         case _: 
#             return "Unknown status"  


# print(a(5007))



# a=[str(4*i) for i in range (1,11)]
# b="\n".join(a)
# print(b)


# def devide(n):
#     if(n%5==0):
#         return True
#     else:
#         return False
# b=[3,6,7,3,5,666,4535,863,9635,8542,3976,8768]
# f=list(filter(devide,b))
# print(f)




# from tkinter import *

# def click(event):
#     global screen
#     text = event.widget.cget("text")
#     print(text)

#     if text == "=":
#         if screen.get().isdigit():
#             value=int(screen.get())
#         else:
#             eval(screen.get())
#         try:
#             value = eval(screen.get().replace("x", "*"))
#             screen.set(value)
#         except Exception as e:
#             screen.set("Error")
#     elif text == "C":
#         screen.set("")
#     else:
#           screen.set(screen.get() + text)
      

# cal = Tk()
# cal.geometry("350x500")
# cal.title("Calculator")

# screen = StringVar()
# screen.set("")
# lcd = Entry(cal, textvar=screen, font="lavida 33 bold",bg="grey")
# lcd.pack(fill=X, padx=16, pady=25)


# f1 = Frame(cal, bg="grey")
# f1.pack(pady=5)

# for txt in ["1", "2", "3", "4"]:
#     b = Button(f1, text=txt, font="lucida 33 bold")
#     b.pack(side=LEFT, padx=7, pady=6)
#     b.bind("<Button-1>", click)


# f2 = Frame(cal, bg="grey")
# f2.pack(pady=5)

# for txt in ["5", "6", "7", "8"]:
#     b = Button(f2, text=txt, font="lucida 33 bold")
#     b.pack(side=LEFT, padx=7, pady=6)
#     b.bind("<Button-1>", click)


# f3 = Frame(cal, bg="grey")
# f3.pack(pady=5)

# for txt in ["9", "0", "+", "-"]:
#     b = Button(f3, text=txt, font="lucida 33 bold")
#     b.pack(side=LEFT, padx=8, pady=6)
#     b.bind("<Button-1>", click)


# f4 = Frame(cal, bg="grey")
# f4.pack(pady=5)

# for txt in ["/", "x", "C", "="]:
#     b = Button(f4, text=txt, font="lucida 33 bold")
#     b.pack(side=LEFT, padx=8, pady=6)
#     b.bind("<Button-1>", click)


# cal.mainloop()




# num = int(input("Enter a 3-digit number: "))

# # extract digits
# a = num // 100       # hundreds place
# b = (num // 10) % 10 # tens place
# c = num % 10         # ones place

# total = a + b + c

# print("Sum of digits:", total)


# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))

# for num in range(start, end+1):
#     if num > 1:  # 1 prime nahi hai
#         for i in range(2, num):
#             if num % i == 0:
#                 break  # divisible → not prime
#         else:
#             print(num, end=" ")
    


# num = int(input("Number enter karo: "))

# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("number is zero")



# a = int(input("Enter a number: "))

# if a % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)


# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)





# num = 1
# count = 0

# while num <= 100:
#     if num % 2 != 0:   # check if odd
#         print(num)
#         count +=1
#     num += 1

# print("Total odd numbers:", count)





# try:
#     a = input("enter a name: ")
#     b = int(input("enter a age: "))
#     if b > 18:
#      print("welcome to the party", a)
#     else:
#         print("sorry", a, "you are not allowed to enter the party")
# except TypeError:
#      print("wrong value, check variable type")
# else:
#       print("you enter a correct values")




# i=["ahsan","CR","akash","rohan","shubham"]

# first ,* all ,last = i

# print(first)
# print(all)
# print(last)



# def A(text):
#     return text[::-1]
# print(A("Ahsan"))



# a=5
# for i in range(1, a+1):
#     print(" " * (a-i),end="")
#     print("*"*(2*i-1))





def my_book():
    book=[]
    with open ("kitab.txt" ,"r") as file:
        file = file.readlines()
    book=[line.strip() for line in file]

    b=input("Enter a book to add:").strip().title()
    a=input("Enter a book to search:").strip().title()
    if b == "0" :
        pass
    else:
        book.append(b)
        with open("kitab.txt", "a") as file:
           file.write(b + "\n")
        print(book)
        
    if a in book:
     print(a,"is available")
    else:
       print(a,"is not available")
    
# # my_book()






def my_grading():
    a=int(input("Enter math number:").strip())
    b=int(input("Enter english number:").strip())
    c=int(input("Enter urdu number:").strip())
    if a>100 or b>100 or c>100:
        print("Invalid marks entered. enter real marks between 0 and 100.")
        return
    total= a+b+c
    p=round((total/300)*100,2)

    if a < 33 or b < 33 or c < 33:
        print("You Failed in exams and your total percentage is: ",p,"%")
        return

    if p>=80:
        print("Grade is A+")
    elif p>=60:
        print("Grade is B")
    else:
        print("Grade is C")
        
    print("total marks percentage is: ",p,"%")

# # my_grading()




def expense_manager():
    expenses=[]
    total_cost=0
    while True:
     a=input("Enter item name:").strip().title()
     if a=="0":
         break
     
     b=int(input("Enter item cost:").strip())

     expenses.append((a, b))

     print("Item added successfully!")
     print("Current expenses:", expenses)
    for a, b in expenses:
     total_cost +=b
     print(f"* {a}: Rs. {b}")
    print("Total expenses:", total_cost)
# expense_manager()



def phonebook_manager():
    phonebook = {}
    while True:
        name=input("Enter a name: ").strip().title()
        if name == "0":
            break
        number=int(input("Enter a phone number: ").strip())
        phonebook[name] = number
    print("Phonebook:", phonebook)
# # phonebook_manager()




def word_counter():
    vowels = "aeiouAEIOU"
    text = input("Enter a sentence: ").strip()
    words = text.split()
    word_count = len(words)
    print(f"Total number of words: {word_count}")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(f"Total number of vowels: {count}")

# word_counter()






def main_menu():
    while True:
        print("Main Menu:")
        print("1. open My book function:")
        print("2. open My grading function:")
        print("3. open Expense manager function:")
        print("4. open Phonebook manager function:")
        print("5. open Word counter function:")
        print("6. Exit")
        a=int(input("Enter your choice: ").strip())
        if a==1:
            my_book()
        elif a==2:
            my_grading()
        elif a==3:
            expense_manager()
        elif a==4:
            phonebook_manager()
        elif a==5:
            word_counter()
        elif a==6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# main_menu()



# friends=["ali","ahmad","hamza",'umar',"bilal"]
# for a in friends:
#     print(f"Salam {a}, kia hal ha dost?")



# scores = [35, 12, 85, 40, 22]

# fail=0
# Pass=0
# for n in scores:
#     if n >= 33:
#         print(f"{n} par app pass ha ")
#         Pass+=1
#     else:
#         print(f"{n} par app fail ha ")
#         fail+=1

# print(f"Total pass: {Pass}")
# print(f"total fail: {fail}")

        






'''_____opp in python_____'''

# # class in py
# class Student:
    
#     def __init__(self,name):
#         self.fullname = name
#         print("Hy, Ahsan")

# # object in py

# a=Student("Ahsan")
# print(a.fullname)



# class factory:

#     def __init__(self,car_name,car_model):
#         self.name=car_name
#         self.car_model=car_model
#         print("car details is loading....")

# car1=factory("B M W",756)
# print(car1.name, car1.car_model)

# car2= factory("Mercedes",876)
# print(car2.name, car2.car_model)



# class collage:
#     collage_name="Graduate collage"
    
#     def __init__(self,s_class,name):
#         self.name=name
#         self.s_class=s_class
#         print("Students data: ")

#     def welcome(self): # Method in class
#         print("welcome, ",self.s_class)


# s1=collage("ahsan","C3")
# print(s1.name,s1.s_class)
# print(s1.collage_name)
# s1.welcome()

# s2=collage("salman","C3")
# print(s2.name,s2.s_class)
# print(s2.collage_name)
# s2.welcome()



# class students:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     @staticmethod  #static methoad
#     def hy():
#         print("helloooooo")

#     def average(self):
#         sum=0
#         for i in self.marks:
#             sum +=i
#         print("hy",self.name,"your avg score is ", sum/4)


# s1=students("ahsan",[86,76,91,92])
# s1.average()
# s1.hy()




# class showroom:
#     def __init__(self,show1,show2):
#         self.show1=show1
#         self.show2=show2
        
    
#     def customer_showroom(self):

#         a=input("Enter car name: ")
#         if a in self.show1:  # abstraction  unnesscary detail  user not see this hide
#             print("Yes, availble") # nesscary detail user see this
#         else:
#             print("sorry, not availble")
#         b=input("Enter car color: ")
#         if b in self.show2:
#             print(f"Yes, {b} color is avalible in {a}.")
#         else:
#             print(f"Not avaible {b} color in {a}.")

# showroom1=showroom("BMW",["black","blue","green"]) 
# showroom1.customer_showroom()




'''Abstraction'''
# hiding the implemention detail of a class and only show the essential features to the user.

'''Encapsulation'''
# wrapping data and function into a singal unit ( object ).



# class account:
#     def __init__(self,balance,account_no):
#         self.balance=balance
#         self.accountno=account_no

#     def credit(self,ammount):
#         self.balance -=ammount
#         print("Rs.",ammount, "was credited")
#         print("total balance = ", self.total_balance())
        
#     def debit(self,ammount):
#         self.balance +=ammount
#         print("Rs.",ammount, "was debited")
#         print("total balance = ", self.total_balance())

#     def total_balance(self):
#         return self.balance


# acc1=account(10000 , 13457896) 
# acc1.credit(2000)
# acc1.debit(600)
# acc1.debit(30000)
# acc1.credit(10000)




# class student:
#     def __init__(self,name):
#         self.name=name

# a=student("Ahsan")

# del a
# print(a.name)



# class number:
#     def __init__(self,number):
#          self.__number=number # private att and obj

#     def reset_pas(self): # private object only access in inside the class.
#         print(b1.__number)

# b1=number("23456774")
# b1.reset_pas()
# print(b1.number)






# class car:
#     def __init__(self,type):
#        self.type=type
       
#     @staticmethod
#     def start():
#         print("car started...")
    
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class honda(car):
#     def __init__(self,name,type):
#      self.name=name
#      super().__init__(type)  # super method

# car1=honda("honda city","petrol")
# car2=honda("perfect","electric")
# print(car1.type,car2.name)




# class var:
#     car="toyota"
    
#     # def name(self,car):
#     #     self.__class__.car="yarrr"

#     @classmethod
#     def name(cls,name):
#         cls.name=name
  
# car1= var()
# car1.name("suzuki")
# print(car1.name)
# print(var.name)




# @property is decorator in python 



# GUI Tkinter in python

import tkinter as tk
root_gui=tk.Tk()


# width x height
root_gui.title("HY , welcome.....................")


root_gui.geometry("444x330")
root_gui.minsize(200, 100)
root_gui.maxsize(700 , 600)

# text= Label(text=("Hy everyone........")).pack()

# pic= PhotoImage(file=("codev.png"))
# pic_label=Label(image=pic).pack()


# entry = tk.Entry(root_gui, width=30)
# entry.pack(pady=10)

# label = tk.Label(root_gui,text="welcome")
# label.pack(pady=20)

# def hit_i():
#     label.config(text="button are clicked")

# button = tk.Button(root_gui , text="click here" , command=hit_i)
# button.pack(pady=20)

# root_gui.mainloop()

