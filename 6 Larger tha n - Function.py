

def LargerThanN(numbers,number):
    for i in numbers:
        if i > number:
            print(i)

numbers=[10,20,30,40,50,60,70,80,90]
number=int(input("Input a number: "))

LargerThanN(numbers,number)
