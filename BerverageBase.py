#!/usr/bin/python  
#-*-  coding:GB2312  -*-
class Beverage(object):
    description = "Normal Beverage"

    def getDescription(self):
        return self.description
    def Settemperature(self, temperature):
        self.temperature = temperature
        return self.temperature
    def Setmilk(self,milk):
        self.milk = milk
        return self.milk

    def cost(self):
        pass


class SugarDecorator(Beverage):
    def getDescription(self):
        pass

class SauceDecorator(Beverage):
    def getDescription(self):
        pass

class CupDecorator(Beverage):
    def getDescription(self):
        pass



