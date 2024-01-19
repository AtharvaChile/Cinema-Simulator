films={
    "Animal":[3,2],
    "Dunki":[18,5],
    "The Marvals":[15,5],
    "Sam Bahadur":[12,5],
    "Salaar":[9,5]
    }

while True:

    choice = input("What film would you like to watch?:").strip().title()

    if choice in films :
        age = int(input("How old are you?").strip())

        #User age
        if age>=films[choice][0]:

          #checking enough seats
          num_seats =films[choice][1]

          if num_seats >0:
              print("Enjoy the films!!")
              films[choice][1]=films[choice][1]-1
          else:
              print("Sorry, tickets are sold out!")

        else:
            print("You are too young to see that film!!")

    else:
        print("We don't have that film..")
        
    
