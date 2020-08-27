#!/usr/bin/python  
#-*-  coding:GB2312  -*-
from BerverageBase import Beverage,SauceDecorator

class MochaSauce(SauceDecorator):   
    def __init__(self,beverage,quantity):
        self.beverage = beverage
        self.quantity = quantity

    def getDescription(self):
        return self.beverage.getDescription() + ",MochaSauce x" +str(self.quantity)

    def cost(self):
        return 0.56 * self.quantity + self.beverage.cost()


class CaramelSauce(SauceDecorator):   
    def __init__(self,beverage,quantity):
        self.beverage = beverage
        self.quantity = quantity

    def getDescription(self):
        return self.beverage.getDescription() + ",CaramelSauce x " + str(self.quantity)

    def cost(self):
        return 0.67*self.quantity + self.beverage.cost()