import pygame as pg
import random as r

    # def applyEffect(self, player, target=None):
    #     if self.name in itemEffects:
    #         itemEffects[self.name](player, target)
# saving for later


waveTypes = ['fight', 'shop']
class WaveHandling():
    def __init__(self,whichWave,waveBuffs):
        self.whichWave = whichWave

        self.waveBuffs = waveBuffs

        self.currentWaveType = waveTypes[0]
        self.buffApplied = False

    def enemyBuffEachWave(self, enemy):
        if not self.buff_applied:
            whichBuff = [enemy.damage, enemy.constitution, enemy.speed]
            buffIndex = r.choice(range(len(whichBuff)))
            if buffIndex == 0:
                enemy.damage += self.waveBuffs
            elif buffIndex == 1:
                enemy.constitution += self.waveBuffs
            else:
                enemy.speed += self.waveBuffs
            self.buff_applied = True
        # this code is so embarassing because of a syntax error

    def endWave(self):
        if not self.currentWaveType == 'shop':
            self.whichWave += 1
        waveTypes.reverse()
        self.currentWaveType = waveTypes[0]
        self.waveBuffs += (self.whichWave // 5)

waveHandler = WaveHandling(1, 0)

turnOrder = []
class TurnHandling():
    def __init__(self, whosTurn: int, whichRound, exhaustion):
        self.whosTurn = whosTurn
        self.whichRound = whichRound
        self.exhaustion = exhaustion

        self.turnThingIdk = turnOrder[whosTurn]

    def endTurn(self):
        pass

    def endRound(self):
        whosTurn += 1
        if whosTurn == 5:
            whosTurn = 0

    def turnOrderThingie(self):
        pass

# turnHandler = TurnHandling()

class Inventory():
    def __init__(self):
        pass

inventory = []

class PlayerCurrencyStats():
    def __init__(self, money,shopKarma):
        self.money = money
        self.shopKarma = shopKarma

    def buyThing(self,thing,amount,player):
        if not thing.isDevil:
            self.money -= (amount - self.shopKarma)
            inventory.append(thing)
        else:
            player.health -= (amount + self.shopKarma)
            self.shopKarma -= (amount // 5)
            inventory.append(thing)
    def sellThing(self,thing):
        if thing in inventory:
            self.money += (thing.price + self.shopKarma)
            inventory.remove(thing)
        else:
            print('this message wont appear soon because i will change this')

itemEffects = {}

class Passives():
    def __init__(self, description,name,amount, passiveFunc):
        self.description = description
        self.name = name
        self.amount = amount
        
        self.passiveFunc = passiveFunc

    def applyEffect(self, player, target=None):
        if self.name in itemEffects:
            itemEffects[self.name](player, target)

class Consumables():
    def __init__(self, description,name,amount, itemFunc):
        self.description = description
        self.name = name
        self.amount = amount

        self.itemFunc = itemFunc

    def applyEffect(self, player, target=None):
        if self.name in itemEffects:
            itemEffects[self.name](player, target)

class Spells():
    def __init__(self, description,name,amount, spellFunc):
        self.description = description
        self.name = name
        self.amount = amount

        self.spellFunc = spellFunc

    def applyEffect(self, player, target=None):
        if self.name in itemEffects:
            itemEffects[self.name](player, target)

class Player():
    def __init__(self,constitution, health,damage,speed, playerClass, effectOnSelf):
        self.constitution = constitution
        self.health = health
        self.damage = damage
        self.speed = speed

        self.maxHealth = constitution * 4

        self.isDamagingSomeone = False
        
        self.playerClass = playerClass
        
        self.effectOnSelf = effectOnSelf

class Enemy():
    def __init__(self, waveBuffs: int):
        super().__init__(Player)
    

print(waveHandler.currentWaveType)
waveHandler.endWave()
print(waveHandler.currentWaveType)  