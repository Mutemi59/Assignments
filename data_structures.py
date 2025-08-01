#Question 1

print("Enter numbers one by one(press Q to quit): ")
numInput = ""
numbersList = []

while(numInput != "Q" and numInput != "q"):
    numInput = input("")
    try:
        numbersList.append(int(numInput))
    except ValueError:
        if numInput != "Q" and numInput != "q":
            print("Only numers input allowed or (Q or q)")

totalSum = 0
print("\nThe sum of ")
for num in numbersList:
    print(num)
    totalSum += num
print(f"equals : {totalSum}")



#Question 2
fav_books = ("Atomic Habits", "The Son", "P is for Peril", "The 48 Laws of power", "The Art of War")

for book in fav_books:
    print(book)


#Question 3
print("______PERSONAL INFORMATION______")
info = dict()

info["Name"] = input("Enter Name : ")
info["Age"] = input("Enter Age : ")
info["Favorite Color"] = input("Enter Favorite Color : ")

print(info)


#Question 4
setA = set()
setB = set()

print("Enter numbers one by one for set A (press Q to quit): ")
numInput = ""

while(numInput != "Q" and numInput != "q"):
    numInput = input("")
    try:
        setA.add(int(numInput))
    except ValueError:
        if numInput != "Q" and numInput != "q":
            print("Only numers input allowed or (Q or q)")


numInput = ""
print("Enter numbers one by one for set B (press Q to quit): ")
while(numInput != "Q" and numInput != "q"):
    numInput = input("")
    try:
        setB.add(int(numInput))
    except ValueError:
        if numInput != "Q" and numInput != "q":
            print("Only numers input allowed or (Q or q)")


if len(setA) > 0 and len(setB) > 0:
    print("The common elements in set A and set B are:  ")
    for element in (setA & setB):
        print(element)



#Question 4

wordlist = ["Book", "School", "Ocean", "Computer", "Software", "Power", "Learn"]

oddWords = [word for word in wordlist if len(word) % 2 != 0]

print(oddWords)


    
