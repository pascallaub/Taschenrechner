def Taschenrechner():
    zahl1 = float(input("Gib eine Zahl ein: "))
    zahl2 = float(input("Gib eine weitere Zahl ein: "))
    operator = input("Wähle '+', '-', '/', '*': ")

    if operator == '+':
        ergebnis = zahl1 + zahl2
    elif operator == '-':
        ergebnis = zahl1 - zahl2
    elif operator == '/':
        if zahl2 != 0:
            ergebnis = zahl1 / zahl2
        else:
            return("Divison durch 0 nicht möglich! Lernt man in der Schule!")
    elif operator == '*':
        ergebnis = zahl1 * zahl2
    else:
        return("Ungültige Eingabe!")

    return f"Das Ergebnis ist: {ergebnis}"

while True:
    print(Taschenrechner())
    neue_rechnung = input("Möchtest du eine weitere Rechnung durchführen? j/n: ")
    if neue_rechnung == 'j':
        continue
    else:
        break