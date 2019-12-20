icecream = {
    "Strawberry" : 50,
    "Vannila" : 50,
   "Choclete" : 50,
}
print(icecream)
input1 = input("How many times do you want to print it:  ")
integer = int(input1)
constructor = list()

for c in range(integer):
    input2 = fruits[input("Enter what flavor you want:  ")]
    print("The price of the flavor is " + str(input2))
    
    
    constructor.append(input2)
    
    total = sum(constructor)
    
    
    print("Your total of the flavors " + str(total))