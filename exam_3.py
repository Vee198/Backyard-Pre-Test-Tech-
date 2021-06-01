import numpy as np
import numpy_financial as npf
import locale

#Create PMT(nper) function
def calculateMonthsUntilPaidOff():
    pv = int(input("What's your credit card balance? : "))
    apr = int(input("What's APR(%Per year) on your card?' : "))
    pmt = int(input("What's the monthly payment you can make? : "))
    nper = int(np.round(npf.nper((apr/100)/12,-(pmt),pv),0))
    return print("Calculate finished.\n\
It will take you " + str(nper) + " months to pay off this card.")
    calculateMonthsUntilPaidOff()


#Create PMT(payment) function
def calculatePaymentUntilPaidOff():
    pv = int(input("What's your credit card balance? : "))
    apr = int(input("What's APR(%Per year) on your card?' : "))
    nper = int(input("How many Installment payment month you can make? : "))
    pmt = int(np.round(npf.pmt((apr/100)/12,nper,pv,0,when='end'),0)) * -1
    return print("Calculate finished.\n\
You should Installment payment $" + str(f"{pmt:,}") + " per months to pay off this card.")
    calculatePaymentUntilPaidOff()


print("Welcome to Exam3 Calculate PMT\n\
You can choise 3 Option for calculate\n\
 1.Calculate month to pay off press : 1\n\
 2.Calculate Installment payment press : 2\n\
 3.Exit program press : Exit")
#main function
def main_calculate():
    welcome = input("Press your order here : ")
    while welcome != "":

        #if welcome.lower() == "exit":
            #print("Thank you for using program.")
            #break

        if welcome == "1":
            print("Welcome to Calculate month to pay off program.Please enter your information here.")
            calculateMonthsUntilPaidOff()
            main_calculate()

            
        elif welcome == "2":
            print("Welcome to Calculate Installment payment program.Please enter your information here.")
            calculatePaymentUntilPaidOff()
            main_calculate()
        
        elif (welcome != "1" and welcome != "2" and welcome != "exit"):
            print("Order : " + str(welcome) +" is not avaliable.Please try again.")
            main_calculate()
            
        elif welcome.lower() == "exit":
            print("Thank you for using program.")
            break
        break
            
    else:
        print("Order can't empty.Please enter your order or press exit.")
        main_calculate()

main_calculate()