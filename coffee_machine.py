# Mikhail Pisman
# Coffee Machine
# https://github.com/mike-pisman/Coffee_Machine


# Class Coffe Machine
class CoffeeMachine:
    # Constructor
    def __init__(self, money, water, milk, coffee, cups):
        self.money = money  # Money
        # Resources needed for making coffee
        self.resources = {"water": water, "milk": milk, "coffee beans": coffee, "disposable cups": cups}
        self.menu()

    # Menu function
    def menu(self):
        while True:
            command = input("\nWrite action (buy, fill, take, remaining, exit):\n")
            # Availeble commands: buy, fill, take, remaining, exit
            if command == "exit":
                break
            else:
                eval("self." + command + "()") #

    # Function to make coffee
    def buy(self):
        # Ask for type of drink 1 - espresso, 2 - latte, 3 - cappuccino
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if choice == "back": # Stop the process if user enters "back"
            return
        else:
            choice = int(choice) - 1

        # list of resource for each drink  espresso, latte, cappuccino
        # water, milk, coffee, disposable cups, price
        coffee_types = [[250, 0, 16, 1, 4], [350, 75, 20, 1, 7], [200, 100, 12, 1, 6]]
        drink = coffee_types[choice]

        # Check if thre is enough resources to make a drink
        for i, resource in enumerate(self.resources):
            if self.resources[resource] < drink[i]:
                # print which resource is missing
                print("Sorry, not enough", resource)
                return

        # If there is enough resource, substract them
        for i, resource in enumerate(self.resources):
            self.resources[resource] -= drink[i]

        # Add money
        self.money += drink[4]
        print("I have enough resources, making you a coffee!")

    # Function to refill Resources
    def fill(self):
        self.resources["water"] += int(input("Write how many ml of water do you want to add:"))
        self.resources["milk"] += int(input("Write how many ml of milk do you want to add:"))
        self.resources["coffee beans"] += int(input("Write how many grams of coffee beans do you want to add:"))
        self.resources["disposable cups"] += int(input("Write how many disposable cups of coffee do you want to add:"))

    # Function to take out all the money
    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0  # Amount in the regester after is zero

    # Show remaining amount of resources and money
    def remaining(self):
        print("The coffee machine has:")
        for i in self.resources:
            print("{} of {}".format(self.resources[i], i))

        print("{} of money".format(self.money))

# Main funciton
def main():
    machine = CoffeeMachine(550, 400, 540, 120, 9)


if __name__ == "__main__":
    main()
