print("\tTo Do List Manager: \n")
myPartyList = []
def printList():
  print() 
while True:
  menu = input("Do you want to view, add or remove?\n")
  if menu == "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.append(item)
  elif menu == "view":
    for item in myPartyList:
      print(item)
    print() 
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      yesOrNo = input("Are you sure you want to remove this?\n")
      if yesOrNo == "yes" or yesOrNo =="Yes":
        myPartyList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()