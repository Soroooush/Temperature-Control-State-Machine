state_number = 1
cooler_state_number = 0
heater_state_number = 0

while True:
    if state_number == 1 :
      tempreture = int(input("input tempreture?"))
      if  tempreture < 25 :
          state_number = 2
      elif tempreture < 15:
          state_number = 3
      else : print("Heater and Cooler are off")

    elif state_number == 2:
        print("Heater is off")
        print("Cooler is on")
        cooler_state_number = 1
        while cooler_state_number !=0 :
          if cooler_state_number == 1 :
            print("CRS = 4 RPS")
            tempre = int(input("state 1 tempreture?"))
            if tempre > 40 :
                 cooler_state_number = 2
            elif tempre < 25 :
                cooler_state_number = 0
          elif cooler_state_number == 2:
              print("CRS = 6 RPS")
              int(input("state 2 tempreture?"))
              if tempre < 35 :
                  cooler_state_number = 1
              elif tempre > 45 :
                  state_number = 3
          elif cooler_state_number == 3 :
              print("CRS = 8 RPS")
              int(input("state 3 tempreture?"))
              if tempre < 40 :
                  cooler_state_number = 2

    elif state_number == 3 :
        print("Heater is on")
        print("Cooler is off")
        heater_state_number = 1
        while heater_state_number !=0 :
          if heater_state_number == 1 :
              print("Low mode has been activated!!")
              temp = int(input("state 1 tempreture?"))
              if temp < 10 :
                  heater_state_number = 2
              elif temp > 30 :
                  heater_state_number = 0
          elif heater_state_number == 2 :
              print("High mode has been activated!!")
              if temp > 15 :
                  heater_state_number = 1



print(f"Current state number is {state_number} .")
print(f"Current cooler state number is {cooler_state_number}.")
print(f"Current heater state number is {heater_state_number}")









