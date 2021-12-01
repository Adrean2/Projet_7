import csv
from pathlib import Path
import itertools

absolute_path = Path(__file__).absolute().parent

class Action:
    def __init__(self,name,price,profit):
        self.name = name
        self.price = price
        self.profit = profit/100    
        self.total_profit = self.price*self.profit    
        
def find_good_ones(liste_actions):
    l_total = []
    for i in range(0,len(liste_actions)):
        for x in itertools.combinations(list(liste_actions),i):
            price_list = [action.price for action in x]
            s = sum(price_list)
            if s == 500:
                l_total.append(x)
    return l_total

def find_best_one(good_ones_list):
    best_one = []
    good_ones = find_good_ones(good_ones_list)
    for l in good_ones:
        profit = sum([action.total_profit for action in l])
        if profit > sum([action.total_profit for action in best_one]):
            best_one = l
    return best_one

def main():

    # l short for liste
    l_actions = []

    with open(absolute_path/"dataset_bruteforce.csv",mode ="r") as Actions:
        reader = csv.reader(Actions,delimiter=";")
        for action in reader:
            name = action[0]
            price = int(action[1])
            profit = int(action[2].strip("%"))
            l_actions.append(Action(name,price,profit))

    best_one = find_best_one(l_actions)
    profit = [action.profit*action.price for action in best_one]
    print(sum(profit))
 

main()


#  iterable = toutes les combinaisons actions qui utilisent 
#  (iterable, maximum_spent)


# itérer sur toutes les actions
# avec une limite de 500€ dépensés
# result = itertools.combinations(actions_list)


# bon résultat = 98.8
# Chercher bruteforce
# Itertools
# Attention aux 500€ MAXIMUM
