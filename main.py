import math

def addition():
    zahl1 = float(input('Geben Sie Summand 1 ein: '))
    zahl2 = float(input('Geben Sie Summand 2 ein: '))
    print (f'Summe: {zahl1 + zahl2}\n')

def subtraktion():
    zahl1 = float(input('Geben Sie den Minuend ein: '))
    zahl2 = float(input('Geben Sie den Subtrahend ein: '))
    print (f'Differenz: {zahl1 - zahl2}')

def multiplikation():
    zahl1 = float(input('Geben Sie Faktor 1 ein: '))
    zahl2 = float(input('Geben Sie Faktor 2 ein: '))
    print (f'Produkt: {zahl1 * zahl2}\n')

def division():
    zahl1 = float(input('Geben Sie den Dividend ein: '))
    zahl2 = 0
    while zahl2 == 0:
        zahl2 = float(input('Geben Sie den Divisor ein: '))
        if zahl2 == 0:
            print(f'Division durch null is nicht moeglich.')

    print(f'Quotient: {zahl1 / zahl2}\n')

def potenzieren():
    zahl1 = float(input('Geben Sie die Basis ein: '))
    zahl2 = float(input('Geben Sie den Exponet ein: '))
    print (f'Ergebnis: {zahl1 ** zahl2}\n')

def sqrt():
    zahl1 = float(input('Geben Sie den Radikand ein: '))
    print (f'Ergebnis: {math.sqrt(zahl1)}\n')

def cbrt():
    zahl1 = float(input('Geben Sie den Radikand ein: '))
    print (f'Ergebnis: {math.cbrt(zahl1)}\n')

def main():
    while True:
        try:
            select = int(input('\nBitte wählen Sie aus -\n'
                               '1. Addition\n'
                               '2. Subtraktion\n'
                               '3. Multiplikation\n'
                               '4. Division\n'
                               '5. Potenzieren\n'
                               '6. 2. Wurzel ziehen\n'
                               '7. 3. Wurzel ziehen\n'
                               '8. Quit\n'))
        except ValueError as e:
            print(f'{e} Error, \n Ungültige Option...')
            continue

        if select == 1:
            addition()

        elif select == 2:
            subtraktion()

        elif select == 3:
            multiplikation()

        elif select == 4:
            division()

        elif select == 5:
            potenzieren()

        elif select == 6:
            sqrt()

        elif select == 7:
            cbrt()

        elif select == 8:
            break

        else:
            print ('Ungültige Option!')

if __name__ == '__main__':
    main()
