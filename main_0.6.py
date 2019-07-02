__author__ = "S.CHENG"
"""
comments
"""
#libirary block
import time
import random
import numpy as np
import matplotlib.pyplot as plt

#varible block
personNum = 100

personList = []

#class defination block
class person:
	# class person defined to manufact date more convenitent
	index   = 0
	money   = 100
	charact = 0

	def set_money(self, mon):
		self.money = mon

	def set_index(self, ind):
		self.index = ind

	def get_money(self):
		return self.money

	def get_index(self):
		return self.index

	def takeMoney(self):
		self.money = self.money - 1

	def gainMoney(self):
		self.money = self.money + 1

#function defination block
def personInit(personL, personN):
	for i in range(personN):
		personL.append(person())
		personL[i].set_index(i)

def moneyExchange(personL):
	for i in range(len(personL)):
		personL[i].takeMoney()
		personL[np.random.randint(0,len(personL))].gainMoney()

def get_wealth(personL):
	wealth = []
	for i in range(len(personL)):
		wealth.append([personL[i].get_index(), personL[i].get_money()])

	return wealth

def plotFig():
	pass


#main function
def main():
	
	personInit(personList, personNum)

	for i in range(100):
		moneyExchange(personList)

	wealth = get_wealth(personList)

	print(wealth)


if __name__ == '__main__':
	#ensure code is conducted only this is called by system
		main()