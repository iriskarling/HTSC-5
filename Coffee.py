#!/usr/bin/python  
#-*-  coding:GB2312  -*-
from BerverageBase import Beverage

class Mocha(Beverage):
    def __init__(self):
        super(Mocha,self).__init__()
        self.description = "Mocha" 

    def getDescription(self):
        return self.description 

    def cost(self):
        return 1.99

class Latte(Beverage):
    def __init__(self):
        super(Latte,self).__init__()
        self.description = 'Latte'

    def getDescription(self):
        return self.description 

    def cost(self):
        return 1.89


class Cappuccino(Beverage):
    def __init__(self):
        super(Cappuccino,self).__init__()
        self.description = 'Cappuccino'


    def getDescription(self):
        return self.description 

    def cost(self):
        return 2.89

