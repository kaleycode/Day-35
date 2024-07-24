import os, time
myList = []
def printList():
  print()
  for items in myList:
    print(items)
    print()

while True:
  menu = input("\tList\nDo you want to view, add, edit, remove or delete the list?\n")
  if menu == "add":
    item = input("What should I add to the list?: ")
    myList.append(item)
  elif menu == "view":
    printList()
  elif menu=="edit":
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(myList)):
      if myList[i]==item:
        myList[i]=new
  elif menu=="delete":
    myList = []
  elif menu == "remove":
    item = input("What should I remove from the list?: ")
    if item in myList:
      yesOrNo = input("Are you sure you want to remove this?\n")
      if yesOrNo == "yes" or yesOrNo =="Yes":
        myList.remove(item)
    else:
      print(f"{item} was not in the list")

  time.sleep(1)
  os.system("clear")
