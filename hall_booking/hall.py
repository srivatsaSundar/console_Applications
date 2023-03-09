class hall_booking:
    def __init__(self):
        self.admin={}
        self.user={}
        self.hall={0:{"name":"Ragam hall","capacity":500,"status":"available"},1:{"name":"Veena hall","capacity":300,"status":"available"},2:{"name":"Sangeetha hall","capacity":200,"status":"available"},3:{"name":"Thanam hall","capacity":100,"status":"available"},4:{"name":"Pallavi hall","capacity":50,"status":"available"}}
        self.GDhall={0:{"name":"Legend hall","status":"available"},1:{"name":"Surya hall","status":"available"},2:{"name":"GD hall 1","status":"available"},3:{"name":"GD hall 2","status":"available"}}
        self.interview={0:{"name":"Interview hall 1","status":"available"},1:{"name":"Interview hall 2","status":"available"},2:{"name":"Interview hall 3","status":"available"},3:{"name":"Interview hall 4","status":"available"},4:{"name":"Interview hall 5","status":"available"}}
        self.hall_booking={}
        self.GDhall_booking={}
        self.interview_booking={}
        #self.date={0:"1/3/2023",1:"2/3/2023",2:"3/3/2023",3:"4/3/2023",4:"5/3/2023",5:"6/3/2023",6:"7/3/2023",7:"8/3/2023",8:"9/3/2023",9:"10/3/2023",10:"11/3/2023",11:"12/3/2023",12:"13/3/2023",13:"14/3/2023",14:"15/3/2023",15:"16/3/2023"}
        self.time={0:"FN",1:"AN"}

hall=hall_booking()

def main():
    print("Welcome to Hall Booking System")
    print("1.Admin")
    print("2.User")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        admin(hall)
    elif choice==2:
        user(hall)
    elif choice==3:
        exit()

def admin(hall):
    print("Welcome Admin")
    print("1.Add user")
    print("2.View user")
    print("3.View hall")
    print("4.View hall booking")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_user(hall)
    elif choice==2:
        view_user(hall)
    elif choice==3:
        view_hall(hall)
    elif choice==4:
        view_hall_booking(hall)
    elif choice==5:
        exit()

def user(hall):
    print("Welcome User")
    print("1.View hall")
    print("2.View hall booking")
    print("3.cancel hall booking")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        view_hall(hall)
    elif choice==2:
        view_hall_booking(hall)
    elif choice==3:
        cancel_hall_booking(hall)
    elif choice==4:
        exit()

if __name__=="__main__":
    main()