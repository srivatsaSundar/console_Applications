import random
def seat(place,destination,tickets):
    for i in range(place,destination):
        if(tickets.stations[i]==10):
            return 0
    min=float('inf')
    for i in range(place,destination):
        ava=10-tickets.stations[i]
        min=ava
    return min

def book_tickets(tickets):
    print("Enter the number of ticket you need to book:")
    n=int(input())
    print("--------------------------------------------")
    print("The available boarding places are : 1.Cbe , 2.Tirupur , 3.Erode , 4.Salem")
    print("--------------------------------------------")
    print("Enter the boarding place you need to book the ticket:")
    place=int(input())-1
    print("--------------------------------------------")
    print("The available destination places are :")
    for i in range(place+1,5):
        print(i+1,tickets.available_places[i])
    print("--------------------------------------------")
    print("Enter the destination place you need to book the ticket:")
    destination=int(input())-1
    if(place==destination):
        print("The boarding place and destination place are same")
    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            if(seat(place,destination,tickets)==0):
                print("There is no sufficient tickets in the boarding place")
                wait=random.randint(1000,9999)
                tickets.waiting_list[wait]=[place,destination,n,wait]
                #tickets.available_places[place]+=10
                print("-------------------------------------------------------")
                print("The waiting ticket id is ",wait)
                print("The number of ticket booked is ",n)
                print("The boarding place is",tickets.available_places[place])
                print("The destination place is",tickets.available_places[destination])
                print("The booking is full now.Your ticket are booked in waiting list")
                print("-------------------------------------------------------")
            else:
                    # tn=random.randint(1000,9999)
                    # ticket.id[tn]=[place,destination,n,tn]
                    if(seat(place,destination,tickets)>=n):
                        tn=random.randint(1000,9999)
                        tickets.id[tn]=[place,destination,n,tn]
                        for i in range(place,destination):
                            tickets.stations[i]+=n
                        print("-------------------------------------------------------")
                        print("The train tickets are successfully booked for ",n," persons")
                        print("The ticket id is ",tn)
                        print("The boarding place is ",tickets.available_places[place])
                        print("The destination place is ",tickets.available_places[destination])
                        print("-------------------------------------------------------")
                        #print("The number of tickets booked is ",n)
                    # else:
                    #     print("The number of tickets are not available")
                    #     print("-------------------------------------------------------")
                    #     wait=random.randint(1000,9999)
                    #     tickets.waiting_list[wait]=[place,destination,n,wait]
                    #     #tickets.available_places[place]+=10
                    #     print("-------------------------------------------------------")
                    #     print("The waiting ticket id is ",wait)
                    #     print("The number of ticket booked is ",n)
                    #     print("The boarding place is",tickets.available_places[place])
                    #     print("The destination place is",tickets.available_places[destination])
                    #     print("The booking is full now.Your ticket are booked in waiting list")
                    #     print("-------------------------------------------------------")
                        
def cancel_tickets(tickets):
    print("Select the options\n 1.Cancel the tickets \n 2.Cancel the tickets in waiting list")
    id=int(input())
    if(id==1):
        print("Enter the tickets's id you need to cancel the ticket:")
        id=int(input())
        if(id in tickets.id.keys()):
            print("-------------------------------------------------------")
            print("The tickets's id is ",tickets.id[id][3])
            print("The boarding place is ",tickets.available_places[tickets.id[id][0]])
            print("The destination place is ",tickets.available_places[tickets.id[id][1]])
            print("The number of ticket booked is ",tickets.id[id][2])
            print("Do you want to cancel the ticket? ()(yes/no)")
            cancel=input()
            if(cancel=="yes"):
                for i in range(tickets.id[id][0],tickets.id[id][1]):
                    tickets.stations[i]-=tickets.id[id][2]
                del tickets.id[id]
                print("The tickets are successfully cancelled")
                print("-------------------------------------------------------")
                if (tickets.waiting_list != {}):
                    for i in tickets.waiting_list.keys():
                        if(seat(tickets.waiting_list[i][0],tickets.waiting_list[i][1],tickets)>=tickets.waiting_list[i][2]):
                            for j in range(tickets.waiting_list[i][0],tickets.waiting_list[i][1]):
                                tickets.stations[j]+=tickets.waiting_list[i][2]
                                tickets.id[i]=[tickets.waiting_list[i][0],tickets.waiting_list[i][1],tickets.waiting_list[i][2],i]
                            del tickets.waiting_list[i]
                            print("The tickets are successfully booked from waiting list to the tickets")
                            print("The ticket id is ",i)
                            # print("The boarding place is ",tickets.available_places[tickets.id[i][0]])
                            # print("The destination place is ",tickets.available_places[tickets.id[i][1]])
                            # print("The number of ticket booked is ",tickets.id[i][2])
                            print("-------------------------------------------------------")
                            break
                        
                        
            else:
                print("The tickets are not cancelled")
                print("-------------------------------------------------------")
        else:
            print("The tickets's id is not available")
    elif(id==2):
        print("Enter the waiting list tickets's id you need to cancel the ticket:")
        id=int(input())
        if(id in tickets.waiting_list[id]):
            print("-------------------------------------------------------")
            print("The waiting list tickets's id is ",tickets.waiting_list[id][3])
            print("The waiting list tickets boarding place is ",tickets.waiting_list[id][0])
            print("The waiting list tickets destination place is ",tickets.waiting_list[id][1])
            print("The number of waiting list ticket booked is ",tickets.waiting_list[id][2])
            print("Do you want to cancel the ticket? ()(yes/no)")
            cancel=input()
            if(cancel=="yes"):
                del tickets.waiting_list[id]
                print("The waiting list tickets are successfully cancelled")
                print("-------------------------------------------------------")
            else:
                print("The tickets are not cancelled")
                print("-------------------------------------------------------")
        else:
            print("The tickets's id is not available")

def print_tickets(tickets):
    print("Enter the tickets's id you need to print the ticket:")
    # print(tickets.id)
    id=int(input())
    if(id in tickets.id.keys()):
        print("-------------------------------------------------------")
        print("The tickets's id is",tickets.id[id][3])
        print("The boarding place is ",tickets.available_places[tickets.id[id][0]])
        print("The destination place is ",tickets.available_places[tickets.id[id][1]])
        print("The number of ticket booked is ",tickets.id[id][2])
        print("-------------------------------------------------------")
    else:
        print("The tickets's id is not available")

def availability(tickets):
    print("--------------------------------------------")
    print("The available boarding places are : 1.Cbe , 2.Tirupur , 3.Erode , 4.Salem")
    print("--------------------------------------------")
    print("Enter the boarding place you need to check the availability:")
    place=int(input())-1
    print("--------------------------------------------")
    print("The available destination places are :") 
    for i in range(place+1,5):
        print(i+1,tickets.available_places[i])
    print("--------------------------------------------")
    print("Enter the destination place you need to check the availability:")
    destination=int(input())-1
    if(place==destination):
        print("The boarding place and destination place are same")
    else:
        if(tickets.stations[place]<tickets.stations[destination]):
            print("-------------------------------------------------------")
            print("The tickets are available in the boarding place")
            print("-------------------------------------------------------")
        else:
            print("-------------------------------------------------------")
            print("The tickets are not available in the boarding place")
            print("-------------------------------------------------------")