# name of student: Alexander den Otter
# number of student: 99067410
# purpose of program: Wisselgeld terug te geven
# function of program: Wisselgeld terug te geven
# structure of program: Dit programma gebruikt een while loop

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

vijfhonderdeurocent = 0
driehonderdeurocent = 0
tweehonderdeurocent = 0
vijftigcent = 0
twintigcent = 0
tiencent = 0
vijfcent = 0
tweecent = 0
eencent = 0

if change > 0: 
  coinValue = 500 
  
  while change > 0 and coinValue > 0: 
    nrCoins = change // coinValue 

    if nrCoins > 0: 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' €!' ) 
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cent did you return? ')) 
      if coinValue == 500:
        vijfhonderdeurocent += nrCoinsReturned
      elif coinValue == 300:
        driehonderdeurocent += nrCoinsReturned
      elif coinValue == 200:
        tweehonderdeurocent += nrCoinsReturned
      elif coinValue == 50:
        vijftigcent += nrCoinsReturned
      elif coinValue == 20:
        twintigcent += nrCoinsReturned
      elif coinValue == 10:
        tiencent += nrCoinsReturned
      elif coinValue == 5:
        vijfcent += nrCoinsReturned
      elif coinValue == 2:
        tweecent += nrCoinsReturned
      else:
        eencent += nrCoinsReturned

      change -= nrCoinsReturned * coinValue 

    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: 
  print('Change not returned: ', str(change) + '€')
  print("Geld terug gegeven")
  print(" -----------------------------------")
  print("|  5 eurocenten          : "+str(vijfhonderdeurocent))
  print("|  3 eurocenten          : "+str(driehonderdeurocent))               
  print("|  2 eurocenten          : "+str(tweehonderdeurocent))   
  print("|  50 centen             : "+str(vijftigcent))    
  print("|  20 centen             : "+str(twintigcent))       
  print("|  10 centen             : "+str(tiencent))         
  print("|  5 centen             : "+str(vijfcent))     
  print("|  2 centen             : "+str(tweecent))           
  print("|  1 centen             : "+str(eencent))           
  print(' -----------------------------------\n')       
else:
  print("Geld terug gegeven")
  print(" -----------------------------------")
  print("|  5 eurocenten          : "+str(vijfhonderdeurocent))
  print("|  3 eurocenten          : "+str(driehonderdeurocent))               
  print("|  2 eurocenten          : "+str(tweehonderdeurocent))   
  print("|  50 centen             : "+str(vijftigcent))    
  print("|  20 centen             : "+str(twintigcent))       
  print("|  10 centen             : "+str(tiencent))         
  print("|  5 centen             : "+str(vijfcent))     
  print("|  2 centen             : "+str(tweecent))           
  print("|  1 centen             : "+str(eencent))           
  print(' -----------------------------------\n')  
  print('Gedaan')