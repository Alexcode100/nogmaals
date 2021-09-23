#Alexander den Otter  -  9067410
print('Je gaat proberen mijn voornaam in 10 pogingen te raden!')
iteratie = 1
while iteratie <= 10:
    Naam = input('Gok mijn voornaam: ')
    if Naam == "Alexander":
        print("Goed gedaan je hebt het geraden in: "+str(iteratie)+" keer!")
        break
    else:
        print('Dit is je '+ str(iteratie)+"e gok!")
        iteratie = iteratie + 1


