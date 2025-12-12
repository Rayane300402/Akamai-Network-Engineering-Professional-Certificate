from random import *

def startGame():
    print("The weather is hot and you're broke.")
    print("With only $1 left in your pocket, the only thing you can do")
    print("is start a lemonade stand.")
    answer = input("Interested? (y/n) ")
    answer = answer[0].lower()

    while not (answer == 'y' or answer == 'n'):
        print("It's not a huge decision:")
        print("you either want to start a lemonade stand")
        print("or you don't.")
        answer = input("Interested? (y/n) ")
        answer = answer[0].lower()

    if answer == 'n':
        print("Totally understandable. The small business life")
        print("isn't for everyone.")
        quit = True
    else:
        print("Fantastic! Get out some posterboard and markers")
        print("and get ready to triumph!")
        print()
        quit = False
        print("Press enter to continue...")
        print()
        input()

    return quit

def rules():
    rules = ['Each day you will recieve a forecast.', 'Based on the forecast, decide how much lemonade to make.', 'Weather, Temperature and price affect sales.', 'A heat wave will automatically sell all lemonade on hand.', 'A thunderstorm means no sales at all.']
    print()
    print("The rules are simple:")
    for rule in rules:
        print(rule)
    print()
    print("Press enter to continue...")
    print()
    input()

def newDay():
	global day
	
	forecast = ['heat wave', 'thunderstorm', 'sunny', 'cloudy']
	sunny = randint(1,100)
	if sunny < 100:
		maxCloudy = 100 - sunny
		cloudy = randint(1,maxCloudy)
		maxHeatWave = 100-sunny-cloudy
		if maxHeatWave > 0:
			heatWave = randint(1, maxHeatWave)
		else:
			heatWave = 0
	else:
		cloudy = 0
		heatWave = 0
	thunderstorm = 100-sunny-cloudy-heatWave
	
	weather = choices(forecast, weights=(heatWave, thunderstorm, sunny, cloudy), k=1)
	weather = weather[0]
	lemonadeCost = randint(1,10)
	temperature = randint(50,100)
	
	day += 1
	
	return weather, lemonadeCost, temperature, sunny, cloudy, heatWave, thunderstorm

def forecast(temperature, sunny, cloudy, heatWave, thunderstorm):
    global day

    print()
    print("Day "+str(day)+":")
    print()
    print("The temperature tomorrow is expected to be "+str(temperature)+" degrees.")
    print()
    print("There is a "+str(sunny)+"% chance of it being sunny,")
    print(" a "+str(cloudy)+"% chance of it being cloudy,")
    print(" a "+str(heatWave)+"% chance of a heat wave,")
    print(" a "+str(thunderstorm)+"% chance of a thunderstorm.")
    print()
    print("The cost to make lemonade today is "+str(lemonadeCost)+" cents.")
    print()
    print("Press enter to continue...")
    print()
    input()

def menu():
    print("1: Sell Lemonade")
    print("2: Make Lemonade")
    print("3: Close for the day")
    print("4: Forecast")
    print("5: Rules")
    print("6: Quit")

    choice = input('What do you want to do? ')
    if choice.isdigit() is True:
        choice = int(choice)

    while choice not in range(1, 7, 1):
        print("I'm sorry, that's not a valid choice.")
        print("Valid choices are 1, 2, 3, 4, 5, ot 6.")
        choice = input('What do you want to do? ')
        if choice.isdigit() is True:
            choice = int(choice)

    return choice

def makeLemonade(lemonadeCost):
    global lemonade
    global cash

    print()
    print("The cost to make lemonade today is "+str(lemonadeCost)+" cents.")
    print("Total cash on hand is: "+str(cash)+" cents.")
    print()

    cups = input('How many cups of lemonade do you want to make? ')

    lemonade = lemonade + int(cups)
    cost = lemonadeCost * int(cups)
    cash = cash - cost

    print("You have made "+cups+" cups of lemonade")
    print("at a total cost of "+str(cost)+" cents.")
    print()
    print("Total cups of lemonade in inventory: "+str(lemonade))
    print("Total cash on hand in now: "+str(cash)+" cents.")
    print()
    print("Press enter to continue...")
    print()
    input()

