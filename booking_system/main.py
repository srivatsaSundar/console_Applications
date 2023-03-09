import sys
from book_tickets import book_tickets,availability,cancel_tickets,print_tickets
class ticket_booking:
    def __init__(self):
        self.place={'Cbe':0,'Tirupur':0,'Erode':0,'Salem':0,'Chennai':0}
        self.available_places={0:'Cbe',1:'Tirupur',2:'Erode',3:'Salem',4:'Chennai'}
        self.stations = [0,0,0,0,0]
        self.no_waiting=[0,0,0,0,0]
        self.id={}
        self.waiting_list={}
ticket=ticket_booking()

def user_interface(ticket):
    while True:
        print("Welcome to train ticket booking system from CBE to Chennai")
        print("Select the options\n 1.Book the tickets \n 2.Availability of the tickets \n 3.Cancel the tickets \n 4.Print the Tickets \n 5.Exit")
        system=int(input())
        if(system==1):
            print("Enter the username")
            username=input()
            print("Enter the password")
            password=input()
            if(username=='user' and password=='user'):
                book_tickets(ticket)
        elif(system==2):
                availability(ticket)
        elif(system==3):
                cancel_tickets(ticket)
        elif(system==4):
                print_tickets(ticket)
        elif(system==5):
                print('Exit')
                return main()

def admin_interface(ticket):
    while True:
        print("Wecolme to train ticket booking system from CBE to Chennai")
        print("Admin username")
        username=input()
        print("Admin password")
        password=input()
        if(username=='admin' and password=='admin'):
             print("Select the options\n 1.No of waiting list \n 2.No of tickets booked \n 3.Exit")
             system=int(input())
             if(system==1):
                print(ticket.no_waiting)
             elif(system==2):
                print(ticket.stations)
             elif(system==3):
                print('Exit')
                return main()
        else:
            print("Invalid username and password")
        return main()
    
def main():
    while True:
        print("Select the options\n 1.User \n 2.Admin \n 3.Exit")
        user=int(input())
        if(user==1):
            user_interface(ticket)
        elif(user==2):
            admin_interface(ticket)
        elif(user==3):
            print("Exit")
            sys.exit()
        else:
            print("Invalid option")
        return

if __name__ == '__main__':
    main()