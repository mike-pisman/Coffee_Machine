# Write your code here

class CoffeeMachine:
    def __init__(self, money, water, milk, coffee, cups):
        self.money = money
        self.resources = {"water": water, "milk": milk, "coffee beans": coffee, "disposable cups": cups}
        self.menu()

    def menu(self):
        while True:
            command = input("\nWrite action (buy, fill, take, remaining, exit):\n")
            if command == "exit":
                break
            else:
                eval("self." + command + "()")

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if choice == "back":
            return
        else:
            choice = int(choice) - 1

        # water, milk, coffee, disposable cups, price
        coffee_types = [[250, 0, 16, 1, 4], [350, 75, 20, 1, 7], [200, 100, 12, 1, 6]]
        drink = coffee_types[choice]

        for i, resource in enumerate(self.resources):
            if self.resources[resource] >= drink[i]:
                self.resources[resource] -= drink[i]
            else:
                print("Sorry, not enough", resource)
                return

        self.money += drink[4]
        print("I have enough resources, making you a coffee!")

    def fill(self):
        self.resources["water"] += int(input("Write how many ml of water do you want to add:"))
        self.resources["milk"] += int(input("Write how many ml of milk do you want to add:"))
        self.resources["coffee beans"] += int(input("Write how many grams of coffee beans do you want to add:"))
        self.resources["disposable cups"] += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def remaining(self):
        print("The coffee machine has:")
        for i in self.resources:
            print("{} of {}".format(self.resources[i], i))

        print("{} of money".format(self.money))


def main():
    machine = CoffeeMachine(550, 400, 540, 120, 9)


if __name__ == "__main__":
    main()
