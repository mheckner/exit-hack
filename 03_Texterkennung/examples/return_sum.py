def main():
    firstNumber = 2
    secondNumber = 40
    sum = calculateSum(firstNumber, secondNumber)
    printSum(sum)

def calculateSum(firstNum, secondNum):
    sum = firstNum + secondNum
    return sum

def printSum(sum):
    print("Dein Ergebnis: ")
    print(sum)

if __name__ == "__main__":
    main()
