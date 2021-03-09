import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

def main():
    transmit()

def transmit():
    alphabet, morse = readMorsealphabet()
    data = fileToList("Test.txt")

    print(data)

    for char in data:
        if (char.isspace()):
            time.sleep(20)

        else:
            index = alphabet.index(char)
            code = morse[index]
            for c in code:
                if (c == "S"):
                    GPIO.output(26, True)
                    print("S")
                    time.sleep(1)
                    GPIO.output(26, False)
                elif (c == "L"):
                    GPIO.output(26, True)
                    print("L")
                    time.sleep(3)
                    GPIO.output(26, False)
                time.sleep(1)


def readMorsealphabet():
    file = open("morsealphabet.txt", "r")

    alphabet = []
    morse = []
    for line in file:
        alphabet.append(line[0])
        m = []
        for code in line[2:]:
            if (code != "\r" and code != "\n"):
                m.append(code)
        morse.append(m)

    file.close()

    return alphabet, morse

def fileToList(fname):
    file = open(fname, "r")

    data = []
    for line in file:
        for char in line:
            data.append(char)

    file.close()

    return data

if __name__ == "__main__":
    main()