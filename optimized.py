import csv
from pathlib import Path
import itertools
absolute_path = Path(__file__).absolute().parent


class Action:
    def __init__(self,name,price,profit):
        self.name = name
        self.price = price
        self.profit = profit/100
        self.benefice_brut = self.price * self.profit
        self.profit_percentage = (self.benefice_brut/self.price)*100
        self.benefice_net = self.price + self.benefice_brut


# liste d'actions
# 
# 
# 
# trouver les listes d'actions qui utilisent 500€ max
# comment trouver les 500 sans bruteforce toutes les possibilités ? 
# 
# 
# 
# 
# 

def sum_action_price(liste,attr):
    desired_liste = []
    for action in liste:
        desired_liste.append(action.attr)
        action_price = sum([action.benefice_brut for action in liste])
        print(action_price)

def calculate_profit(liste_actions):

    argent = 500
    sorted_profit = sorted(liste_actions, key = lambda action : action.profit, reverse=True)
    # Récupère les 5 meilleurs profits
    four_best_profit = sorted_profit[0:4]
    # "dépense" l'argent des actions
    argent -= sum([action.price for action in four_best_profit])
    [liste_actions.remove(action) for action in four_best_profit]


    l_total = []
    for i in range(0,(len(liste_actions)-len(four_best_profit))):
        for x in itertools.combinations(list(liste_actions),i):
            price_list = [action.price for action in x]
            s = sum(price_list)
            if s == argent:
                l_total.append(x)
    
    best_benefice = []
    true_profit = 0
    # trie par benefice brut
    for l_actions in l_total:
        profit = sum([action.benefice_brut for action in l_actions])
        if profit > true_profit:
            true_profit = profit
            # attribue la liste qui a le meilleur benefice
            best_benefice = l_actions

    big_winner = list(best_benefice) + four_best_profit
    return big_winner

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

    winner = calculate_profit(l_actions)
    sum_action_price(winner)

main()