'''''''''Mandatory Task 1: Fraction Calculator'''''''''
'''''''''''''Alejandro Reyes Martin'''''''''''''
''''''''''''''''''"14.11.2022"''''''''''''''''''

# input of the first fraction
Numerator_1=int(input("Numerator of the 1st fraction: "))       #Numerator of 1st fraction must be specified by the user
Denominator_1=int(input("Denominator of the 1st fraction: "))   #Denominator of 1st fraction must be specified by the user

# input of the second fraction
Numerator_2=int(input("Numerator of the 2nd fraction: "))       #Numerator of 2nd fraction must be specified by the user
Denominator_2=int(input("Denominator of the 2nd fraction: "))   #Denominator of 2nd fraction must be specified by the user

if (Denominator_1 != 0 and Denominator_2 !=0):      #"if" case to check if denominators are a number different than '0'

    ari=(input("Aritmetic process to be done (Type + , - , * or / ): "))    #Mathematical operation must be specified by the user

    #Addition of fractions
    def addition(num1,num2,den1,den2):      #Funciton for fraction addition is defined
        num_add=(num1*den2)+(num2*den1)     #Numerator of the final result is calculated by multiplying num1 by den2 and num2 by den1 and adding both results
        den_add=den1*den2                   #Denominator of the final result is calculated by multiplying den1 by den2
        deci_add=num_add/den_add            #To get the answer in decimal form, we devide numerator by denominator
        print(f"Fraction1 + Fraction2 (Fraction form)= {num_add}/{den_add}")    #Result in fraction form  
        print(f"Fraction1 + Fraction2 (Decimal form)= {deci_add:.2f}")          #Result in decimal form (2 decimals)

    #Subtraction of fractions
    def subtraction(num1,num2,den1,den2):   #Funciton for fraction subtraction is defined
        num_sub=(num1*den2)-(num2*den1)
        den_sub=den1*den2
        deci_sub=num_sub/den_sub
        print(f"Fraction1 - Fraction2 (Fraction form)= {num_sub}/{den_sub}")
        print(f"Fraction1 - Fraction2 (Decimal form)= {deci_sub:.2f}")

    #Multiplication
    def multiplication(num1,num2,den1,den2):    #Funciton for fraction multiplication is defined
        num_mul=num1*num2
        den_mul=den1*den2
        deci_mul=num_mul/den_mul
        print(f"Fraction1 * Fraction2 (Fraction form)= {num_mul}/{den_mul}")
        print(f"Fraction1 * Fraction2 (Decimal form)= {deci_mul:.2f}")

    #Division
    def division(num1,num2,den1,den2):      #Funciton for fraction division is defined
        num_div=num1*den2
        den_div=den1*num2
        deci_div=num_div/den_div
        print(f"Fraction1 / Fraction2 (Fraction form)= {num_div}/{den_div}")
        print(f"Fraction1 / Fraction2 (Decimal form)= {deci_div:.2f}")

    if ari=="+":                                                            #"If" to select the aritmetic procedure
        addition(Numerator_1,Numerator_2,Denominator_1,Denominator_2)       #Call addition function when ari is "+"

    elif ari=="-":
        subtraction(Numerator_1,Numerator_2,Denominator_1,Denominator_2)    #Call subtraction function when ari is "-"
        
    elif ari=="*":
        multiplication(Numerator_1,Numerator_2,Denominator_1,Denominator_2) #Call multiplication function when ari is "*"

    elif ari=="/":
        division(Numerator_1,Numerator_2,Denominator_1,Denominator_2)       #Call division function when ari is "/"
        
    else :
        print("INVALID CHARACTER \nPlease select between + , - , * or / \nRestart the programm")    #Ari is not valid

else:       
    print("Wrong input-Invalid Denominator. Please provide a number different to '0'")  #If a denominator is '0' we print this
                                                                                        #message to then restart the program

#What am I doing here

