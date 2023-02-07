#acronyms = ["LOL", "IDK", "SMH", "TBH"]


# List
# acronyms = []
# acronyms.append("LOL")
# acronyms.append("IDK")
# acronyms.append("SMH")
# acronyms.append("TBH")
# acronyms.remove("LOL")
# del acronyms[2]

# #print(acronyms)

# if "SMH" in acronyms :
#     print("true")
# else :
#     print("false")


# Dictionary (collection of lists)
from gettext import translation
from subprocess import call


acronyms = {
    'LOL' : 'laugh out loud',
    'IDK' : "I don't know",
    'TBH' : 'to be honest'
}
# If key exists --> changing value. If key doesn't exist --> Create
acronyms['TBHA'] = 'honestly'


# Removing dictionary item
#del acronyms['LOL']




#sentence = 'IDK' + ' what happened ' + 'TBH'

# Get the values from the dictionary
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')
print(translation)


# Print out specific key value
# print(acronyms['TBH'])