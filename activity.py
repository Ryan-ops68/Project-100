class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def checkbalance(self):
        print("your balance is 100,000")
    def withdrawl(self, amount):
        new_amount = 100000 - amount
        print("you have withdrawn " + str(amount)+ " Your remaining blance is " +str (new_amount))
def main():
    card_number = input("enter your card number:")
    pin_number = input("Enter your pin number:")
    newUser = Atm(card_number, pin_number)
    print("Choose your activity")
    print("1.balance inquiry 2.withdrawl")
    activity = int(input("enter the activity number:"))
    if activity == 1:
        newUser.checkbalance()
    elif activity == 2:
        amount = int(input("enter the amount to be withdrawn:"))
        newUser.withdrawl(amount)
    else:
        print("enter a valid number")
if __name__ == "__main__":
    main()