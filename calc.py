def main():
    try :
        number1 = int(input("enter the number : "))
        number2 = int(input("enter the other number : "))
    except ValueError:
        print("value error")
        exit()
    try :
        calc = int(input("""chose the number
        1 = addition (+)
        2 = subtraction (-)
        3 = multiplication (*)
        4 = division (/)
        5 = exponentiation (**)
        6 = all
        """))
        if calc == 1 :
            print(jam(number1 , number2))
        elif calc == 2 :
            print(tar(number1 , number2))
        elif calc == 3 :
            print(dar(number1, number2))
        elif calc == 4 :
            print(qis(number1, number2))
        elif calc == 5 :
            print(pui(number1 , number2))
        elif calc == 6 :
            print(str(jam(number1 , number2)) + "\n"+ str(tar(number1 , number2)) + "\n" + str(dar(number1, number2)) + "\n" + str(qis(number1, number2)) + "\n" + str(pui(number1 , number2)))
    except ValueError :
        print("value error")
        exit()



def jam(num1 , num2) :
    return num1 + num2


def tar(num1 , num2) :

        return num1 - num2


def dar(num1 , num2) :
        return num1 * num2

def qis(num1 , num2) :

        return num1 / num2


def pui(num1 , num2) :
        return num1 ** num2


main()