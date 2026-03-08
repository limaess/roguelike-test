import pygame as pg
import random as r
from rogueliketestClasses import *

# this is actually spells AND items i js didnt know how to name this

def regiItemEffect(item_name, effect_func):
    itemEffects[item_name] = effect_func

#------------------------------------- potions or any usable item

def healEffect(player, amount, playerInv, whichItem):
    if whichItem in playerInv:
        player.health += amount
    else:
        print('how the fuck did you get this message')

def attackPotionEffect(player, amount, playerInv, whichItem):
    if whichItem in playerInv:
        player.damage += amount
    else:
        print('how the fuck did you get this message')

#------------------------------------- passives

def damageUp(player, amount):
    player.damage += amount

def constUp(player, amount):
    player.constitution += amount

def speedUp(player,amount):
    player.speed += amount

#------------------------------------- spells  

 