def sellLemonade(weather, lemonadeCost, temperature):
    global lemonade

    print()
    print("Maximum price: $1 (100 cents)")
    print()
    price = input("How many cents do you want to charge per cup? ")

    if price.isdigit() is True:
        price = int(price)

    while price not in range(1, 101, 1):
        print("I'm sorry, that's not a valid price.")
        print("Valid prices are in cents from 0 to 100.")
        price = input("How many cents do you want to charge per cup? ")
        if price.isdigit() is True:
            price = int(price)

    if weather == 'heatWave':
        demand = lemonade
    elif weather == 'thunderstorm':
        demand = 0
    else:
        cupsSold = randint(1,100)
        # 10% less demand for each 10 cent price increase
        priceFactor = float(100-price)/100
        # 20% less demand for each degree under 100
        heatFactor = 1 - (((100-temperature)*2)/float(100))
        demand = (cupsSold*priceFactor*heatFactor)

    if weather == 'sunny':
        demand = demand * 1.1
    if weather == 'cloudy':
        demand = demand * .9

    demand = int(round(demand, 0))

    if demand < lemonade:
        cupsSold = demand
    elif demand >= lemonade:
        cupsSold = lemonade

    if weather == 'thunderstorm':
        print("Unfortunately, a thunderstorm kept you closed!")
    elif weather == 'heatwave':
        print("You have sold out thanks to a heat wave!")
    elif lemonade == 0:
        print("You had 0 cups in inventory! No loss, no gain.")
    elif cupsSold > lemonade:
        print("You had "+str(lemonade)+" cups in inventory.")
        print("You sold out!")
        print()
        print("But there was demand for "+str(demand)+" cups.")
        print("Next time you might want to have more inventory on hand.")

    elif cupsSold == lemonade:
        print("You had "+str(lemonade)+" cups in inventory.")
        print("There was demand for "+str(demand)+" cups.")
        print()
        print("You sold out!")
        print()
        print("Clearly you have a great mind for business!")
    elif cupsSold < lemonade:
        print("You had "+str(lemonade)+" cups in inventory.")
        print("There was demand for "+str(demand)+" cups.")
        print()
        print("Not a great sales day, but there's always tomorrow.")

    calculateProfits(cupsSold, demand, price)

def calculateProfits(cupsSold, demand, price):
    global cash
    global lemonade

    if lemonade > 0:
        profit = round(cupsSold * price, 0)
        cash = cash + profit
        lemonade = lemonade - cupsSold
        print()
        print("You sold "+str(cupsSold)+" cups of lemonade.")
        print("Your total profit was "+str(profit)+" cents.")
        print()

    print("Total cash on hand is: "+str(cash)+" cents.")
    print()
    print("Press enter to continue...")
    print()
    input()

quit = startGame()

if quit is False:
    rules()

day = 0
cash = 100
lemonade = 0

while quit is False:
    wait = False
    weather, lemonadeCost, temperature, sunny, cloudy, heatWave, thunderstorm = newDay()
    forecast(temperature, sunny, cloudy, heatWave, thunderstorm)
    choice = menu()
    while choice > 1:
        if choice == 6:
            quit = True
            break
        elif choice == 5:
            rules()
            choice = menu()
            continue
        elif choice == 4:
            forecast(temperature, sunny, cloudy, heatWave, thunderstorm)
            choice = menu()
            continue
        elif choice == 3:
            wait = True
            break
        elif choice == 2:
            makeLemonade(lemonadeCost)
            choice = menu()
            continue
    if quit is True:
        break
    elif wait is True:
        continue
    else:
        sellLemonade(weather, lemonadeCost, temperature)

totalProfit = cash - 100
if totalProfit > 0:
    print("Wow, you increased your net worth by "+str(totalProfit))
    print("You're well on your way to being rich!")
    print("If you're ever broke again, you can always sell lemonade!")
elif totalProfit == 0:
    print("It ends where it started. You still have $1. No harm done.")
elif totalProfit < 0:
    print("Maybe sales is not your thing.")
    print("You lost "+str(totalProfit * -1)+" cents.")
    print("You should probably get looking for a job.")
    print("It's going to be a long road to paying back your parents.")
    
print()
print("Goodbye!")