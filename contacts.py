contacts = {
    "numer" : 4,
    "students" :
    [
        {"name" : "Sebastian Dahlgren", "email" : "sebastian@example.com"},
        {"name" : "Harry Potter", "email" : "harry@example.com"},
        {"name" : "Hermione Granger", "email" : "hermionen@example.com"},
        {"name" : "Ron Weasley", "email" : "ron@example.com"},
    ]
}

for student in contacts["students"] :
    print(student["name"])
    print(student["email"])