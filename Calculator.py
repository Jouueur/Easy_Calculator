
def addition(a,b):
    return str(a+b)

def subtraction(a,b):
    return str(a-b)

def multiplication(a,b):
    return str(a*b)

def division(a,b):
    return str(a/b)


print("Here is a calculator ?")

# Display of the various possible operations
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

verification = False
# Loop that checks if the choice of operation is valid
while verification == False:
    choix = int(input("Quelle opération ? (1/2/3/4): "))
    if choix == 1 or choix == 2 or choix == 3 or choix == 4 :
        verification = True

# Choice of the two numbers to calculate
number1 = int(input("Premier number: "))
number2 = int(input("Deuxième number: "))

# Choice of operation
if choix == 1:
    print("The result is : " + addition(number1,number2))
elif choix == 2:
    print("The result is : " + subtraction(number1,number2))
elif choix == 3:
    print("The result is : " + multiplication(number1,number2))    
elif choix == 4:
    print("The result is : " + division(number1,number2))

