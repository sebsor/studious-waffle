import random


# ROll D20
def randomD20() :
  dice_total = random.randint(1,20)
  return dice_total




# import threading
# playInputTest = ''

# def functionOne() :
#   while playInputTest :
#       playInputTest = input('Vad heter du?\n')
#       if playInputTest :
#         print('Hello',playInputTest)
#         break
#       else :
#         print("Vad sa du att du hette nu igen?")

# def functionTwo() :
#   print('Ska inte komma förrän första kört klart!')



# def functionOne() :
#   playInputTest = input('Vad heter du?\n')
#   print('Hejsan', playInputTest)

# def functionTwo() :
#   print('Ska inte komma förrän första kört klart.')

# def functionOne():
#   while True:
#       playInputTest = input('Vad heter du?\n')
#       if playInputTest:
#         print('Hello',playInputTest)
#         break
#       else:
#         print("Vad sa du att du hette nu igen?")

# def functionTwo() :
#   print('Ska inte komma förrän första kört klart.')

# t1 = threading.Thread(target=functionOne)
# t2 = threading.Thread(target=functionTwo)
# t1.start()
# t1.join()
# t2.start()
