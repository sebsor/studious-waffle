thirdBrotherNameInput1 = ""
thirdBrotherInput2 = ""

def thirdBrotherName() :
    global thirdBrotherNameInput1 
    thirdBrotherNameInput1 = input('Vad heter stora bocken Bruse?\n')

def thirdBrotherJourney() :
    global thirdBrotherInput2
    thirdBrotherInput2 = input('Vad vill du att ' + thirdBrotherNameInput1 + ' ska göra?\n Se sig om\n Ropa\n Dansa\n Gå över bron\n')
    while thirdBrotherInput2.lower() != "gå över bron" :
        if thirdBrotherInput2.lower() == 'se sig om' :
            print('Stora bocken ' + thirdBrotherNameInput1 + ' ser sig om. Han ser en bro framför sig och några fåglar i fjärran, men inte mycket mer än så...')
        elif thirdBrotherInput2.lower() == 'ropa' :
            print('Stora bocken ' + thirdBrotherNameInput1 + ' skriker "Hallå!" och hans eko svarar "Halloj!" tillbaka.')
        elif thirdBrotherInput2.lower() == 'dansa' :
            print('Stora bocken ' + thirdBrotherNameInput1 + ' är för cool för att dansa. "Aint nobody got time for that!"')
        else :
            print('Stora bocken ' + thirdBrotherNameInput1 + ' tycker att han behöver tänka igenom det en gång till.')
        thirdBrotherInput2 = input('Vad vill du att ' + thirdBrotherNameInput1 + ' ska göra?\n Se sig om\n Ropa\n Dansa\n Gå över bron\n')
    print('Stora bocken ' + thirdBrotherNameInput1 + ' börjar med självsäkra steg att gå över bron.')

def thirdBrotherCont2() :
    print('Stora bocken Bruse:\n ”Det är jag, den stora bocken Bruse ' + thirdBrotherNameInput1 + "!" + ' Jag ska till ängen för att jag känner för det."')

def thirdBrotherCont3() :
    print('Stora bocken Bruse:\n "You are a fool, Troll..."')
