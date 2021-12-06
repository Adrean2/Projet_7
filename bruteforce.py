import csv
import itertools
import sys
import timeit

start = timeit.default_timer()

class Action:
    def __init__(self,name,price,profit):
        self.name = name
        self.price = price
        self.profit = profit/100    
        self.benefice = self.price*self.profit
        self.market_value = self.benefice + self.price


# Fonction cherchant la liste d'action la plus rentable
def find_best_one(liste_actions):

    most_profitable_liste = []
    for actions_quantity in range(0,len(liste_actions)):
        # Création de toutes les solutions possibles
        for combination in itertools.combinations(list(liste_actions),actions_quantity):
            price_list = [action.price for action in combination]
            s = sum(price_list)
            # Si les solutions ont un coût de 500€ ou moins
            if s <= int(sys.argv[2]):
                # Elles se trient sur leurs benefice
                if sum([action.benefice for action in combination]) > sum([action.benefice for action in most_profitable_liste]):
                    most_profitable_liste = combination

    return most_profitable_liste

def main():

    liste_actions = []
    # Lecture du fichier contenant les actions
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

    best_one = find_best_one(liste_actions)

    # Résultat final
    print("Bénéfice réalisé : ",sum([action.benefice for action in best_one]))
    print("Coût total: ",sum([action.price for action in best_one]))
    print("Capital final : ", sum([action.benefice for action in best_one]) + int(sys.argv[2]))
    print([action.name for action in best_one])

    stop = timeit.default_timer()
    print("time: ",stop - start)
 

if __name__ == "__main__":
    main()
