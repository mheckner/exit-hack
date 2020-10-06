def main():
    message = getMessage()
    printMessage(message)

def getMessage():
    msg = "Hello World!"
    return msg

def printMessage(msg):
    print(msg)

if __name__ == "__main__":
    main()
