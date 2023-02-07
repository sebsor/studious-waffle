secondBrotherNameInput1 = ""
secondBrotherInput2 = ""

def secondBrotherName() :
    global secondBrotherNameInput1 
    secondBrotherNameInput1 = input('Vad heter mellersta bocken Bruse?\n')

def secondBrotherJourney() :
    global secondBrotherInput2
    secondBrotherInput2 = input('Vad vill du att ' + secondBrotherNameInput1 + ' ska göra?\n Se sig om\n Ropa\n Dansa\n Sov\n Gå över bron\n')
    while secondBrotherInput2.lower() != "gå över bron" :
        if secondBrotherInput2.lower() == 'se sig om' :
            print('Mellersta bocken ' + secondBrotherNameInput1 + ' ser sig om, men det enda han ser är bron framför sig och gräs som svajar i vinden...')
        elif secondBrotherInput2.lower() == 'ropa' :
            print('Mellersta bocken ' + secondBrotherNameInput1 + ' ropar ut, men ingen svarar...')
        elif secondBrotherInput2.lower() == 'dansa' :
            print('Mellersta bocken ' + secondBrotherNameInput1 + ' busts out some sweet moves. Synd att ingen är här för att se dem...')
        elif secondBrotherInput2.lower() == 'sov' :
            print('Mellersa bocken ' + secondBrotherNameInput1 + ' tar sig en 15 minuter power nap och känner sig utvilad.')
        else :
            print('Mellersta bocken ' + secondBrotherNameInput1 + ' vet inte vad han vill göra och tänker över sina val igen...')
        secondBrotherInput2 = input('Vad vill du att ' + secondBrotherNameInput1 + ' ska göra?\n Se sig om\n Ropa\n Dansa\n Sov\n Gå över bron\n')
    print('Mellersta bocken ' + secondBrotherNameInput1 + ' börjar glatt visslandes att gå över bron...')

def secondBrotherCont2() :
    print('Mellersta bocken Bruse:\n ”Det är den mellersta bocken Bruse ' + secondBrotherNameInput1 + "," + ' och jag ska till ängen och bli stor och rippad."')

def secondBrotherCont3() :
    print('Mellersta bocken Bruse:\n "Nej, nej, nej, ta inte mig! Ta den som är efter mig! Ta du stora bocken, stor och fet och tjock en."')
