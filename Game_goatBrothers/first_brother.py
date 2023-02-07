import sys
firstBrotherNameInput1 = ""
firstBrotherInput2 = ""

def firstBrotherName() :
    global firstBrotherNameInput1 
    firstBrotherNameInput1 = input('Vad heter yngsta bocken Bruse?\n')

def firstBrotherJourney() :
    global firstBrotherInput2
    firstBrotherInput2 = input('Vad vill du att ' + firstBrotherNameInput1 + ' ska göra?\n Se sig om\n Ropa\n Dansa\n Gå över bron\n')
    while firstBrotherInput2.lower() != "gå över bron" :
        if firstBrotherInput2.lower() == 'se sig om' :
            print('Yngsta bocken ' + firstBrotherNameInput1 + ' ser sig om, men det enda han ser är bron framför sig och gräs som svajar i vinden...')
        elif firstBrotherInput2.lower() == 'ropa' :
            print('Yngsta bocken ' + firstBrotherNameInput1 + ' ropar ut, men ingen svarar...')
        elif firstBrotherInput2.lower() == 'dansa' :
            print('Yngsta bocken ' + firstBrotherNameInput1 + ' dansar en crappy variant av Macarena. Tur att ingen är här för att se det...')
        else :
            print('Yngsta bocken ' + firstBrotherNameInput1 + ' vet inte vad han vill göra och tänker över sina val igen...')
        firstBrotherInput2 = input('Vad vill du att ' + firstBrotherNameInput1 + ' ska göra?\n Se sig om\n Ropa\n Dansa\n Gå över bron\n')
    print('Yngsta bocken ' + firstBrotherNameInput1 + ' börjar ängsligt att gå över bron...')

def firstBrotherCont2() :
    print('Yngsta bocken Bruse:\n ”Det är den minsta bocken Bruse ' + firstBrotherNameInput1 + "," + ' och jag ska till ängen och bli stor och fet."')

def firstBrotherCont3() :
    print('Yngsta bocken Bruse:\n "Nej, nej, nej, ta inte mig! Ta den som är efter mig! Ta du mellan bocken, stor och fet och tjock en."')

