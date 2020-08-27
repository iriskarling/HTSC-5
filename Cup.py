#!/usr/bin/python  
#-*-  coding:GB2312  -*-
from BerverageBase import Beverage,CupDecorator
class Middle(CupDecorator):
    def __init__(self,beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ",Middle cup"

    def cost(self):
        return 0.56 + self.beverage.cost()

class Big(CupDecorator):
    def __init__(self,beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ",Big cup"

    def cost(self):
        return 0.56 + self.beverage.cost()

class SuperBig(CupDecorator):
    def __init__(self,beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ",Superbig cup"

    def cost(self):
        return 0.56 + self.beverage.cost()