""" The Challenge
Author: Adopted from Ms. Alysson's code
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

totalbill = input('How much is your total bill? ')

payment = input('How much is your payment? ')

change = float(payment) - float(totalbill)

print('Hi! Your change is {0:.2f}'.format(change))
