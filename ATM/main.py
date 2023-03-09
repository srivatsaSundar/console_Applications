from admin import admin
from user import users
import sys

class ATM:
    def __init__(self):
        self.min_balance=500
        self.user=['Sri','Zoro','Luffy']
        self.pin=[0000,4567,4444]
        self.amount=[3000,10000,7500]
        self.password=54321
        self.notes={2000:0,500:0,200:0,100:0}
        self.balance=0
atm = ATM()

while True:
    
    print("Welcome to ATM . The ATM is in service")
    print("Select any one option\n  1.Admin\n  2.User\n  3.Exit")
    atm_option=int(input())
    if(atm_option==1):
        admin(atm)
    elif(atm_option==2):
        users(atm)
    elif(atm_option==3):
        print('Exit')
        sys.exit()
    else:
        print('Invalid input')
        sys.exit()
