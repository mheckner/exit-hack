import time, sys
from termcolor import colored

correctNumbers = """1598489145
1265411859
5584687676
6875615874
9878542862
6652144876
3765284974
9645267576
7845184516
1598489145
1265411859
5584687676
6875615874
9878542862
6652144876
3765284974
9645267576
7845184516

1598489146
1265411860
5584687677
6875615875
9878542863
6652144877
3765284975
9645267577
7845184517
1598489146
1265411860
5584687677
6875615875
9878542863
6652144877
3765284975
9645267577
7845184517

1598489147
1265411861
5584687678
6875615876
9878542864
6652144878
3765284976
9645267578
7845184518
1598489147
1265411861
5584687678
6875615876
9878542864
6652144878
3765284976
9645267578
7845184518
"""

def main(file):
    printSubmissionProgress()
    print()
    printCheckingProgress()
    compareFiles(file)

def compareFiles(file):
    with open(file, 'r') as file:
        data = file.read()
    if (correctNumbers.strip() == data.strip()):
        print(colored('Die Zahlen stimmen! Öffnen Sie den gründne Umschlag.', 'green'))
    else:
        print(colored('Sorry, Zahlen stimmen nicht überein! Versuchen Sie es weiter.', 'red'))

def printSubmissionProgress():
    items = list(range(0, 20))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Uploading File:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Uploading File:', suffix = 'Complete', length = 50)

def printCheckingProgress():
    items = list(range(0, 35))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Checking File:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Checking File:', suffix = 'Complete', length = 50)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(colored('Fehler! Korrekter Aufruf: python3 submit.py numbers.csv', 'red'))
        exit()
    try:
        open(sys.argv[1], "r")
    except IOError:
        print(colored("Fehler: Datei " + sys.argv[1] + " existiert nicht.", "red"))
        exit()
    main(sys.argv[1])
