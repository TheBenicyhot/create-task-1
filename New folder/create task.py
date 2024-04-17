import time 
import turtle as trtl


from playsound import playsound



wn = trtl.Screen()
wn.setup(width=800, height=600)
trtl.hideturtle()
trtl.penup()
trtl.goto(-225,175)
trtl.write("what is your bi-weekly income in January?")
print("what is your bi-weekly income in January?")
Janincome = int(input("->"))
monthly_income = Janincome * 2
if Janincome >= 5000:
    wn.clear()
    trtl.hideturtle()
    trtl.penup()
    trtl.goto(-225,250) 
    trtl.write("why do you need financial advice if you make so much money")
    print("why do you need financial advice if you make so much money")
    wn.bgpic("walter.gif")
    wn.update()
    playsound("money.mp3")
    time.sleep(3)
elif monthly_income < 2000 :
    wn.clear()
    trtl.hideturtle()
    trtl.penup()
    trtl.goto(-200,175) 
    trtl.write("you are broke how are you even alive in this economy")
    print( "you are broke how are you even alive in this economy")
    wn.bgpic("hobo.gif")
else:
    trtl.goto(-200,165)
    trtl.write("Your monthly income will be close to " + str(monthly_income) + " dollars")
    print("Your monthly income will be close to ", monthly_income, " dollars")
    deductions = [0.35, 0.10, 0.15, 0.15, 0.20, 0.05]
    'rent , food , utilities, car, savings, entertainment'
    rent = monthly_income * deductions[0]
    print(rent, "dollars should be going to rent")
    food = monthly_income * deductions[1]
    print(food, "dollars should be going to food")
    utilities = monthly_income * deductions[2]
    print(utilities, "dollars should be going to utilities")
    car = monthly_income * deductions[3]
    print(car, "dollars should be going to car")
    savings = monthly_income * deductions[4]
    print(savings, "dollars should be going to savings")
    entertainment = monthly_income * deductions[5]
    print(entertainment, "dollars should be going to entertainment")
   
    time.sleep(2)
    trtl.goto(-200,155)
    trtl.write(str(rent)+ "dollars should be going to rent")
    trtl.goto(-200,145)
    trtl.write(str(food)+ "dollars should be going to rent")
    trtl.goto(-200,135)
    trtl.write(str(utilities)+ "dollars should be going to rent")
    trtl.goto(-200,125)
    trtl.write(str(car)+ "dollars should be going to rent")
    trtl.goto(-200,115)
    trtl.write(str(savings)+ "dollars should be going to rent")
    trtl.goto(-200,105)
    trtl.write(str(entertainment)+ "dollars should be going to rent")
    

    trtl.goto(-200,95)
    trtl.write("what is your bi-weekly in February?")
    print("what is your bi-weekly in February?")
    Febincome = int(input("->"))
    if Febincome > Janincome:
        trtl.goto(-200,85)
        trtl.write("you made a profit keep it up and you will be a millionaire")
        print("you made a profit keep it up and you will be a millionaire")
        time.sleep(2)
        trtl.goto(-200,75)
        trtl.write("their are always ways to increase your wealth even further")
        print("their are always ways to increase your wealth even further")
        time.sleep(2)
        wn.clear()
        wn.bgpic("money.gif")
        trtl.penup()
        trtl.goto(-200,-187)
        trtl.write("you can invest your money in stocks, bonds, real estate, and even cars")
        print( "you can invest your money in stocks, bonds, real estate, and even cars")
    elif Febincome == Janincome:
        trtl.goto(-200,85)
        trtl.write("you broke even not good or bad ")
        print("you broke even not good or bad ")
        time.sleep(2)
        trtl.goto(-200,75)
        trtl.write("here are some things that can help improve your finances")
        print("here are some things that can help improve your finances ")
    else:
        trtl.goto(-200,85)
        trtl.write(" you made a loss you should be more careful")
        print("you made a loss you should be more careful")
        time.sleep(2)
        trtl.goto(-200,75)
        trtl.write("here are some things that can help improve your finances ")
        print("here are some things that can help improve your finances ")
    if Febincome <= Janincome:
        time.sleep(2)
        trtl.goto(-200,65)
        trtl.write("you should consider job hoping ")
        print("you should consider job hoping")
        time.sleep(2)
        trtl.goto(-200,55)
        trtl.write("around 75 percent of people get a 7-10 percent increase to their salary when they job hop ")
        print("around 75 percent of people get a 7-10 percent increase to their salary when they job hop")
        time.sleep(2)
        trtl.goto(-200,45)
        trtl.write("do you like your current employment (yes/no) ")
        print("do you like your current employment (yes/no)")
        answer = input("->")
        if answer.lower() == "yes":
         trtl.goto(-200,35)
         trtl.write("consider asking for a raise around 50 percent of people who ask for a raise get one ")
         print("consider asking for a raise around 50 percent of people who ask for a raise get one")
        elif answer.lower() == "no":
         trtl.goto(-200,25)
         trtl.write("consider using another job offer as leverage to get a raise ")
         print("consider using another job offer as leverage to get a raise ")
        







wn.mainloop()