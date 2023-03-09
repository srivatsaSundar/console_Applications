import sys
def admin(atm):

    print("enter the password :")
    pas=int(input())
    if(pas==atm.password):
        print("Entered password is right")
        print("Select any one option\n  1.Load amount\n  2.Balance in ATM \n  3.Exit")
        admin_option=int(input())
        
        if(admin_option==1):
             load_amount(atm)
        elif(admin_option==2):
            balance(atm)
        elif(admin_option==3):
            print('Exit')
            sys.exit()
        else:
            print("Invalid input")
            sys.exit()
    else:
        print("The password is not correct")
        sys.exit()
        
def load_amount(atm):
            notes_2000=int(input("Enter the number of 2000 rupees notes to be loaded in ATM: "))
            notes_500=int(input("Enter the number of 500 rupees notes to be loaded in ATM: "))
            notes_200=int(input("Enter the number of 200 rupees notes to be loaded in ATM: "))
            notes_100=int(input("Enter the number of 100 rupees notes to be loaded in ATM: "))

            if(atm.notes[2000]+notes_2000>=100):
                print("The notes loaded can be only 100, so remove ",notes_2000-100,"extra notes")
                
            elif(atm.notes[500]+notes_500>=100):
                print("The notes loaded can be only 100, so remove ",notes_500-100,"extra notes")
               
            elif(atm.notes[200]+notes_200>=100):
                print("The notes loaded can be only 100, so remove ",notes_200-100,"extra notes")
                
            elif(atm.notes[100]+notes_100>=100):
                print("The notes loaded can be only 100, so remove ",notes_100-100,"extra notes")
                
            else:
                atm.notes[2000]+=notes_2000
                atm.notes[500]+=notes_500
                atm.notes[200]+=notes_200
                atm.notes[100]+=notes_100
                #print(atm.notes)
                print("The amount loaded in the ATM is:")
                print(atm.notes[2000]*2000+atm.notes[500]*500+atm.notes[200]*200+atm.notes[100]*100)
                print("The amount is successfully loaded in the ATM")

def balance(atm):
        atm.balance=atm.notes[2000]*2000+atm.notes[500]*500+atm.notes[200]*200+atm.notes[100]*100
        print("The balance present in the ATM is ",atm.balance)