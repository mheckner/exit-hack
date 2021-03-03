def main():
    geld = 2
    brotzeit = getLeberkaeseSemmel(geld)
    printBrotzeit(brotzeit)

def getLeberkaeseSemmel(geld):
    print("Kaufe ein für €")
    print(geld)
    return "Leberkäsesemmel"

def printBrotzeit(brotzeit):
    print("Deine Brotzeit: ")
    print(brotzeit)

if __name__ == "__main__":
    main()
