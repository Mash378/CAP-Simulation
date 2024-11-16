import random
import matplotlib.pyplot as plt

class Player:
    def __init__(self,type,contribution):
        self.type= type  
        self.contribution = contribution

#Simulation
def Simulation():
    #User input
    #people = input("Enter number of people: ")
    #rounds = input("Enter number of rounds: ")
    #people = random.randint(2,10)
    #rounds = random.randint(1,10)
    people = 50
    rounds = 50

    cheaters = random.randint(1,people-1) #Some players are cheaters
    players = []
    for i in range(people-cheaters):
        players.append(Player("Normal",float(1.00/rounds)))
    for i in range(cheaters):
        players.append(Player("Cheater",float(1.00/rounds)))

    Contribution =0
    Cheat = random.randint(0,rounds-1)
    has_cheated = False

    #Game start
    for i in range(rounds):
        for j in range(people):
            if(players[j].type=="Cheater" and Cheat==i):
                Contribution+=0
                continue
            if(has_cheated==False):
                Contribution+=players[j].contribution
            else:
                Contribution+=0
        if(i==Cheat):
            has_cheated=True

    return Cheat, Contribution

#100 Simulations
y_values = []
x_values = []

for i in range(100):
    x,y= Simulation()
    y_values.append(y)
    x_values.append(x)

plt.plot(x_values, y_values,linestyle='-', color='b') 
plt.xlabel('Round cheated on')
plt.ylabel('Total Contribution')

plt.show()