from narrator import introScene, firstBrotherStart, firstBrotherCont1, firstBrotherCont4, firstBrotherSurvival, secondBrotherStart, secondBrotherCont1, secondBrotherCont4, secondBrotherSurvival, thirdBrotherStart, thirdBrotherCont1, thirdBrotherCont4, thirdBrotherSurvival
from troll import genericTrollQuestion
from first_brother import firstBrotherName, firstBrotherJourney, firstBrotherCont2, firstBrotherCont3
from second_brother import secondBrotherName, secondBrotherJourney, secondBrotherCont2, secondBrotherCont3
from third_brother import thirdBrotherName, thirdBrotherJourney, thirdBrotherCont2, thirdBrotherCont3
from ending_images import everyoneDies, everyoneSurvives
from other import randomD20

introScene()
firstBrotherStart()
firstBrotherName()
firstBrotherJourney()
firstBrotherCont1()
genericTrollQuestion()
firstBrotherCont2()
firstBrotherCont3()
firstBrotherCont4()
firstBrotherSurvival()

secondBrotherStart()
secondBrotherName()
secondBrotherJourney()
secondBrotherCont1()
genericTrollQuestion()
secondBrotherCont2()
secondBrotherCont3()
secondBrotherCont4()
secondBrotherSurvival()

thirdBrotherStart()
thirdBrotherName()
thirdBrotherJourney()
thirdBrotherCont1()
genericTrollQuestion()
thirdBrotherCont2()
thirdBrotherCont3()
thirdBrotherCont4()
thirdBrotherSurvival()

# from other import functionOne, functionTwo
# import threading
# t1 = threading.Thread(target=functionOne)
# t2 = threading.Thread(target=functionTwo)
# t1.start()
# t1.join()
# # t2.start()