def firstMethod():
    secondMethod()
print("Iam The first method")
def secondMethod():
    thirdMethod()
print("Iam The second method")
def thirdMethod():
    fourthMethod()
print("Iam The third method")
def fourthMethod():
    print("Iam The fourth method")