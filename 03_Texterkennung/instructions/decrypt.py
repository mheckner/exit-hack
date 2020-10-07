import sys
from time import sleep
from progress.spinner import PixelSpinner

def main():
    key = 7
    sentence = readSentenceFromFile()
    showProgress()
    decryptedSentence = decryptSentence(sentence, key)
    print(decryptedSentence)

def showProgress():
    with PixelSpinner('Entschlüsselung läuft...') as bar:
        for i in range(100):
            sleep(0.06)
            bar.next()

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
    encryptedSentence = open("encrypted_message.text", "r").read()
    return encryptedSentence

if __name__ == "__main__":
    main()
