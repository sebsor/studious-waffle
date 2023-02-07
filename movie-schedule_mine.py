movies = {
    'Spider-man' : 'Onsdag | 21:30 | Salong 1 ',
    'Bladerunner' : 'Fredag | 22:00 | Salong 1',
    'My little pony' : 'Tisdag | 18:00 | Salong 3',
    'Star Wars' : 'Lördag | 19:00 | Salong 2'
}

customerAgreement = input('Ska du se på bio?\n')

if customerAgreement.lower() == "ja" :
    print('I så fall visar vi den här veckan följande filmer' + ':' ' Spider-man, Bladerunner, My little pony och Star Wars.')
else :
    print("Då får vi tacka för denna gången. Ha en fortsatt trevlig dag!")



if customerAgreement.lower() == "ja" :
    customerFilmChoice = input('Skriv in filmen du vill se för att se dess visningstid.\n')
else :
    print()

if customerFilmChoice.lower() == 'spider-man' :
    print(movies.get('Spider-man')) 
elif customerFilmChoice.lower() == 'bladerunner' :
    print(movies.get('Bladerunner'))  
elif customerFilmChoice.lower() == 'my little pony' :
    print(movies.get('My little pony'))
elif customerFilmChoice.lower() == 'star wars' :
    print(movies.get('Star Wars'))
else :
    print('Vi hittade inte filmen du sökte på. Var god försök igen.')