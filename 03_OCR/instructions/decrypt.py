import sys

def main():
    key = 7
    sentence = readSentenceFromFile()
    decryptedSentence = decryptSentence(sentence, key)
    print(decryptedSentence)

def decryptChar(char, key):
    originalCharAscii = ord(char)
    if ((char >= "a" and char<="z") or (char >= "A" and char<="Z")):
        if (char.isupper()):
            alphabetShift = ord("A")
        else:
            alphabetShift = ord("a")
        originalCharIndex = originalCharAscii - alphabetShift

        decryptedCharIndex = (originalCharIndex - key) % 26
        decryptedCharAscii = decryptedCharIndex + alphabetShift
        char = chr(decryptedCharAscii)
    return char

def decryptSentence(sentence, key):
    decryptedSentence = ""
    for char in sentence:
        char = decryptChar(char, key)
        decryptedSentence = decryptedSentence + char
    return decryptedSentence

def readSentenceFromFile():
    encryptedSentence = open("encrypted_message.txt", "r").read()
    return encryptedSentence

if __name__ == "__main__":
    main()
