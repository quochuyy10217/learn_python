import fraction_lib
import os
while True:
    os.system("clear")
    print("----Fraction Calculator----")
    print("1.Adding Fraction")
    print("2.Subtracting Fraction")
    print("3.Multiplying Fraction")
    print("4.Dividing Fraction")
    print("0.Quit")
    option = int(input("Your Option Is: "))
    if (option>0) & (option<5):
        num_a = int(input("Numerator of fraction A is: "))
        den_a = int(input("Denominator of fraction A is: "))
        num_b = int(input("Numerator of fraction B is: "))
        den_b = int(input("Denominator of fraction A is: "))
        fraction_a = fraction_lib.fraction(num_a,den_a)
        fraction_b = fraction_lib.fraction(num_b,den_b)
        if option==1:
            result=fraction_a+fraction_b
            print("Result of A+B is: " + str(result))
            newfrac=fraction_lib.fraction(result[0],result[1])
            print("The reduction of result is: "+str(newfrac.fraction_reduction()))
        elif option==2:
            result=fraction_a-fraction_b
            print("Result of A-B is: " + str(result))
            newfrac=fraction_lib.fraction(result[0],result[1])
            print("The reduction of result is: "+str(newfrac.fraction_reduction()))
        elif option==3:
            result=fraction_a*fraction_b
            print("Result of A*B is: " + str(result))
            newfrac=fraction_lib.fraction(result[0],result[1])
            print("The reduction of result is: "+str(newfrac.fraction_reduction()))
        else:
            result=fraction_a/fraction_b
            print("Result of A/B is: " + str(result))
            newfrac=fraction_lib.fraction(result[0],result[1])
            print("The reduction of result is: "+str(newfrac.fraction_reduction()))
        print("Do you want to continue? Y/N")
        loop = input("Your Option Is: ")
        if (loop=='Y'):
            continue
        else:
            break
    elif option==0:
        print("Exitting the program!")
        break
    else:
        print("Your option is not valid!")
        print("Press any key to return to the menu: ")
        temp = input()