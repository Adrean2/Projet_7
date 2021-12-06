import csv
import sys
import timeit
start = timeit.default_timer()


class Action:
    def __init__(self,name,price,profit):
        self.name = name
        self.price = price
        self.profit = profit/100
        self.benefice = self.price * self.profit
        self.market_value = self.price + self.benefice
        self.ratio_prix_benefice = self.market_value/self.benefice


def calculate_profit(liste_actions):

    liste_actions = sorted(liste_actions,key = lambda action : action.ratio_prix_benefice)
    capital = int(sys.argv[2])
    confirmed_actions = []

    for action in liste_actions:
        if capital - action.price >= 0:
            capital -= action.price
            confirmed_actions.append(action)

    return confirmed_actions


def main():

    liste_actions = []

    with open(sys.argv[1],mode ="r") as fh:
        reader = csv.reader(fh,delimiter=",")
        next(reader,None)
        for action in reader:
            name = action[0]
            price = float(action[1])
            profit = float(action[2])
            if price <=0 or profit <=0:
                pass
            else: liste_actions.append(Action(name,price,profit))
                        

    most_profitable_actions = calculate_profit(liste_actions)
    print(f"Coût total:  {sum([action.price for action in most_profitable_actions])}\nBénéfice réalisé : {sum([action.benefice for action in most_profitable_actions])}\nCapital final :  {sum([action.benefice for action in most_profitable_actions]) + int(sys.argv[2])}")
    print([action.name for action in most_profitable_actions])
    stop = timeit.default_timer()
    print("time: ",stop - start)


if __name__ == "__main__":
    main()
