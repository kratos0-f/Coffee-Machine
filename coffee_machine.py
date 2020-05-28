def condition(water, milk, coffee, cups, money):
    print('The coffee machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(coffee, 'of coffee beans')
    print(cups, 'of disposable cups')
    print(money, 'of money')


class CoffeeMaker():
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
machine = CoffeeMaker()

while True:
    action = input('Write action (buy, fill, take, remaining, exit):')
    if action == 'buy':
        coffee_want = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if coffee_want == '1' and machine.water >= 250 and machine.coffee >= 16 and machine.cups >= 1:
            machine.water -= 250
            machine.coffee -= 16
            machine.cups -= 1
            machine.money += 4
        elif coffee_want == '2' and machine.water >= 350 and machine.milk >= 75 and machine.coffee >= 20 and machine.cups >= 1:
            machine.water -= 350
            machine.milk -= 75
            machine.coffee -= 20
            machine.cups -= 1
            machine.money += 7
        elif coffee_want == '3' and machine.water >= 200 and machine.milk >= 100 and machine.coffee >= 12 and machine.cups >= 1:
            machine.water -= 200
            machine.milk -= 100
            machine.coffee -= 12
            machine.cups -= 1
            machine.money += 6
        elif coffee_want == 'back':
            continue
        else:
            print('I have enough resources, making you a coffee!')
        
        
    elif action == 'fill':
        machine.water += int(input('Write how many ml of water do you want to add:'))
        machine.milk += int(input('Write how many ml of milk do you want to add:'))
        machine.coffee += int(input('Write how many grams of coffee beans do you want to add:'))
        machine.cups += int(input('Write how many disposable cups of coffee do you want to add:'))
    elif action == 'take':
        print('I gave you $' + str(machine.money))
        machine.money = 0
    elif action == 'remaining':
        condition(machine.water, machine.milk, machine.coffee, machine.cups, machine.money)
    elif action == 'exit':
        break
    