#!/usr/bin/python  
#-*-  coding:GB2312  -*-

from BerverageBase import Beverage,SauceDecorator,SugarDecorator
from Sugar import CaramelSugar,OrignalSugar,FilbertSugar,VanillaSugar,RaspberrySugar,MochaSugar
from Sauce import MochaSauce,CaramelSauce
from Cup import Middle,Big,SuperBig
from Coffee import Latte,Cappuccino,Mocha

if __name__ == "__main__":
    
    cuptypes = {"Middle":Middle, "Big":Big, "Superbig":SuperBig}
    coffeeType = {"Mocha": Mocha(),"Cappuccino":Cappuccino(),"Latte":Latte()}
    condimenttypes = {"Original": OrignalSugar,"Vanilla":VanillaSugar, "Caramel":CaramelSugar, "Filbert":FilbertSugar, "Mocha":MochaSugar,"Raspberry":RaspberrySugar }
    sauceTypes = {"Mocha":MochaSauce,"Caramel":CaramelSauce}
    try:
        print("Welcom,please order your own coffee")
        coffee_type = input("please input the type of coffee（Mocha/Latte/Cappuccino）:")
        coffee = coffeeType[coffee_type]
        temperature = input("please input temperature（Iced/Normal/Hot）：")
        coffee.Settemperature(temperature)
        cuptype = input("please input your cup size（Middle/Big/Superbig）:")          
        coffee = cuptypes[cuptype](coffee)
        milktype = input("please choose the type of milk（Fullcream/Oat/Skim/SoyMilk）:")
        coffee.Setmilk(milktype)
        key = None
        while key not in ["N","n"]:            
            condimenttype = input("please choose your sugar（Original/Vanilla/Caramel/Filbert/Mocha/Raspberry）：")
            quantity = input("please the number of sugar: ")
            coffee = condimenttypes[condimenttype](coffee,int(quantity))
            saucetype = input("please choose your sauce（Mocha/Caramel）：")
            number = input("please the number of sauce: ")
            coffee = sauceTypes[saucetype](coffee,int(number))
            key = input("Do you want to add more sugar or sauce[Y/N]")
        print("Your coffee description：" + temperature+","+milktype+","+ coffee.getDescription() + " the price is￥"+str(coffee.cost()))
    except Exception as e:
        print("Unexpected input, please re-input！")
    finally:
        print("Bye, have a nice day:)")
    