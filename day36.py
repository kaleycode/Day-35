nameList = []
def printList():
   print()
   for name in nameList:
     print(name)
   print()

while True:
   print()
   firstName = input("What is your first name? ").strip().capitalize()
   lastName = input("What is your last name? ").strip().capitalize()
   name = f"{firstName} {lastName} "
   if name not in nameList:
     nameList.append(name)
   else:
     print("ERROR: Duplicate name")
   printList()