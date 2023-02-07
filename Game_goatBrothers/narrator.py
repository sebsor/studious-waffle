import random
from other import randomD20
from ending_images import everyoneDies
# from ending_images import someoneDies
from ending_images import everyoneSurvives

# INTROSCEN
def introScene() :
  print('Berättaren:\n Det var en gång tre bockar, som skulle gå till ängen och äta sig feta. Bockarna Bruse hette de. På vägen till ängen behövde de gå över en bro som korsade en stor fors. De ville också gå till ängen vid helt olika tider på dagen av någon anledning som jag inte kommer gå in på.')

# FIRST BROTHER
def firstBrotherStart() :
  print('Berättaren:\n Först kom den yngsta Bocken Bruse och skulle över bron.')

def firstBrotherCont1() :
  print('Berättaren:\n Tripp, tripp, trapp, lät det i bron.')

def firstBrotherCont4() :
  print('Berättaren:\n Ödet rullar en D20 tärning. Tärningen måste visa 7 eller mer för att yngsta bocken Bruse ska klara sig.')

# Om D20 är över/lika med 7 = vinn, annars förlora
def firstBrotherSurvival() :
  roll = randomD20()
  if roll < 7 :
    print('Berättaren:\n Ödet rullade en ' + str(roll) + '\n Trollet struntade i yngsta bocken Bruses argument och svalde honom hel.')
  else :
    print('Berättaren:\n Ödet rullade en ' + str(roll) + '\n Motvilligt lät trollet den yngsta bocken Bruse pasera över bron, med hoppet om att snart kunna fånga en ännu större måltid.')


# SECOND BROTHER
def secondBrotherStart() :
  print('Berättaren:\n Efter en liten stund kom den mellersta bocken Bruse.')

def secondBrotherCont1() :
  print('Berättaren:\n Kloppetiklopp lät det när mellersta bocken Bruse hoppsade sig över bron.')

def secondBrotherCont4() :
  print('Berättaren:\n Ödet rullar en D20 tärning. Tärningen måste visa 10 eller mer för att mellersta bocken Bruse ska klara sig.')

# Om D20 är över/lika med 10 = vinn, annars förlora
def secondBrotherSurvival() :
  roll = randomD20()
  if roll < 7 :
    print('Berättaren:\n Ödet rullade en ' + str(roll) + '\n Trollet drop-kickade mellersta bocken Bruse rakt i fejan så han däckade och fortsatte sedan i lugn takt att äta upp honom.')
  else :
    print('Berättaren:\n Ödet rullade en ' + str(roll) + '\n Igen, denna gången ännu mer motvilligt, lät trollet även mellersta bocken Bruse passera över bron, men lovade sig själv att nästa bock som kom förbi inte skulle komma så lätt undan...')

# THIRD BROTHER

def thirdBrotherStart() :
  print('Berättaren:\n Rätt som det var kom den stora bocken Bruse.')

def thirdBrotherCont1() :
  print('Berättaren:\n Klamp, klamp, klamp lät de säkra stegen från stora bocken Bruse när han började gå över bron.')

def thirdBrotherCont4() :
  print('Berättaren:\n Ödet rullar en D20 tärning. Tärningen måste visa 13 eller mer för att stora bocken Bruse ska klara sig.')

# Om D20 är över/lika med 13 = vinn, annars förlora
def thirdBrotherSurvival() :
  roll = randomD20()
  if roll < 7 :
    print('Berättaren:\n Ödet rullade en ' + str(roll) + '\n Striden var episk. Det såg länge ut som att ena parten skulle vinna innan den andre varje gång lyckades få överhanden igen. Tillslut, när röken skingrade sig stod trollet kvar som ensam segrare. Det hade varit en bra dag och det skulle gå flera veckor tills han behövde äta igen. Och då skulle han vara redo...')
    everyoneDies()
  else :
    print('Berättaren:\n Ödet rullade en ' + str(roll) + '\n Striden var episk. Det såg länge ut som att ena parten skulle vinna innan den andre varje gång lyckades få överhanden igen. Tillsut, när röken lagt sig stod stora bocken Bruse över kötthögen som brukade vara trollet. Området +/- 50 meter kring bron skulle komma att vara fredligt i generationer framåt.')
    everyoneSurvives()


