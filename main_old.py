import numpy as np
class Card:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Servant(Card):
    kind = "Servant"
    def __init__(self, name, cost):
        super().__init__(name, cost)


    def display(self):
        print("%s is a %s card (cost: %d)" % (self.name, Servant.kind, self.cost))



class Soldier:
    def __init__(self, name, HP, ATK, DEF):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

    def attack(self, enemy) -> None:
        Rules.attack(self, enemy)
        print("%s attack %s" % (self.name, enemy.name))
        print(f"{enemy.name}'s HP: {enemy.HP}")
    
    def display(self):
        print(f"[{self.name}] HP: {self.HP} ATK: {self.ATK} DEF: {self.DEF}")
        
class Player:
    def __init__(self, name="BILLY", HP=30, GOLD=1):
        self.GOLD = GOLD
        self.HP = HP
        self.name = name

    def display(self):
        print("%s's GOLD: %s" % (self.name, self.GOLD))

class BattleField:
    def __init__(self, max_num):
        self.max_num = max_num
        self.battle = [[],[]]
        self.actionQueue = []

    def add(self, what: Soldier, owner: int):
        if len(self.battle[owner]) > self.max_num:
            print("Already full!")
        else:
            self.battle[owner].append(what)

    def remove(self, what: Soldier, owner: int):
        self.battle[owner].remove(what)
    
    def beginBattle(self):
        pass
        # for player_index in range(2):
        #     for _soldier in self.battle[player_index]:
        #         _soldier.cd = 100
        # while(True):
        #     for player_index in range(2):
        #         for _soldier in self.battle[player_index]:
        #             Rules.update_cd(_soldier)
        #             if _soldier.cd < 0:
        #                 _soldier.attack()

    def display(self):
        print("Player 1 has soldiers:")
        for i in range(len(self.battle[0])):
            self.battle[0][i].display()
        print("Player 2 has soldiers:")
        for i in range(len(self.battle[1])):
            self.battle[1][i].display()

class Phase:
    MAX_SOLDIER_NUM = 10
    def __init__(self):
        self.battleField = BattleField(Phase.MAX_SOLDIER_NUM)

    def battlePhase(self):
        pass



class Rules():
    @staticmethod
    def attack(attacker: Soldier, defender: Soldier) :
        defender.HP -= attacker.ATK - defender.DEF

    @staticmethod
    def update_cd(foo: Soldier):
        foo.speed = 1
        foo.cd -= foo.speed

# test
if __name__ == "__main__":
    
    a = Player()
    a.display()
    b = Servant("Gobllin", 1)
    b.display()

    s1 = Soldier("soldier uu", 10, 5, 1)
    s3 = Soldier("soldier kk", 10, 5, 1)
    s2 = Soldier("soldier jj", 10, 2, 1)
    s1.attack(s2)
    print("------------")
    p = Phase()
    p.battleField.add(s1, 0)
    p.battleField.add(s3, 0)
    p.battleField.add(s2, 1)
    p.battleField.display()