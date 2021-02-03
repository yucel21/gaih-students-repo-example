#YUCEL TASKIRAN

#1 Create a List and swap the second half of the list with first half of the list and print this list on the screen
List = [1,2,3,4,5,6]
newList=List[:3]
newList2 = List[3:]
List = newList2 + newList
print(List)

#2 Ask the user to input a single digit integer to a variable "n".
# Then, print out all of the even numbers from 0 to n(including n)

n = int(input("Enter a number please: "))
if int(n)>=0:
    print("Even Numbers : ")
    for i in range(n+2):
        if i % 2 == 0:
            print(i)
