#!/usr/bin/python  
#-*-  coding:GB2312  -*-
from BerverageBase import Beverage,SugarDecorator
class OrignalSugar(SugarDecorator):
    
    def __init__(self,beverage,quantity):
        self.beverage = beverage
        self.quantity = quantity

    def getDescription(self):
        return self.beverage.getDescription() + ",OrignalSugar x" +  str(self.quantity)
    def cost(self):
        return 0.33*self.quantity+ self.beverage.cost()

class VanillaSugar(SugarDecorator):   
    def __init__(self,beverage,quantity):
        self.beverage = beverage
        self.quantity = quantity

    def getDescription(self):
        return self.beverage.getDescription() + ",VanillaSugar x" +  str(self.quantity)
    def cost(self):
        return 0.33*self.quantity + self.beverage.cost()

class FilbertSugar(SugarDecorator):   
    def __init__(self,beverage,quantity):
        self.beverage = beverage
        self.quantity = quantity

    def getDescription(self):
        return self.beverage.getDescription() + ",FilbertSugar x" +  str(self.quantity)
    def cost(self):
        return 0.33*self.quantity + self.beverage.cost()


class CaramelSugar(SugarDecorator):   
    def __init__(self,beverage,quantity):
        self.beverage = beverage
        self.quantity = quantity

    def getDescription(self):
        return self.beverage.getDescription() + ",CaramelSugar x" +  str(self.quantity)

    def cost(self):
        return 0.33*self.quantity+ self.beverage.cost()

class RaspberrySugar(SugarDecorator):   
    def __init__(self,beverage,quantity):
        self.beverage = beverage
        self.quantity = quantity

    def getDescription(self):
        return self.beverage.getDescription() + ",RaspberrySugar x" + str(self.quantity)
    def cost(self):
        return 0.33 *self.quantity + self.beverage.cost()

class MochaSugar(SugarDecorator):   
    def __init__(self,beverage,quantity):
        self.beverage = beverage
        self.quantity = quantity

    def getDescription(self):
        return self.beverage.getDescription() + ",MochaSugar x" +  str(self.quantity)
    def cost(self):
        return 0.33*self.quantity + self.beverage.cost()