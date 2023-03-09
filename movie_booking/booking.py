import random
class movie_booking:
    def __init__(self):
        self.movie_time={}
        self.seat_1={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0}
        self.seat_2={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0}
        self.seat_3={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0}
        self.seat_4={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0}
        self.available_seats={'1':self.seat_1,'2':self.seat_2,'3':self.seat_3,'4':self.seat_4}
        self.movie_time['1']='10:00 AM'
        self.movie_time['2']='12:00 PM'
        self.movie_time['3']='02:00 PM'
        self.movie_time['4']='06:00 PM'
        self.id={}
        self.user={}
        self.movie_name={}
        self.movie_name['1']='Avengers'
        self.movie_name['2']='Spiderman'
        self.movie_name['3']='Ironman'
        self.movie_name['4']='Thor'

    def book_ticket(self):
        print('Select Movie')
        for i in self.movie_name:
            print(i,self.movie_name[i])
        movie=input('Enter movie number')
        print('Select Time')
        for i in self.movie_time:
            print(i,self.movie_time[i])
        time=input('Enter time number')
        print('Select seat')
        for i in self.available_seats[time]:
            print(i,self.available_seats[time][i])
        seat=input('Enter seat number')
        self.available_seats[time][seat]=1
        print('Ticket booked')
        print('Movie:',self.movie_name[movie])
        print('Time:',self.movie_time[time])
        print('Seat:',seat)
        self.id[seat]=random.randint(1000,9999)
        print('ID:',self.id[seat])
        self.user[seat]=input('Enter Name:')


    def cancel_ticket(self):
        print("Enter the time:")
        time = input()
        print("Enter the ticket ID:")
        id = int(input())
        for i in self.id:
            if id == self.id[i]:
                self.available_seats[time][i] = 0
                print("Ticket cancelled")
                del self.id[i]
                break
        
    
    def check_ticket(self):
        print('Select Movie')
        for i in self.movie_name:
            print(i,self.movie_name[i])
        movie=input('Enter movie number')
        print('Select Time')
        for i in self.movie_time:
            print(i,self.movie_time[i])
        time=input('Enter time number')
        print('Select seat')
        for i in self.available_seats[time]:
            print(i,self.available_seats[time][i])
        seat=input('Enter seat number')
        print('Ticket booked')
        print('Movie:',self.movie_name[movie])
        print('Time:',self.movie_time[time])
        print('Seat:',seat)
        print('ID:',self.id[seat])
        print('Name:',self.user[seat])

    def show_available_seats(self):
        print('Select Movie')
        for i in self.movie_name:
            print(i,self.movie_name[i])
        movie=input('Enter movie number')
        print('Select Time')
        for i in self.movie_time:
            print(i,self.movie_time[i])
        time=input('Enter time number')
        print('Available seats')
        for i in self.available_seats[time]:
            print(i,self.available_seats[time][i])

    def show_booked_ticket_user_info(self):
        print('Select Movie')
        for i in self.movie_name:
            print(i,self.movie_name[i])
        movie=input('Enter movie number')
        print('Select Time')
        for i in self.movie_time:
            print(i,self.movie_time[i])
        time=input('Enter time number')
        print('Booked ticket user info')
        for i in self.available_seats[time]:
            if self.available_seats[time][i]==1:
                print(i,self.id[i],self.user[i])

    def exit(self):
        print('Thank you')


# Path: movie_booking\main.py
from booking import movie_booking
def main():
    obj=movie_booking()
    while True:
        print('1. Book Ticket')
        print('2. Cancel Ticket')
        print('3. Check Ticket')
        print('4. Show Available Seats')
        print('5. Show Booked Ticket User Info')
        print('6. Exit')
        choice=input('Enter your choice')
        if choice=='1':
            obj.book_ticket()
        elif choice=='2':
            obj.cancel_ticket()
        elif choice=='3':
            obj.check_ticket()
        elif choice=='4':
            obj.show_available_seats()
        elif choice=='5':
            obj.show_booked_ticket_user_info()
        elif choice=='6':
            obj.exit()
            break
        else:
            print('Invalid choice')

if __name__=='__main__':
    main()
