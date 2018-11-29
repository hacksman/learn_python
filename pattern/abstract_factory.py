#!/usr/bin/env python 
# coding:utf-8
# @Time :11/29/18 14:47


import random


class PetShop(object):

    def __init__(self, abstract_instance=None):
        self.factory_instance = abstract_instance

    def show_pet(self):
        print("this pet is {}".format(self.factory_instance))
        print("pet need to {}".format(self.factory_instance.speak()))

class Dog:
    def speak(self):
        print("{} to woof".format(__class__.__name__))
        return "woof"

class Cat:
    def speak(self):
        print("{} to miao".format(__class__.__name__))
        return "miao"


def random_choice():
    random_instance = PetShop(random.choice(Dog, Cat)())
    return random_instance.show_pet()

if __name__ == '__main__':
    cat = PetShop(Cat())
    cat.show_pet()
