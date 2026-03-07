import pygame as pg
import random as r
from rogueliketestClasses import *

# this is actually spells AND items i js didnt know how to name this

def regiItemEffect(item_name, effect_func):
    itemEffects[item_name] = effect_func

#------------------------------------- potions or any usable item

def healEffect(player, target):
    pass

def attackPotionEffect(player, target):
    pass

#------------------------------------- passives

def damageUp(player, amount):
    player.damage += amount

def constUp(player, amount):
    player.constitution += amount

def speedUp(player,amount):
    player.speed += amount

#------------------------------------- spells   
