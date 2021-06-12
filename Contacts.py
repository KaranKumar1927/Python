contacts = {
    "nummber":4,
    "Students":
      [
       {"name":"Karan","email":"karan@smart.com","age":"22"},
       {"name":"Riya","email":"Riya@cute.com","age":"23"},
       {"name":"Harshitha","email":"Harshitha@cool.com","age":"21"},
    ]
}

for students in contacts["Students"]:
    print(students["email"])
